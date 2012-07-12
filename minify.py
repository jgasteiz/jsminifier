#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import json
import argparse

__author__ = 'Javi Manzano | https://github.com/jgasteiz'
__license__ = 'GPL'
__version__ = '0.1'
__email__ = 'javi.manzano.oller@gmail.com'


def main():
    """
    Description
    -----------
    Giving a source folder, this will minify javascript files in it and put
    them named as original_javascript_filename.min.js into a /source/min/
    folder.

    If specified in settings.json file, it will use a predefined source and
    destination folders, as well as the compilation_level selected

    Parameters
    ----------
    -s, --source : string, the path where your javascript files are.
        Must

    Examples
    --------
    python minify.py -s /Users/jgasteiz/Desktop/javascript_files/

    or if there is a source folder specified in settings.json

    python minify.py

    Notes
    -----
    Java must be installed.
    Closure Compiler Application documentation:
    https://developers.google.com/closure/compiler/docs/gettingstarted_app
    """

    # ArgumentParser
    parser = argparse.ArgumentParser(
        description='Minifies js code using google closure.')

    # Check for config file
    settings_file = open('settings.json')
    settings = json.load(settings_file)
    source_path = settings['source_path']
    destination_path = settings['destination_path']
    compilation_level = settings['compilation_level']
    settings_file.close()

    if source_path == '':
        parser.add_argument('-s', '--source_path',
                        help='Source folder where original javascript files are',
                        required=True)
    if destination_path == '':
        destination_path = 'min/'
    if compilation_level == '':
        compilation_level = 'WHITESPACE_ONLY'

    ARGS = vars(parser.parse_args())

    # Gets the source_path if it's blank on settings. Must end with '/'.
    if source_path == '':
        source_path = ARGS['source_path']
    if not source_path[-1] == '/':
        source_path = source_path + '/'

    # Checks if destination_path is relative or absolute. Must end with '/'.
    if not destination_path[0] == '/':
        destination_path = source_path + destination_path
    if not destination_path[-1] == '/':
        destination_path = destination_path + '/'

    # Creates the min/ dir
    if not os.path.exists(destination_path):
        os.mkdir(destination_path)

    # Creates/modifies .min.js files
    for file in os.listdir(source_path):
        if file.lower().endswith('js'):
            max_name = source_path + file
            min_name = destination_path + file[:-3] + '.min.js'
            instruction = 'java -jar closure_compiler/compiler.jar'
            args = ' --compilation_level ' + compilation_level + \
            ' --js=' + max_name + ' --js_output_file=' + min_name
            os.system(instruction + args)

if __name__ == "__main__":
    main()
