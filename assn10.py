#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
Student Name

Assignment 10

In this assignment, you will read the contents of a custom data file into a CSV file. You
will need to write custom code to parse this data type and determine appropriate column
headers on your own. You must identify the pattern and then parse the file. You may use
advanced string handling techniques, regular expressions, and any modules deemed helpful
to accomplish this task.

You will be parsing the included 'proprietary_data.txt' file, which contains data that
is structured in a proprietary way that you must determine. Put the first and last names
of each person in the file in separate columns in the CSV file. Do not put the numbers
at the beginning of each line in the CSV file nor any asterisks, only write the relevant 
data in each column.
"""

import csv
import itertools
from itertools import islice
from sys import argv
import string

infile = argv[1]
textfile = open('proprietary_data.txt', 'r')

headers = ['Serial', 'Make', 'Model', 'User']
lines = []

for line in textfile:
	line = line[5:]
	line = line.strip()
	line = line.strip('*')
	line = line.strip(' ')
	lines.append(line)

def groupIt(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())
	
with open(infile, 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(headers)
	writer.writerows(groupIt(lines, 4))
print lines
	
raw_input()
