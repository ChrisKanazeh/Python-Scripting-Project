'''
Created on Dec 3, 2015

@author: Chris
'''
import re
insert = input("Please enter the name of the file containing the input zipcodes:");

fileObject = open(insert, 'r')
LL = fileObject.readlines()
fileObject.close()
pattern_1 = '^[0-9][0-9][0-9][0-9][0-9]$'
pattern_2='^[0-9][0-9][0-9][0-9][0-9]\-+[0-9][0-9][0-9][0-9]$'
for row in LL:
    valid = re.match(pattern_1, row)
    valid2 = re.match(pattern_2,row)
    if valid is not None:
        print("Match found - valid U.S. zipcode: " + row + "\n")
    elif valid2 is not None:
        print("Match found - valid U.S. zipcode: " + row + "\n")
    else:
        print("Error - no match - invalid U.S. zipcode: " + row + "\n")