#!/usr/bin/env python3

from sys import argv # importing modules

script, filename = argv # arguments for script and filename ex. HelloWorld.txt

txt = open(filename) # asking for filename

print(f'here\'s you file {filename}:') # printing text, and filename name
print(txt.read()) # printing information inside filename

txt.close() # closes the file

print('Type the filename again:') # asking for the filename again
file_again = input('> ') # asking for user input

txt_again = open(file_again) # command to open file again

print(txt_again.read()) # printing txt file info again

txt_again.close() # closes the file again