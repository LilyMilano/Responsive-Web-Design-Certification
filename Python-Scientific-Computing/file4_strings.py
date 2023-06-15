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

#...................................................

for n in 'banana':
    print(n)
    
# Output:
# b
# a
# n
# a
# n
# a

# ? Intermediate Strings: