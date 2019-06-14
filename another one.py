#! /usr/bin/env python3

#remember you can put a f in-front of the string and use {} instead of () in a string to call on a variable
# examples below

name = "Graham Parr"
height = 6
age = 8

print(f"Your name is {name}.")
print(f"you're {height} ft, and {age} years old.")

# printing two Variables in one string

we = "living la"
are = " vida loca"

print(we + are)

# formatting a sentence

living = False
question = "are you alive? {}"

print(question.format(living))
