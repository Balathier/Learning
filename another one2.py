#! /usr/bin/env python3

# random printing exercises, using format, and printing multiples lines using "\n" and triple """

formatter = "{} {} {} {}"

days = "Sun, Mon, Tues, Wed, Thurs, Fri, Sat"
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print(formatter.format(
    "living in",
    "an old world",
    "of fools and",
    "gold"))

print(f"here are the days {days}")
print(f'Here are the Months: {months}')

# \t will do a horizontal tab, three " or ' can be used instead of \n

print('''
Many
Lines
So
\tBoring\'s''')

