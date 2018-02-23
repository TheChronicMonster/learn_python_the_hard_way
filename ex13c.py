# Parameters, Unpacking, Variables

from sys import argv

script, cartoon_character, childhood_movie, super_hero = argv

print("This is the script:", script)
print((input("What's your name? "))) # Just playing with input here
name = input("What's your name, again? ")
print(cartoon_character, "Was", name, "'s favorite cartoon character.")
print(childhood_movie, "is a great film.")
print(super_hero, "is bad to the bone.")
city = input("What city did you grow up in? ")
print("So you grew up in", city, ", were given the name of", name,\
", and you like", cartoon_character, ",", childhood_movie, ", and",\
super_hero, ".")