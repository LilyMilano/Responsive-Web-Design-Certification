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

#? Write a program to prompt the user for hours and rate per hours to compute gross pay.
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")
pay = float(hours) * float(rate)
print("Pay:", pay)

# Enter Hours: 35
# Enter Rate: 2.75
# Pay: 96.25

# __________________________________________________________________

#? What will print out after running this code:
width = 15
height = 12.0
print(height / 3)

# 4.0

# __________________________________________________________________
#? Conditional Steps:
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

#? Nested Decisions:
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

#? Two-way decisions with else:

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

#? Multi-way (elif):

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

#? Try-Except:
