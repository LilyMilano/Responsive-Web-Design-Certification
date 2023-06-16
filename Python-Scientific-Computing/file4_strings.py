# Looking inside Strings:
fruit = "banana"
letter = fruit[1]
print(letter)
# a
x = 3
w = fruit[x - 1]
print(w)
# n

# ? Strings Length:
# len() -> length of the string
# len() - 1 = position of the last index
fruit = "banana"
print(len(fruit))
# length: 6
# positions: 6 - 1

# ? Looping through Strings:
# * Using a While statement and an iteration variable, and the len() function, we can construct a loop to look at each of the letters in a string individually..

fruit = "banana"
index = 0

while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

# Output:
# 0 b
# 1 a
# 2 n
# 3 a
# 4 n
# 5 a

# * A definite loop using for statement is much more elegant. The iteration variable is completely taken care of by the 'for' loop:

fruit = "banana"
for letter in fruit:
    print(letter)

# Output:
# b
# a
# n
# a
# n
# a

# ? Looping and counting an specific letter:

word = "banana"
count = 0
for letter in word:
    if letter == "a":
        count += 1
print(count)

# Output:
# 3

# ...................................................

for n in "banana":
    print(n)

# Output:
# b
# a
# n
# a
# n
# a

# TODO Intermediate Strings:

# ? Slicing Strings:

str = "Monty Python"

print(str[0:4])
# str sub zero through four: start at position zero and then go up through, but not including four.
# Output: Mont
print(str[6:7])
# Output: P
print(str[6:20])
# Output: Python (if the second number is beyond the end of the string, it stops at the end.)

# * If we leave off the first number or the last number of the slice. it is assumed to be the beginning or end of the string respectively:

str = "Monty Python"
print(str[:2])
# Output: Mo
print(str[8:])
# Output: thon
print(str[:])
# Output: Monty Python

# ? String Concatenation:
a = "hello"
b = a + "there"
print(b)
# Output: hellothere
c = a + " " + "there"
print(c)
# Output: hello there

# ? Using 'in' as a logical operator:
# * The 'in' keyword can also be used to check to see is one string is in another string.

fruit = "banana"

if "n" in fruit:
    print("Found it!")
else:
    print("Not found it!")
# Output: Found it!
# .................................................................

if "m" in fruit:
    print("Found it!")
else:
    print("Not found it!")
# Output: Not found it!
# .................................................................

if "nan" in fruit:
    print("Found it!")
else:
    print("Not found it!")
# Output: Found it!
# .................................................................

if "a" in fruit:
    print("Found it!")
else:
    print("Not found it!")
# Output: Found it!

# .................................................................

# ? String Comparison (lexicographically):
word = input("> What is your favorite fruit? ")
if word == "banana":
    print("All right, bananas.")
if word < "banana":
    print("Your word," + word + ", comes before banana.")
elif word > "banana":
    print("Your word, " + word + ", comes after banana.")
else:
    print("All right, bananas.")

# Output:
# > What is your favorite fruit? coconut
# Your word, coconut, comes after banana.

# > What is your favorite fruit? BANANA
# Your word,BANANA, comes before banana.

# > What is your favorite fruit? banana
# All right, bananas.
# All right, bananas.

# .................................................................

# ? String Library:
# https://www.w3schools.com/python/python_ref_string.asp
# ? functions do not modify the original string. The return a new altered string (zap).

# ? lower()

greet = "Hello Bob"
zap = greet.lower()
print(zap)
# Output:
# hello bob

print(greet)  # Not altered
# Output:
# Hello Bob

print("Hi There".lower())
# Output:
# hi there

# .................................................................
stuff = "Hello world"
print(type(stuff))

# Output:
# <class 'str'>

# .................................................................
print(dir(stuff))
# https://docs.python.org/3/library/stdtypes.html#string-methods


# * ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# .................................................................

# ? find(): We use .find() function to search for a substring within another string.
# ? find() finds the first occurrence of the substring.
# ? If the substring is not found find() returns -1
# ? Remember that string positions starts at zero.

fruit = "banana"
position = fruit.find("na")
print(position)
# * Output : 2

pos = fruit.find("z")
print(pos)
# * Output : -1

# .................................................................

# ? UPPER CASE:

greet = "Hello Bob"
greet_upper = greet.upper()
print(greet_upper)
# Output: HELLO BOB

greet_lower = greet.lower()
print(greet_lower)
# Output: hello bob

# .................................................................

# ? Search and replace:
# * replace() is like a "search and replace" operation.
# * It replaces ->> all concurrences <<- of the search string with the replacement string.

greet = "Hello Bob"
greet_replace = greet.replace("Bob", "Jane")
print(greet_replace)
# Output:Hello Jane

greet_replace = greet.replace("o", "X")
print(greet_replace)
# Output: HellX BXb

# .................................................................

# ? Stripping Whitespace:
# ? Take a string and remove whitespace at the beginning and/or end

# * lstrip() and rstrip() >> Remove whitespace at the left or right.
# * strip() >> Removes both beginning and ending whitespace

greet = "   Hello Bob  "
zaz = greet.rstrip()
print("rstrip: ", zaz)
# Output: rstrip:     Hello Bob

zaz = greet.lstrip()
print("lstrip: ", zaz)
# Output: lstrip:  Hello Bob

zaz = greet.strip()
print("strip: ", zaz)
# Output: lstrip:  Hello Bob

# .................................................................

# ? Prefixes:
# * startswith()

line = "Please have a nice day"

if line.startswith("Please"):
    print(True)
elif line.startswith("p"):
    print(False)
else:
    print("Invalid input")
# Output: True

# .................................................................

# ? Parsing and Extracting:

data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
# * Extracting email host: 'uct.ac.za' (from data)
atposition = data.find("@")
print(atposition)  # * 21
space_position = data.find(" ", atposition)
print(space_position)  # * 31
host = data[atposition + 1 : space_position]
print(host)
# * Output:
# * uct.ac.za
# .................................................................

# ? Exercise  6.5: Take the following Python code that stores a string:

# ? string = 'X-DSPAM-Confidence: 0.8475'

# ? Use find and string slicing to extract the portion of the string after the colon character and then use the float function to convert the extraced string into a floating number.

str = "X-DSPAM-Confidence: 0.8475"
print(str)  # X-DSPAM-Confidence: 0.8475
colon_position = str.find(":")
print(colon_position)  # * 18
piece = str[18 + 2 :]
print(piece)  # * 0.8475
print(type(piece))  # * <class 'str'>
value = float(piece)
print(value)  # * 0.8475
print(type(value))  # * <class 'float'> 
