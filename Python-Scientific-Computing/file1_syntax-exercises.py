nam = input("Who are you? ")
print("Welcome", nam)

inp = input("Europe floor? ")
usf = int(inp) + 1
print("US floor:", usf)

# Who are you? Liliana
# Welcome Liliana
# Europe floor? 0
# US floor 1

# __________________________________________________________________

# ? Write a program to prompt the user for hours and rate per hours to compute gross pay.
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:", pay)

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25


# ? Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked about 40 hours.
strHours = input("Enter Hours: ")
strRate = input("Enter Rate: ")
try:
    floatHours = float(strHours)
    floatRate = float(strRate)
# print(floatHours, floatRate)
except:
    print("Error, please enter numeric input")
    quit()

if floatHours > 40:
    print("Overtime")
    regularPay = floatHours * floatRate
    extraPay = (floatHours - 40) * (1.5 * floatRate)
    print(regularPay, extraPay)
    pay = regularPay + extraPay
else:
    print("Regular")
    pay = floatHours * floatRate
print("Pay: ", pay)

# Log:
# Overtime
# 500.0 150.0
# Pay:  650.0

# __________________________________________________________________

# ? What will print out after running this code:
width = 15
height = 12.0
print(height / 3)

# 4.0

# __________________________________________________________________
# ? Conditional Steps:
x = 15

if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")
print("Finish")

# Finish

# __________________________________________________________________

y = 5
if y > 2:
    print("Bigger than 2")
    print("Still Bigger")
print("Done with 2")

for i in range(5):
    print(i)
    if i > 2:
        print("Bigger than 2")
    print("Done with i", i)
print("All Done")

# Log:

# Bigger than 2
# Still Bigger
# Done with 2
# 0
# Done with i 0
# 1
# Done with i 1
# 2
# Done with i 2
# 3
# Bigger than 2
# Done with i 3
# 4
# Bigger than 2
# Done with i 4
# All Done
# __________________________________________________________________

# ? Nested Decisions:
z = 42
if z > 1:
    print("More than one")
    if z < 100:
        print("Less than 100")
print("All done")

# Log:
# More than one
# Less than 100
# All done

# __________________________________________________________________

# ? Two-way decisions with else:

var1 = 4

if var1 > 2:
    print("Bigger")
else:
    print("Smaller")
print("All done")

# Log:
# Bigger
# All done
# __________________________________________________________________

# ? Multi-way (elif):

# Example 1:

var2 = 20

if var2 < 2:
    print("Small")
elif var2 < 10:
    print("Medium")
else:
    print("Large")
print("All done")

# Log:
# Large
# All done

# Example 2:
var3 = 160

if var3 < 2:
    print("Small")
elif var3 < 10:
    print("Medium")
elif var3 < 20:
    print("Big")
elif var3 < 40:
    print("Large")
elif var3 < 100:
    print("Huge")
else:
    print("Ginormous")

# Log:
# All done
# Ginormous

# __________________________________________________________________

# ? Try-Except:

# Example a:
astr = "Hello, Chuck"

try:
    istr = int(astr)
except:
    istr = -1

print("First: ", istr)

# Example b:
astr = "123"

try:
    istr = int(astr)
except:
    istr = -1

print("Second: ", istr)

# Log:
# First:  -1
# Second:  123

# Example c:
rawstr = input("Enter a positive number: ")
try:
    ivalue = int(rawstr)
except:
    ivalue = -1

if ivalue > 0:
    print("Nice work")
else:
    print("Not a positive number")

# Enter a number: 42
# Nice work

# Enter a number: forty-two
# Not a positive number
