'''
Created on Dec 3, 2015

@author: Chris
'''
import re

user_input = input("Please enter the name of the file containing the input IP addresses:");



file = open(user_input, 'r');

number = file.readlines()

file.close()

pattern = '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$'


for line in number:
    yes = re.match(pattern, line)
    if yes is not None:
        print("Match found - valid IP address: " + line + "\n")
    else:
        print("Error - no match - invalid IP address: " + line + "\n")