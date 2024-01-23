# Data Structures:
# ? Lists:

print([1, 24, 76])  # [1, 24, 76]

print(["red", "yellow", "blue"])  # ['red', 'yellow', 'blue']

print(["red", 24, 98.6])  # ['red', 24, 98.6]

print([1, [5, 6], 7])  # [1, [5, 6], 7]

print([])  # []

# __________________________________________________________________________

for i in [5, 4, 3, 2, 1]:
    print(i)
print("Blastoff!")
# Output:
# 5
# 4
# 3
# 2
# 1
# Blastoff!

friends = ["Joseph", "Glenn", "Sally"]
for friend in friends:
    print("Happy New Year 2024:", friend)
print("Done!")
# Output:
# Happy New Year 2024: Joseph
# Happy New Year 2024: Glenn
# Happy New Year 2024: Sally
# Done!

# ? Looking inside lists.
# * Just like strings, we can get at any single element in a list using an index specified in square brackets.

friends = ["Joseph", "Glenn", "Sally"]
print(friends[1])  # Glenn

# * Lists are mutable:
# * Strings are " immutable"- we cannot change the contents of a string - we must make a new string to make any change.

fruit = "Banana"
# fruit[0] = 'b'
# Traceback (most recent call last):
# TypeError: 'str' object does not support item assignment

# Way to go: make a new string to make any change (x)
x = fruit.lower()
print(x)  # banana

# * Lists are "mutable"- we can change an element of a list using the index operator:
lotto = [2, 14, 26, 41, 63]
print(lotto)  # [2, 14, 26, 41, 63]

lotto[2] = 28
print(lotto)  # [2, 14, 28, 41, 63]

# ? How long is a list?
greet = "Hello Bob"
print(len(greet))  # 9 (for strings)

x = [1, 2, "joe", 99]
print(len(x))  # 4 (number of elements in the list)

# ? Using the range function:
print(range(4))  # range(0, 4)
print(list(range(4)))  # [0, 1, 2, 3]

friends = ["Joseph", "Glenn", "Sally"]
print(len(friends))  # 3
print(range(len(friends)))  # range(0, 3)
print(list(range(len(friends))))  # [0, 1, 2]

for i in range(len(friends)):
    friend = friends[i]
    print("Happy New Year:", friend)
# Happy New Year: Joseph
# Happy New Year: Glenn
# Happy New Year: Sally

# ? Concatenating lists using +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b

print(c)  # [1, 2, 3, 4, 5, 6]
print(a)  # [1, 2, 3]

# ? Lists can be sliced using:
# * Just like in strings, the second number is "up to but not including"
t = [9, 41, 12, 3, 74, 15]

print(t[1:3])  # [41, 12]
print(t[:4])  # [9, 41, 12, 3]
print(t[3:])  # [3, 74, 15]
print(t[:])  # [9, 41, 12, 3, 74, 15]

# ? Lists Methods:
x = list()
print(type(x))  # <class 'list'>

print(dir(x))

# * ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# https://docs.python.org/3/tutorial/datastructures.html

# ? Building a list from scratch (append method):
# * We can create an empty list and then add elements using the append method.
# * The list stays in order and new elements are added at the end of the list.

stuff = list()
stuff.append("book")
stuff.append(99)
print(stuff)  # ['book', 99]
stuff.append("cookie")
print(stuff)  # ['book', 99, 'cookie']

# ? Is something in a List? (in - not in):
# * Logical Operators that return True or False. Do not modify the list.
some = [1, 9, 21, 10, 16]
print(9 in some)  # True
print(15 in some)  # False
print(20 not in some)  # True

# ? Lists are in order:
# * A list can be sorted (i.e., change its order). The sort method (unlike in strings) means "sort yourself."
friends = ["Joseph", "Glenn", "Sally"]
friends.sort()
print(friends)  # ['Glenn', 'Joseph', 'Sally']
print(friends[1])  # Joseph

# ? Built-in Functions and Lists:
nums = [3, 41, 12, 9, 74, 15]

print(len(nums))  # 6

print(max(nums))  # 74

print(min(nums))  # 3

print(sum(nums))  # 154

