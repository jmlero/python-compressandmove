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
- TODO
"""


# stdlib imports
import argparse
import errno
import os


# global variables
_SCRIPT_VERSION = '0.0.1'


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
    if len(args.localresource) < 1 or len(args.storageaccount) < 1 or \
            len(args.container) < 1:
        raise ValueError('invalid positional arguments')
    if args.upload and args.download:
        raise ValueError('cannot force transfer direction of download '
                         'and upload in the same command')
    if args.storageaccountkey is not None and args.saskey is not None:
        raise ValueError('cannot use both a sas key and storage account key')
    if args.pageblob and args.autovhd:
        raise ValueError('cannot specify both pageblob and autovhd parameters')


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
    parser.add_argument("-v", "--version", help="show program's version number and exit", action='version', version=_SCRIPT_VERSION)
    parser.add_argument("-f", "--folder", help='specify the folder to compress')
    parser.add_argument("-d", "--delete", help='delete folder at the end')
    return parser.parse_args()


if __name__ == '__main__':
    main()

