#!/usr/bin/env python

#   Copyright (C) 2024 Simon Crase

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

'''Find unreferenced image files'''

from os import listdir
from os.path import isfile, join, splitext
from re import compile
from time import time

def find_included_images(file_name,R):
    image_files = []
    with open(file_name) as f:
        for line in f:
            match = R.match(line)
            if match:
                image_files.append(match.group(1))
    return image_files

if __name__=='__main__':
    print (__doc__)
    start  = time()
    count_referenced = 0
    count_unreferenced = 0
    R = compile(r'\s*\\includegraphics.*\{(.*)\}.*')
    image_files = [find_included_images(file_name,R) for file_name in listdir('.')
                   if isfile(file_name) and splitext(file_name)[1]=='.tex']
    image_lookup = set([f for i in image_files for f in i])
    with open('rm.sh','w') as out:
        for image in listdir('figs'):
            if splitext(image)[0] not in image_lookup:
                out.write(f'git rm figs/{image}\n')
                count_unreferenced += 1
            else:
                count_referenced += 1

    percent_unreferenced = 100 * count_unreferenced/(count_referenced + count_unreferenced)
    print (f'{count_unreferenced} unreferenced images, {count_referenced} referenced, {percent_unreferenced:.1f}% unreferenced')
    elapsed = time() - start
    minutes = int(elapsed/60)
    seconds = elapsed - 60*minutes
    print (f'Elapsed Time {minutes} m {seconds:.2f} s')
