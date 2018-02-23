print("How old are you?"), # changing spacing formalities per documenation
age = input()
print("How tall are you?"),
height = input()
print("How much do you weigh?"),
weight = input()

print("So, you're %r old, %s tall and %r heavy." % (age, height, weight))

# %r on var height prints '6\3"' 
# %s on var height prints 6'3"
# again proving that %s is better for printing outputs for users

print("What's your name?")
name = input()
print("What's your favorite color?")
color = input()
print("What city do you live in?")
city = input()

# the comma after the print command doesn't seem to matter in python3 like it did in python2
print("So your name is %s, your favorite color is %s, and you live in %s." % (name, color, city))