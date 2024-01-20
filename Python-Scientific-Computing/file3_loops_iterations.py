# Example: While loop

n = 5

while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")
print(n)

# Output:
# 5
# 4
# 3
# 2
# 1
# Blastoff!
# 0
# __________________________________________________________________
# ? Breaking Out a Loop:
# https://www.w3schools.in/python/break-and-continue

# ? break:

while True:
    line = input("> ")
    if line == "done":
        break
    print(line)
print("Done!")

# Output:
# > hello there
# hello there
# > finished
# finished
# > done
# Done!

# ________________________________________________________________
n = 0

while True:
    if n == 3:
        break
    print(n)
    n = n + 1

# Output:
# 0
# 1
# 2

# ________________________________________________________________
count = 0

while count <= 100:
    print(count)
    count += 1
    if count == 3:
        break

# Output:
# 0
# 1
# 2

# _______________________________________________________________

# ? continue:

while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")

# Output:
# > #hello
# #hello
# > #hi
# #hi
# > done
# Done!

# _______________________________________________________________
# ? Definite Loops:

for i in range(0, 5):
    if i == 3:
        continue
    print(i)

# Output:
# 0
# 1
# 2
# 4

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
    print("Happy New Year:", friend)
print("Done!")

# Output:
# Happy New Year: Joseph
# Happy New Year: Glenn
# Happy New Year: Sally
# Done!

for i in [2, 1, 5]:
    print(i)

# Output:
# 2
# 1
# 5

# ? Loop Idioms: Finding the largest value

largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15]:
    if the_num > largest_so_far:
        largest_so_far = the_num
    print(largest_so_far, the_num)
print("After", largest_so_far)

# Output:
# Before -1
# 9 9
# 41 41
# 41 12
# 41 3
# 74 74
# 74 15
# After 74

# ? Finding the smallest value:

smallest = None
print("Before:", smallest)
for iterval in [3, 2, 12, 9, 74, 1]:
    if smallest is None or iterval < smallest:
        smallest = iterval
    print("Loop:", iterval, smallest)
print("Smallest:", smallest)

# Output:
# Before: None
# Loop: 3 3
# Loop: 2 2
# Loop: 12 2
# Loop: 9 2
# Loop: 74 2
# Loop: 1 1
# Smallest: 1

smallest = None
print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print("After", smallest)

# ? Counting a loop:

# * To count how many times we execute a loop, we introduce a counter variable that starts at 0 and we add one to it each time through the loop.

counter = 0
print("Before:", counter)
for element in [9, 41, 12, 3, 74, 15]:
    counter += 1
    print(counter, element)
print("After:", counter)

# Output:
# Before: 0
# 1 9
# 2 41
# 3 12
# 4 3
# 5 74
# 6 15
# After: 6

# ? Summing in a loop:
# * To add up a value we encounter in a loop, we introduce an accumulator variable (sum) that starts at 0 and we add the value to the sum each time through the loop.

accumulator = 0
print("Before:", accumulator)
for thing in [9, 41, 12, 3, 74, 15]:
    accumulator = accumulator + thing
    print(accumulator, thing)
print("After:", accumulator)

# # Output:
# Before: 0
# 9 9
# 50 41
# 62 12
# 65 3
# 139 74
# 154 15
# After: 154

# ? Finding the average in a loop:
# * An average just combines the counting and sum patterns and divided when the loop is done.

count = 0
sum = 0
print("Before:", count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count += 1
    sum += value
    print(count, sum, value)
print("After:", count, sum, (sum / count))

# Output:
# Before: 0 0
# 1 9 9
# 2 50 41
# 3 62 12
# 4 65 3
# 5 139 74
# 6 154 15
# After: 6 154 25.666666666666668

# ? Filtering in a loop:
# * We use an 'if' statement in the loop to catch/filter the values we are looking for.

print("Before")
for value in [9, 41, 12, 3, 74, 15]:
    if value > 20:
        print("Large number", value)
print("After")

# Output:
# Before
# Large number 41
# Large number 74
# After

# ? Search Using a Boolean Variable:
# * If we just want to search and know if a value was found, we use a variable that starts at 'False' and is set to True as soon as we find what we are looking for.

found = False
print("Before:", found)
for value in [9, 41, 12, 3, 74, 15]:
    if value == 3:
        found = True
    print(found, value)
print("After:", found)

# Output:
# Before: False
# False 9
# False 41
# False 12
# True 3
# True 74
# True 15
# After: True

# ? Review exercise:
# * Write a program which repeatedly reads numbers until user enters 'done'. Once 'done' is entered, print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake using 'try' and 'except' and print and error message and skip to the next number.

count = 0
accum = 0.0
while True:
    str_value = input("Enter a number: ")
    if str_value == "done":
        break
    try:
        f_value = float(str_value)
    except:
        print("Invalid input")
        continue
    # print(f_value)
    count += 1
    accum += f_value
# print("ALL DONE")
print(count, accum, accum / count)

# Output:
# Enter a number: li
# Invalid input
# Enter a number: 15
# Enter a number: 15
# Enter a number: 15
# Enter a number: 15
# Enter a number: done
# 4 60.0 15.0
