#! /usr/bin/env python3
from sys import argv

script, user_name = argv
prompt ='> '   # prompt user for input

print(f'hi {user_name}, I\'m the {script} script')
print('I\'d like you ask a few questions.')
print(f'Do you like me {user_name}?')
likes = input(prompt)

print(f'Where do you live {user_name}?')
lives = input(prompt)

print('What kind of computer do you have?')
computer = input(prompt)

print(f'''
Alright, so you said you {likes} about liking me.
you live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
 ''')
