# jsminifier

* A simple command line tool to minify your javascript files.

It uses Google Closure Compiler Application to compile with two different levels
of compilation: WHITESPACE_ONLY or SIMPLE_OPTIMIZATIONS.

Examples:

	python minify.py -s /Users/jgasteiz/Desktop/javascript_files/


This will generate a .min.js file with its whitespaces and linebreaks removed for each .js file in javascript_files/. The script will create a min/ folder inside the source folder if it doesn't exist already.


	python minify.py -l 1 -s /Users/jgasteiz/Desktop/javascript_files/


The same as the other, but this time it goes further and shortens variable names too.