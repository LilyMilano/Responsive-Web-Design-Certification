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
x = 0

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
# * To add up a value we encounter in a loop, we introduce an accumulator variable that starts at 0 and we add the value to the sum each time through the loop.

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
