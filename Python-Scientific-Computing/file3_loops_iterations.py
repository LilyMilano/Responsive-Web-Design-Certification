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