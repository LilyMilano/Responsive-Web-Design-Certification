# What is the purpose of the "def" keyword in Python?
# It indicates the start of a function, and the following indented section of code is to be stored for later.


def thing():
    print("Hello")
    print("Fun")


thing()
print("Zip")
thing()

# Log:
# Hello
# Fun
# Zip
# Hello
# Fun
# __________________________________________________________________

# Built-in functions max() and min():
big = max("Hello world")
print(big)
# Log: w

tiny = min("Hello world")
print(tiny)
# Log: ' '
# __________________________________________________________________
# Type Conversions:

print(float(99) / 100)
# 0.99
i = 42
print(type(i))
# Log: <class 'int'>
f = float(i)
print(f)
# Log: 42.0
type(f)
print(type(f))
# Log: <class 'float'>
print(1 + 2 * float(3) / 4 - 5)
# Log: -2.5

# __________________________________________________________________
# Building Own Functions: (not invoking)
x = 5
print("Hello")


def print_lyrics():
    print("I am a lumberjack, and I am okay.")
    print("I sleep all night, and I work all day.")


print("Yo")
x = x + 2
print(x)
