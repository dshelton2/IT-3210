#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
David Shelton

Assignment 2

This program should receive input from the user from both the command line arguments
used when launching the script and by use of prompts while the script is running. The
comments in this assignment give further guidance on what specific input is expected
and how it is to be handled.

Feel free to be creative and go beyond the minimum requirements. The primary learning
objective of this assignment is receiving user input, both from command line arguments
and within the program's execution. Can you incorporate any previously learned knowledge
about Python into this exercise?
"""

from sys import argv

script_name, user_name, age = argv
print "Hi, %r welcome to the %r script.\nGlad to see you're hanging in there at %r years old!!" % (user_name, script_name, age)

print "If it's alright I'm going to ask you a few questions...\n"

print "How many feet tall are you (excluding inches)? ", 
height_feet = int(raw_input())
height_inches = int(raw_input("How many inches tall are you (excluding feet)? "))

print "You are %d'%d\" tall...\nthat means" % (height_feet, height_inches), 

inches = height_feet * 12 + height_inches
print "You are %d inches tall!" % inches