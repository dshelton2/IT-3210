#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
David Shelton

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
import re
import string

Serial = re.compile(r'\d+\*+\s+(DATA[a-zA-Z0-9]+)')
Other = re.compile(r'\d+\s(.*)')

textfile = open('proprietary_data.txt', 'r')

headers = ['Serial', 'Make', 'Model', 'First', 'Last']
lines = []

textfileData = textfile.readlines()

while len(textfileData) > 0:
  line = textfileData[0]

  del textfileData[0]

  if len(textfileData) < 1:
    break

  match = Serial.search(line)

  if match:
    itemData = {
      'serial': match.group(1),
      'make': 'unknown',
      'model': 'unknown',
      'user': 'unknown'
    }

    index = 0
    count = 0

    data = ['unknown', 'unknown', 'unknown']

    while index < len(textfileData) and Serial.search(textfileData[index]) == None and index < 4:
      match = Other.search(textfileData[index])

      if not match:
        break

      data[index] = match.group(1).strip('*')

      index += 1
      count += 1

    while count > 0:
      del textfileData[0]

      count -= 1

    itemData['make'] = data[0]
    itemData['model'] = data[1]
    itemData['user'] = data[2]

    lines.append(itemData['serial'])
    lines.append(itemData['make'])
    lines.append(itemData['model'])

    nameInfo = itemData['user'].rsplit(' ', 1)

    lines.append(nameInfo[0])

    if len(nameInfo) == 2:
      lines.append(nameInfo[1])

def groupIt(it, size):
    it = iter(it)
    return iter(lambda: tuple(islice(it, size)), ())

with open('prop_data.csv', 'w') as csvfile:
	writer = csv.writer(csvfile)
	writer.writerow(headers)
	writer.writerows(groupIt(lines, 5))

textfile.close()
