x = 1
print(x)

x = x + 1
print(x)

x = x + 2
print(x)

# Conditional Steps___________________________________________________

x = 5

if x < 10:
    print("Smaller")
if x > 20:
    print("Bigger")

print("Finish")

# Loops_______________________________________________________________

n = 5
while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")

# 5
# 4
# 3
# 2
# 1
# Blastoff!

# Chapter II: Variables, Expressions, and Statements___________________

hours = 35.0
rate = 12.5
pay = hours * rate
print(pay)  # log: 437.5

xx = 2
xx = xx + 2
print(xx)  # log:4

yy = 440 * 12
print(yy)  # log: 5280

zz = yy / 1000
print(zz)  # log: 5.28

jj = 23
kk = jj % 5
print(kk)  # log: 3

x = 1 + 2**3 / 4 * 5
print(x)  #  log: 11.0

eee = "hello " + "there"
print(eee)

print(float(99) + 100)  # 199.0

i = 42
print(type(i))  # <class 'int'>
f = float(i)
print(type(f))  # <class 'float'>

# Strig conversions

sval = "123"
print(type(sval))  # <class 'str'>
ival = int(sval)
print(type(ival))  # <class 'int'>
print(ival + 1)  # 124

# User input:
nam = input("Who are you? ")
print("Welcome,", nam)  # Welcome, Liliana

# Converting user input:
inp = input("Europe floor?")
usf = int(inp) + 1
print("US floor", usf)  # US floor 1

# Exercise 1:
hours = input('Enter Hours: ')  # 2
rate = input('Enter Rate: ')    # 10
pay = float(hours) * float(rate)
print('Pay:', pay)  # Pay: 20.0
