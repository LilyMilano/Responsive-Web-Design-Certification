import re

# ? Using re.search() like find():

hand = open("mbox.txt")
for line in hand:
    line = line.rstrip()
    if re.search("De:", line):
        print(line)  # De: Financial Aid <financial.aid@uopeople.edu>

# ? Using re.search() like startswith():

hand = open("mbox.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^De:", line):
        print(line)  # De: Financial Aid <financial.aid@uopeople.edu>

# ? Warning:Greedy Matching:

# * re.search() returns a True/False depending on whether the string matches the regular expression.

# * If we actually want to matching strings to be extracted, we use re.findall()

x = "My 2 favorite numbers are 19 and 42"
y = re.findall("[0-9]+", x)
print(y)  # * ['2', '19', '42']

y = re.findall("[AEIOU]+", x)
print(y)  # * []

# * The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string.
x = "From: Using the : character"
y = re.findall("^F.+:", x)
print(y)  # * ['From: Using the :']

# ? Non-Greedy Matching:
# * Not all regular expression repeat codes are greedy!
# * If you add a ? character, the + and * chill out a bit.
x = "From: Using the : character"
y = re.findall("^F.+?:", x)
print(y)  # * ['From:']

# ? Fine-Tuning String Extraction:
# * You can refine the match for re.findall() and separately determine which portion of the match is to be extracted by using parentheses.

x = "From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

y = re.findall(r"\S+@\S+", x)
print(y)  # * ['stephen.marquard@uct.ac.za']

# * Parentheses are not part of the match - but they tell where to start and stop what string to extract

x = "From: stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

y = re.findall(r"^From: (\S+@\S+)", x)
print(y)  # * ['stephen.marquard@uct.ac.za']

# ? Example:
s = "A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM"
lst = re.findall("\\S+@\\S+", s)
print(lst)  # * ['csev@umich.edu', 'cwen@iupui.edu']

# \\S+ will match any sequence of characters that does not contain whitespace. This is in contrast to the lowercase s (\\s), which matches a single whitespace character, such as a space or a tab.

# ? Regular Expressions: Practical Applications:

# ? Extracting a host name - using find and string slicing:
data = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"

atposition = data.find("@")
print(atposition)  # * 21

space_position = data.find(" ", atposition)
print(space_position)  # * 31

host = data[atposition + 1 : space_position]
print(host)  # * uct.ac.za

# * The Double Split Pattern:

words = data.split()
email = words[1]
pieces = email.split("@")
print(pieces[1])  # * uct.ac.za
# _________________________________________________________________________

# * RegEx 1:
line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("@([^ ]*)", line)
print(y)  # *  ['uct.ac.za']

# * Even cooler Regex version:
line = "From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
y = re.findall("^From .*@([^ ]*)", line)
print(y)  # * ['uct.ac.za']
# _________________________________________________________________________

# * Working with files:
hand = open("mbox-short.txt")
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(stuff) != 1:
        continue
    num = float(stuff[0])
    numlist.append(num)
print("Maximum:", max(numlist))  # * Maximum: 0.9907

# ? Escape Character: _____________________________________________________
# * If you want a special regular expression character to just behave normally (most of the time) you prefix it with '\'

x = "We just received $10.00 for cookies."
y = re.findall(r"\$[0-9.]+", x)
print(y)  # * ['$10.00']
