#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
David Shelton

Assignment 3

This program should receive two filenames from the user from the command line arguments
used when launching the script, and copy the first file into the second. Use the file
provided (infile.txt) as the input_file.
"""

from sys import argv
from os.path import exists
import os
input_file = argv[1]
output_file = argv[2]

# we don't use the script variable, so there is no need to assign it a value:
# use the indexing operator / slice techniques learned for strings and apply them to the
# argv attribute to ONLY extract the filenames (as discussed in last week's discussion 
# board).
# print the absolute path of each file using the relevant function from the os.path module
print os.path.abspath('%s')% input_file
print os.path.abspath('%s') % output_file
# combine the next two lines into one

indata = open(input_file).read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(output_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input("? ")

out_file = open(output_file, 'w')
out_file.write(indata)

# before closing the files, read the first 13 characters from the first file and print
# them to the console
thirteen = open(input_file).readline(13)
print thirteen 

# append the footer string to the output_file (do not overwrite any existing text)
outfile = open(output_file, 'a')
footer = 'The End'
outfile.write(footer)


# why are the next two lines important? - They save files that have been written to.
out_file.close()


