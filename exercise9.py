# fun with days and months
days = "Mon Tue wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print the strings with variables
print ("Here are the days: ", days)
print ("Here are the months: ", months)

# prints the months as previously
test_string = "Here are the months %s"
print(test_string % months)

# prints the raw string as stored in var months
test_string_two = "Here are the months %r"
print(test_string_two % months)

# prints many lines as one string
print ("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")