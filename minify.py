#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
import argparse

__author__ = 'Javi Manzano | https://github.com/jgasteiz'
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
	parser.add_argument('-s','--source', 
						help='Source folder where original javascript files are', 
						required=True)
	parser.add_argument('-l','--compilation_level', type=int, default=0, 
						choices=range(0, 2), 
						help="""Can choose between 0: WHITESPACE_ONLY, 
						1: SIMPLE_OPTIMIZATIONS""")
	ARGS = vars(parser.parse_args())

	# Determines the compilation_level
	COMPILATION_LEVELS = ['WHITESPACE_ONLY', 'SIMPLE_OPTIMIZATIONS']
	compilation_level = COMPILATION_LEVELS[ARGS['compilation_level']]

	# Source and destination paths
	source_path = ARGS['source']
	if not source_path[-1] == '/':
		source_path = source_path + '/'
	output_path = source_path + 'min/'

	# Creates the min/ dir
	if not os.path.exists(output_path):
		os.mkdir(output_path)

	# Creates/modifies .min.js files
	for file in os.listdir(source_path):
		if file.lower().endswith('js'):
			max_name = source_path + file
			min_name = output_path + file[:-3] + '.min.js'
			instruction = 'java -jar closure_compiler/compiler.jar' 
			args = ' --compilation_level ' + compilation_level + \
			' --js=' + max_name + ' --js_output_file=' +  min_name
			os.system(instruction + args)

if __name__ == "__main__":
	main()