print(sum(nums) / len(nums))  # 25.666666666666668

# ? Exercise:
# * Average using counter and accumulator:
accumulator = 0
counter = 0

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    accumulator += value
    counter += 1
average = accumulator / counter
print("Average:", average)

# Output:
# Enter a number: 3
# Enter a number: 9
# Enter a number: 5
# Enter a number: done
# Average: 5.666666666666667

# * Average using built-in methods and lists: require more memory but the result is the same.

numlist = list()

while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print("Average:", average)

# Output:
# Enter a number: 3
# Enter a number: 9
# Enter a number: 5
# Enter a number: done
# Average: 5.666666666666667

# __________________________________________________________________________

# ? Best friends: Strings and Lists
# * Split() breaks a string into parts and produces a list of strings. We think of these as words. We can access a particular word or loop through all the words.

abc = "With three words"

stuff = abc.split()

print(stuff)  # ['With', 'three', 'words']
print(len(stuff))  # 3
print(stuff[0])  # With

for word in stuff:
    print(word)
# Output:
# With
# three
# words
# __________________________________________________________________________

# * When you do not specify a delimiter, multiple spaces are treated like one delimiter:

line = "A lot                of spaces"
temp = line.split()
print(temp)  # ['A', 'lot', 'of', 'spaces']

# * You can specify what delimiter character to use in the splitting:

line = "first;second;third"
thing = line.split()
print(thing)  # ['first;second;third']
print(len(thing))  # 1

thing = line.split(";")
print(thing)  # ['first', 'second', 'third']
print(len(thing))  # 3

# __________________________________________________________________________
fhand = open("mbox.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith("De: "):
        continue
    words = line.split()
    print(words[2])  # Aid

line = "De: Financial Aid <financial.aid@uopeople.edu>"
words = line.split()
print(words)  # ['De:', 'Financial', 'Aid', '<financial.aid@uopeople.edu>']

# ? The Double split pattern:
# * Sometimes we split a line one way, and then grab one of the pieces of the line and split that piece again:

words = line.split()
email = words[3]
print(email)  # <financial.aid@uopeople.edu>
pieces = email.split("@")
print(pieces[1][:-1])  # uopeople.edu

# * Note: The [:-1] notation specifies that you want to slice the string from the beginning to the second-to-last character, effectively removing the final character ">".

# _____________________________________________________________________
# ? Exercise:
# * Python Guardian Pattern: The guardian pattern is a technique used in Python to ensure that certain conditions are met before executing a block of code. It is often used to handle cases where unexpected data or errors may occur. The guardian pattern helps to make the code more robust and prevents potential errors or crashes.

# ? Way 1

file_handler = open("mbox.txt")

for line in file_handler:
    line = line.rstrip()
    words = line.split()

    # guardian a bit stronger:
    if len(words) < 3:
        continue

    if words[0] != "De:":
        continue
    print(words[3][1:-1])  # * financial.aid@uopeople.edu

    # * [1:-1] get rid of "<" and ">" symbols.

# ? Exercise: Way 2

file_handler = open("mbox.txt")

for line in file_handler:
    line = line.rstrip()
    words = line.split()

    # Guardian in a compound statement:
    if len(words) < 3 or words[0] != "De:":
        continue
    print(words[3][1:-1])  # * financial.aid@uopeople.edu

# ? Exercise: Way 3
# * You can replace the guardian pattern in your code with a try-except block. The try-except block is a common approach in Python for handling exceptions and can be used to achieve similar functionality as the guardian pattern.

file_handler = open("mbox.txt")

for line in file_handler:
    line = line.rstrip()
    words = line.split()

    # * try-except block:
    try:
        if len(words) < 3:
            raise IndexError  # Raise an exception if the condition is not met
        if words[0] != "De:":
            raise ValueError  # Raise an exception if the condition is not met
        print(words[3][1:-1])  # * financial.aid@uopeople.edu
    except (IndexError, ValueError):
        continue

# TODO: In summary, while both the guardian pattern and the try-catch block can be used effectively, the try-catch block is generally recommended for exception handling due to its clearer structure and better code readability. It is important to consider the specific requirements and context of your code when deciding which approach to use.
