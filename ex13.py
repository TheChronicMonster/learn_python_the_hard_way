# Parameters, Unpacking, Variables

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

# To print this in the command line 
# $ python ex13.py first second third
# OR for variety
# $ python ex13.py first 2nd 3rd