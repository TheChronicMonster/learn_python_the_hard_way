formatter = "%r %r %r %r"
print (formatter % (1, 2, 3, 4)) # prints the numerals
print (formatter % ("one", "two", "three", "four")) # prints the written numbers
print (formatter % (True, False, False, True)) # prints booleans
# prints for sets fo the formatter
print (formatter % (formatter, formatter, formatter, formatter))
# prints the following string on one line
print (formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
))