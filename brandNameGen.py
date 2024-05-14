#!/usr/bin/env python

# Day One
# Collecting, storing and recalling user information

# Brand Name Generator
# Created by: TnTe3

# usage
# python3 brandNameGen.py

# user input

answer1 = input('What is your favorite color? ')
answer2 = input('Enter a verb that best describes your brand ')
answer3 = input('''if you'd like to include & with additional words: (hit enter to skip) ''')

# input manipulation
if not answer3:
    print('Your brand name is: ' + answer1.capitalize() + ' ' + answer2.capitalize())
else:
    print('Your brand name is: ' + answer1.capitalize() + ' ' + answer2.capitalize() + ' & ' + answer3.capitalize())
