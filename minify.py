#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import json

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


    Parameters
    ----------
    -s, --source : string, the path where your javascript files are.
        Must
    -l, --compilation_level : Chooses compilation level between 0 or 1.
        0 == WHITESPACE_ONLY
        1 == SIMPLE_OPTIMIZATIONS
        Optional
        default: 0


    Examples
    --------
    python minify.py -s /Users/jgasteiz/Desktop/javascript_files/

    or

    python minify.py -s /Users/jgasteiz/Desktop/javascript_files/ -l 1


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

    if settings['source_path'] == '':
        parser.add_argument('-s','--source_path', 
                        help='Source folder where original javascript files are', 
                        required=True)        
    if settings['destination_path'] == '':
        parser.add_argument('-d','--destination_path', default='min/',
                        help='Destination folder. If it does not exist, it\'ll be created', 
                        required=False)
    if settings['compilation_level'] == '':
        parser.add_argument('-l','--compilation_level', type=int, default=0, 
                        choices=range(0, 2), 
                        help="""Can choose between 0: WHITESPACE_ONLY, 
                        1: SIMPLE_OPTIMIZATIONS""")

    ARGS = vars(parser.parse_args())
    COMPILATION_LEVELS = ['WHITESPACE_ONLY', 'SIMPLE_OPTIMIZATIONS']

    if source_path == '':
        source_path = ARGS['source_path']        

    if not source_path[-1] == '/':
        source_path = source_path + '/'

    if destination_path == '':
        destination_path = ARGS['destination_path']
        
    if not destination_path[0] == '/':
        destination_path = source_path + destination_path
    if not destination_path[-1] == '/':
        destination_path = destination_path + '/'
    
    if compilation_level == '':
        compilation_level = COMPILATION_LEVELS[ARGS['compilation_level']]

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
            ' --js=' + max_name + ' --js_output_file=' +  min_name
            os.system(instruction + args)

if __name__ == "__main__":
    main()