#!/usr/bin/env python

# file.py Code
#
# Copyright (c) Jose M. Molero
#
# All rights reserved.
#
# MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a
# copy of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
# DEALINGS IN THE SOFTWARE.

"""
Code sample to

Notes:
- Insert notes

TODO list:
- Check if / at the end of --folder
- Add delete option

"""


# stdlib imports
import argparse
import errno
import os
import tarfile
import shutil
import string


# global variables
_SCRIPT_VERSION = '0.0.2'


def make_tarfile(output_filename, source_dir):
    """Create tarfile gz
    Parameters:
        output_filename
        source_dir
    Returns:
        Nothing
    Raises:
        Nothing
    """
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def main():
    """Main function
    Parameters:
        None
    Returns:
        Nothing
    Raises:
        ValueError for invalid arguments
    """
    # get args
    args = parseargs()

    # check parameters
    if os.path.isdir(args.folder) is not True:
        raise ValueError('Invalid folder directory')
    if os.path.isdir(args.destination) is not True:
        raise ValueError('Invalid destination directory')

    # Eliminate / at the end of the folder path

    # Change to destination folder
    os.chdir(args.destination)
    # Extract folder name
    folder_basename = os.path.basename(args.folder)
    # Create tar.gz
    make_tarfile(folder_basename + ".tar.gz", args.folder)


def parseargs():  # pragma: no cover
    """Sets up command-line arguments and parser
    Parameters:
        Nothing
    Returns:
        Parsed arguments
    Raises:
        Nothing
    """
    parser = argparse.ArgumentParser(description='Compress and move folders')
    parser.add_argument("--folder", required=True, help='specify the folder to compress')
    parser.add_argument("--destination", required=True, help='specify the folder to store the compressed folder')
    parser.add_argument("--delete", help='delete folder at the end')
    parser.add_argument("-v", "--version", help="show program's version number and exit", action='version', version=_SCRIPT_VERSION)
    return parser.parse_args()


if __name__ == '__main__':
    main()

