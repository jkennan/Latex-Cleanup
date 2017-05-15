# Latex CLEANUP
A stupid python script that cleans up old and unnecessary Latex files, leaving only the remaining
.tex source files and .pdf result files

## About this project
This script does exactly what it says it does. It is basically nothing. But it works and it is useful.

### What it actually does
On run, this script asks for a full filepath to the folder you want to move. On a Windows machine,
this is most easily accomplished by navigating to the folder in File Explorer, and then copy-pasting
the path in the navigator bar into the script.
This script then moves remnant Latex files into a folder entitled `!LATEX-CLEANUP` as a subfolder
of the original given folder.

## Running the program
You must have Python 2.7 installed (*not* 3.x) to run this script.
To run, use a terminal to navigate to the folder in which the `.py` file is saved. Then
run the python script with `python Latex-Cleanup.py`. Be ready to paste or type the filepath.

## Warnings
**There are a couple of important notes about using this script, because it can have unintended
consequences.**

Perhaps most importantly, this script operates simply by looking at file extensions. Latex, on
compilation, leaves behind a number of files. Their extensions are:
* .aux
* .fdb_latexmk
* .fls
* .log
* .txt
* .gz

Note the last 3: Latex leaves behind .log, .txt, and .gz files. What this means is that this script
will search through the entire folder and move ANY FILE with these extensions into the
`!LATEX-CLEANUP` folder. If you have any files at all with these extensions, they *will be moved*.
In the future, this can be avoided by having the script check that any file with these extensions
matches a file with a `.tex` extension, but that's not something I want to do during finals period.

As always, keep in mind that this script is directly manipulating the file system, and things can
and very well could go wrong. Use at your own risk.

## Credits
Created by Jeffrey Kennan, May 2017.
