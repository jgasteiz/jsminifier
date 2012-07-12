# jsminifier

A simple python script that I use to minify my javascript files. It uses Google Closure Compiler Application to compile with two different levels of compilation: WHITESPACE_ONLY or SIMPLE_OPTIMIZATIONS.


You can specify the source folder (where your javascript files are) as an argument. It will generate a .min.js file for each .js file in the source folder and place them inside a "min" folder in the same source folder and override existing ones.

Example:

	python minify.py -s /absoloute_path/to_your/js_files/


There is also the option to specify the source and destination paths manually in a settings file, for more automated process. To do so, you have to open settings.json file and write down there your paths. 

You can also set the compilation level for your min.js files:
* WHITESPACE_ONLY: it will remove spaces and linebreaks
* SIMPLE_OPTIMIZATIONS: it will remove spaces, linebreaks and do some JavaScript obfuscation

In settings.json:

    {
        "source_path":  "/Users/jgasteiz/Desktop/lalala",
        "destination_path":  "/Users/jgasteiz/Desktop/nope",
        "compilation_level":  "SIMPLE_OPTIMIZATIONS"
    }

And the execution would be as simple as:

    python minify.py
