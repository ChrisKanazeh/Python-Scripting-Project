'''

@author: Chris
'''
import re
user_input = input("Please enter the name of the file containin the input North American phone numbers:");
file = open(user_input, 'r');
zfile = file.readlines()
file.close()
pattern1 = '^[1-9][0-9]{2}.[1-9][0-9]{2}.[0-9]{4}$'
pattern2 ='^.[1-9][0-9]{2}..[1-9][0-9]{2}.[0-9]{4}$'
for eachline in zfile:
    yes = re.match(pattern1, eachline)
    yes2 = re.match(pattern2, eachline)
    if yes is not None:
        print("Match found - valid North American phone number: \n\t" + eachline + "\n")
    elif yes2 is not None:
        print("Match found - valid North American phone number: \n\t" + eachline + "\n")
    else:
        print("Error - no match - invalid North American phone number: \n\t" + eachline + "\n")
