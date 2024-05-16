#!/usr/bin/env python

# Day One Project Two
# Basic integer operations & decimal floats

# Tip Calculator
# Created by: TnTe3

# usage
# python3 tipCalc.py

# Ask customer for total bill amount, desired tip %, # of people paying

total = float(input('What is the total of the bill? '))
tip = int(input('What is the total of the bill? 5-20% '))
party = int(input('How many people are contributing?  '))

tip_percent = tip / 100
tip_total = total * tip_percent
bill_total = total + tip_total
total_amount = bill_total / party
final_amount = round(total_amount, 2)

print("The bill total is " + "$" + str(round(total, 2)))
print(F"Each person should pay: ${final_amount}")
