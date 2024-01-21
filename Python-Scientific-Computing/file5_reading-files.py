# Files as a Sequence:

# ? Counting lines in a file:
file_handler = open("mbox.txt")
count = 0
for line in file_handler:
    count += 1
print("Line Count:", count)  # Output: Line Count: 4

# ? Reading the hole file:
# * We can read the whole file (newlines and all) into a single string:
file_handler = open("mbox.txt")
inp = file_handler.read()
print(len(inp))  # Output: 236
print(inp[:20])  # De: Financial Aid <f

# ? Searching through a file:
file_handler = open("mbox.txt")
for line in file_handler:
    line = line.rstrip()
    if line.startswith("De:"):
        print(line)  # De: Financial Aid <financial.aid@uopeople.edu>

# ? Skipping with continue: Another way to do the same.
file_handler = open("mbox.txt")
for line in file_handler:
    if not line.startswith("De:"):
        continue
    print(line)  # De: Financial Aid <financial.aid@uopeople.edu>

# ? Using 'in' to select lines:
file_handler = open("mbox.txt")
for line in file_handler:
    line = line.rstrip()
    if not "milanoliliana129@gmail.com" in line:
        continue
    print(line)  # To: Liliana Milano Rivas <milanoliliana129@gmail.com>

# ? Prompt for file name:
file_name = input("Enter the file name: ")
file_handler = open(file_name)
count = 0
for line in file_handler:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", file_name)

# Enter the file name: mbox.txt
# There were 1 subject lines in mbox.txt

# ? Bad file names:
file_name = input("Enter the file name: ")
try:
    file_handler = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()

count = 0
for line in file_handler:
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", file_name)

# Output:
# Enter the file name: mbox.txt
# There were 1 subject lines in mbox.txt
# Enter the file name: mbox,txt
# File cannot be opened: mbox,txt

# ? Exercise: Write a program to read through a file and print the contents of the file (line by line) all in upper case.

file_handler = open("mbox.txt")
# print(file_handler)  # Output: <_io.TextIOWrapper name='mbox.txt' mode='r' encoding='cp1252'>

for line in file_handler:
    line = line.rstrip()
    print(line.upper())
# Output:
# DE: FINANCIAL AID <FINANCIAL.AID@UOPEOPLE.EDU>
# DATE: VIE, 19 ENE 2024 A LA(S) 1:51Â€¯A.M.
# SUBJECT: YOUR SCHOLARSHIP HAS NOW BEEN ALLOCATED TO (UNIV 1001ONLINE # EDUCATION STRATEGIES )!
# TO: LILIANA MILANO RIVAS <MILANOLILIANA129@GMAIL.COM>
