#!/usr/bin/env python
# # -*- coding: utf-8 -*-

"""
Compare two directories containing text files

Given two directories: first check whether they contain only the same file
names and no other file names; then run a diff on each pair of files that
share the name in the two directories.
"""

import sys
import os
import difflib


def get_file_names(directory):
    """Get all files from the given directory and its subfolders."""
    file_names = []
    for (path, dirs, files) in os.walk(directory):
        file_names.extend([path + "/" + f for f in files])
    return file_names


dir1 = sys.argv[1]
dir2 = sys.argv[2]
files1 = get_file_names(dir1)
files2 = get_file_names(dir2)
files1.sort()
files2.sort()

for (f1, f2) in zip(files1, files2):
    short_name_1 = f1[len(dir1):]
    short_name_2 = f2[len(dir2):]
    print("===================")
    print(f"{short_name_1} vs. {short_name_2}")
    if short_name_1 != short_name_2:
        print(f'{f1} != {f2}')
    else:
        try:
            with open(f1, 'r') as f1read:
                with open(f2, 'r') as f2read:
                    diff = difflib.unified_diff(
                        f1read.readlines(),
                        f2read.readlines(),
                        fromfile=f1,
                        tofile=f2
                    )
                    for l in diff:
                        print(l)
        except UnicodeDecodeError:
            print(f"{short_name_1} or {short_name_2} not a text file?")
