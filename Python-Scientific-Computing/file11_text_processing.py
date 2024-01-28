import urllib.request, urllib.parse, urllib.error

# Representing Simple Strings
# * Each character is represented by a number between 0 and 256 stored in 8 bits of memory (1 byte).
# * The ord() function tells us the numeric value of a simple ASCII character.

print(ord("H"))  # 72
print(ord("h"))  # 104
print(ord("ñ"))  # 241
print(ord("E"))  # 69
print(ord("e"))  # 101
print(ord("\n"))  # 10

# In Python 3:
x = b"abc"
print(type(x))  # <class 'bytes'>

x = "こんにちは"  # hello in japanese
print(type(x))  # <class 'str'>

x = "こんにちは"  # hello in japanese: konnichiwa (unicode)
print(type(x))  # <class 'str'>

# __________________________________________________________________________
# ? Networking: Using urllib in Python. Like a file...
fhand = urllib.request.urlopen("https://data.pr4e.org/romeo.txt")
for line in fhand:
    print(line.decode().strip())  # show data without headers
    """
    But soft what light through yonder window breaks
    It is the east and Juliet is the sun
    Arise fair sun and kill the envious moon
    Who is already sick and pale with grief
    """
# __________________________________________________________________________
fhand = urllib.request.urlopen("https://data.pr4e.org/romeo.txt")

counts = dict()
for line in fhand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
# {'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1, 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3, 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2, 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1, 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1, 'grief': 1}

# __________________________________________________________________________

fhand = urllib.request.urlopen("http://www.dr-chuck.com/page1.htm")
for line in fhand:
    print(line.decode().strip())

    """
    <h1>The First Page</h1>
    <p>
    If you like, you can switch to the
    <a href="http://www.dr-chuck.com/page2.htm">
    Second Page</a>.
    </p>
    """
