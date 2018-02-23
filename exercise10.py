# Setting up vars
tabby_cat = "\tI'm tabbed in." # tab in
persian_cat = "I'm split\non a line." # new line
backslash_cat = "I'm \\ a \\ cat." # adds back slashes

# long string with tabs and new line
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# print commands
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

# Creates a revolving asterisk image in console. control + c to exit
# while True:
# 	for i in ["/","-","|","\\","|"]:
# 		print ("%s\r" % i,)

# A couple more notes
# %r prints raw formatter (used for debugging)
# %s prints string formatter the way we want user to see output