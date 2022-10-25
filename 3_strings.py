#This is a python script to demonstrate strings

#This is a string
#Strings are used to store text
myString = "Hello World"

#Strings are arrays
#Get the character at position 1
print(myString[1])

#Substring
#Get the characters from position 2 to position 5 (not included)
print(myString[2:5])

#The strip() method removes any whitespace from the beginning or the end
print(myString.strip())

#The len() method returns the length of a string
print(len(myString))

#The lower() method returns the string in lower case
print(myString.lower())

#The upper() method returns the string in upper case
print(myString.upper())

#The replace() method replaces a string with another string
print(myString.replace("H", "J"))

#The split() method splits the string into substrings if it finds instances of the separator
#Default separator is any whitespace
print(myString.split(" "))

#Check if the phrase "Hello" is present in the following text
txt = "The rain in Spain stays mainly in the plain"
x = "Hello" in txt
print(x)

#Check if the phrase "ain" is NOT present in the following text
x = "ain" not in txt
print(x)

#String concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

#String format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

#Escape character
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


#String methods

#capitalize()	Converts the first character to upper case
#casefold()	Converts string into lower case
#center()	Returns a centered string
#count()	Returns the number of times a specified value occurs in a string
#encode()	Returns an encoded version of the string
#endswith()	Returns true if the string ends with the specified value
#expandtabs()	Sets the tab size of the string
#find()	Searches the string for a specified value and returns the position of where it was found
#format()	Formats specified values in a string
#format_map()	Formats specified values in a string
#index()	Searches the string for a specified value and returns the position of where it was found
#isalnum()	Returns True if all characters in the string are alphanumeric
#isalpha()	Returns True if all characters in the string are in the alphabet
#isdecimal()	Returns True if all characters in the string are decimals
#isdigit()	Returns True if all characters in the string are digits
#isidentifier()	Returns True if the string is an identifier
#islower()	Returns True if all characters in the string are lower case
#isnumeric()	Returns True if all characters in the string are numeric
#isprintable()	Returns True if all characters in the string are printable
#isspace()	Returns True if all characters in the string are whitespaces
#istitle()	Returns True if the string follows the rules of a title
#isupper()	Returns True if all characters in the string are upper case
#join()	Joins the elements of an iterable to the end of the string
#ljust()	Returns a left justified version of the string
#lower()	Converts a string into lower case
#lstrip()	Returns a left trim version of the string
#maketrans()	Returns a translation table to be used in translations
#partition()	Returns a tuple where the string is parted into three parts
#replace()	Returns a string where a specified value is replaced with a specified value
#rfind()	Searches the string for a specified value and returns the last position of where it was found
#rindex()	Searches the string for a specified value and returns the last position of where it was found
#rjust()	Returns a right justified version of the string
#rpartition()	Returns a tuple where the string is parted into three parts
#rsplit()	Splits the string at the specified separator, and returns a list
#rstrip()	Returns a right trim version of the string
#split()	Splits the string at the specified separator, and returns a list
#splitlines()	Splits the string at line breaks and returns a list
#startswith()	Returns true if the string starts with the specified value
#strip()	Returns a trimmed version of the string
#swapcase()	Swaps cases, lower case becomes upper case and vice versa
#title()	Converts the first character of each word to upper case
#translate()	Returns a translated string
#upper()	Converts a string into upper case
#zfill()	Fills the string with a specified number of 0 values at the beginning

