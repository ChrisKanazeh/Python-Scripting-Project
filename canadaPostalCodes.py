'''
Created on Dec 3, 2015

@author: Chris
'''
import re
user_input = input("Please enter the name of the file containing the input Canadian postal codes:");


file = open(user_input, 'r');
zt = file.readlines()
file.close()
pattern_1 = '^[0-9]{2,5}.[0-9a-zA-Z]+.[A-Za-z]+..[A-Za-z.]+..[A-Za-z.]+..[A-Za-z.]+..[ABCEGHJKLMNPRSTVXY][0-9A-Z]{2}.[0-9A-Z]{3}$'
pattern2 ='^[0-9]{2,5}.[0-9a-zA-Z]+.[A-Za-z]+..[A-Za-z.]+..[A-Za-z.]+..[ABCEGHJKLMNPRSTVXY][0-9A-Z]{2}.[0-9A-Z]{3}$'
for line in zt:
    yes = re.match(pattern_1, line)
    yes2 = re.match(pattern2, line)
    if yes is not None:
        print("Match found - valid Canadian address: \n\t" + line + "\n")
    elif yes2 is not None:
        print("Match found - valid Canadian address: \n\t" + line + "\n")
    else:
        print("Error - no match - invalid Canadian address: \n\t" + line + "\n")