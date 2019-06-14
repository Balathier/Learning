#! /usr/bin/env python3

from sys import argv

# read the WYSS section for how to run this
# this is run by using terminal typing in -- python3 "Another one4".py first second third.

script, first, second, third = argv

print('The script is called:', script)
print('Your first variable is:', first)
print('Your second variable is:', second)
print('Your third variable is:', third)
