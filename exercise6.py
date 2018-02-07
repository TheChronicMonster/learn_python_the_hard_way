# setting variables with string formatters. 
x= "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

# print first statements (what a joke)
print (x)
print (y)

# print statements with variables
print ("I said: %r." % x)
print ("I also said: '%s'." % y)

# setting new variables
hilarious = True
joke_evaluation = "Isn't that joke so funny?! %r"

# print joke and evaluation
print (joke_evaluation % hilarious)

# Setting new strings with vars w and e
w = "This is the left side of..."
e = "a string with a right side."

# print final statement, concatenating string
print (w + e)