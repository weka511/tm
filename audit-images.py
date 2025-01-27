#!/usr/bin/env python

#   Copyright (C) 2024-2025 Simon Crase

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.

#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.

'''
    Find unreferenced image files

    Build a dictionary of all image files that are included in each tex file.
    iterate through the images diretory to verify that image is actually included.
    If not, construct git rm command.
'''

from argparse import ArgumentParser

from os import listdir
from os.path import isfile, join, splitext
from time import time

def create_included_images(verbose):
    '''
    Create set of images that have been included with a tex includegraphics command
    '''
    def create_matches(file_name):
        '''
        Find images for one specified file
        '''
        Product = []
        with open(file_name) as file:
            if verbose:
                print (file_name)
            for line in file:
                trimmed = line.strip()
                if trimmed.startswith(r'\includegraphics'):
                    j = trimmed.find('{')
                    k = trimmed.find('}')
                    name = trimmed[j+1:k].strip()
                    if verbose:
                        print(f'\t{name}')
                    Product.append(name)

        return Product

    image_files = [create_matches(file_name) for file_name in listdir('.')
                   if isfile(file_name) and splitext(file_name)[1]=='.tex']
    return set([file_name for image_list in image_files for file_name in image_list])

def parse_arguments():
    parser = ArgumentParser(__doc__)
    parser.add_argument('--verbose',default=False,action='store_true',help='Used to list names of text files as they are processed')
    parser.add_argument('--figs', default = './figs')
    return parser.parse_args()

if __name__=='__main__':
    start  = time()
    args = parse_arguments()
    count_referenced = 0
    count_unreferenced = 0
    image_lookup = create_included_images(args.verbose)
    unreferenced = False
    with open('rm.sh','w') as out:
        if not unreferenced:
            print ('Unreferenced images')
            unreferenced = True
        for image in listdir(args.figs):
            if splitext(image)[0] not in image_lookup:
                print (f'\t{image}')
                out.write(f'git rm {args.figs}/{image}\n')
                count_unreferenced += 1
            else:
                count_referenced += 1

    percent_unreferenced = 100 * count_unreferenced/(count_referenced + count_unreferenced)
    print (f'{count_unreferenced} unreferenced images, {count_referenced} referenced, {percent_unreferenced:.1f}% unreferenced')
    elapsed = time() - start
    minutes = int(elapsed/60)
    seconds = elapsed - 60*minutes
    print (f'Elapsed Time {minutes} m {seconds:.2f} s')
