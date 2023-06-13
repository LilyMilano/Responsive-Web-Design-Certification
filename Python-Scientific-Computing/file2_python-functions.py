# **
# ? purpose of the "def" keyword in Python: It indicates the start of a function, and the following indented section of code is to be stored for later.


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
# ? Built-in functions max() and min():

big = max("Hello world")
print(big)
# Log: w

tiny = min("Hello world")
print(tiny)
# Log: ' '
# __________________________________________________________________
# ? Type Conversions:

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
# ? Building Own Functions: (not invoking)
x = 5
print("Hello")


def print_lyrics():  # Defining the function
    print("I am a lumberjack, and I am okay.")
    print("I sleep all night, and I work all day.")


# This function is NOT going to be printed, because is NOT being invoking, just defining.


print("Yo")
x = x + 2
print(x)

# Log:
# Hello
# Yo
# 7
# __________________________________________________________________
# ? Invoking a function:
x = 5
print("Hello")


def print_lyrics():
    print("I am a lumberjack, and I am okay.")
    print("I sleep all night, and I work all day.")


print("Yo")
print_lyrics()  # Invoking the function
x = x + 2
print(x)

# Log:
# Hello
# Yo
# I am a lumberjack, and I am okay.
# I sleep all night, and I work all day.
# 7
# __________________________________________________________________
# ? Invoking with Parameters:


def greet(lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")


greet("en")  # Hello
greet("es")  # Hola
greet("fr")  # Bonjour
# __________________________________________________________________
# ? Return Value:


def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"


print(greet("en"), "Glenn")  # Hello Glenn
print(greet("es"), "Sally")  # Hola Sally
print(greet("fr"), "Lily")  # Bonjour Lily

# __________________________________________________________________
# ? Multiple Parameters / Arguments:


def addtwo(a, b):
    added = a + b
    return added


x = addtwo(3, 5)
print(x)  # Log: 8

# __________________________________________________________________
# ? Write a pay computation function to give an employee 1.5 times the hourly rate for hours worked about 40 hours.


def computepay(hours, rate):  # Hasn't been invoked yet
    # print("In computepay", hours, rate)
    if hours > 40:
        regular = rate * hours
        overtime_pay = (hours - 40) * (0.5 * rate)
        pay = regular + overtime_pay
    else:
        pay = rate * hours
    # print("Returning", pay)
    return pay


# Asking for the data:
strh = input("Enter Hours: ")
strr = input("Enter Rate: ")
fh = float(strh)
fr = float(strr)

overtime_total_pay = computepay(fh, fr)
print("Pay: ", overtime_total_pay)

# Log:
# Enter Hours: 50
# Enter Rate: 10
# In computepay 50.0 10.0
# Returning 550.0
# Pay:  550.0
