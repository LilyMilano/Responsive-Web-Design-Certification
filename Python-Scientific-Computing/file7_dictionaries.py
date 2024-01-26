# Dictionaries
# ? Dictionaries Vs Lists:
# * Lists index their entries based on the position in the list.
# * Dictionaries are like bags - no order.
# * So we index the things we put in the dictionary with a "lookup tag"

purse = dict()

purse["money"] = 12
purse["candy"] = 3
purse["tissues"] = 75

print(purse)  # * Output: {'money': 12, 'candy': 3, 'tissues': 75}
print(purse["candy"])  # * Output: 3

purse["candy"] = purse["candy"] + 2

print(purse)  # * Output: {'money': 12, 'candy': 5, 'tissues': 75}

# ? Dictionary literals:
# * Use curly braces and have a list of key:value pairs.
# * You can make an empty dictionary using empty curly braces (no need to ddd = dict())

jjj = {"chuck": 1, "fred": 42, "jane": 100}
print(jjj)  # {'chuck': 1, 'fred': 42, 'jane': 100}

ooo = {}
print(ooo)  # {}

# ? Dictionaries: Common Applications
# * Counting: Histograms

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)  # * Output: {'csev': 2, 'cwen': 2, 'zqian': 1}

# ? The get method for dictionaries:
# * Simplified counting with get(). We can use get() and provide a default value of zero when the key is not yet in the dictionary - and then just add one.

counts = dict()
names = ["csev", "cwen", "csev", "zqian", "cwen"]

for name in names:
    counts[name] = counts.get(name, 0) + 1

print(counts)  # * {'csev': 2, 'cwen': 2, 'zqian': 1}

# * 0 is the default value:
counts = {"quincy": 1, "mrugesh": 42, "beau": 100, "0": 10}
print(counts.get("kris", 0))  # * Output: 0

# ? Asking a user prompt:
counts = dict()
line = input("Enter a line of text:")
words = line.split()

print("Words:", words)
print("Counting...")

for word in words:
    counts[word] = counts.get(word, 0) + 1

print("Counts", counts)
# * Enter a line of text:the clown ran after the car and the car ran into the tent and the tent fell down on the clown and the car

# * Words: ['the', 'clown', 'ran', 'after', 'the', 'car', 'and', 'the', 'car', 'ran', 'into', 'the', 'tent', 'and', 'the', 'tent', 'fell', 'down', 'on', 'the', 'clown', 'and', 'the', 'car']

# * Counting...

# * Counts {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}

# ? Definite loops and Dictionaries:
counts = {"chuck": 1, "fred": 42, "jane": 100}

for key in counts:
    print(key, counts[key])
# * Output:
# * chuck 1
# * fred 42
# * jane 100

# ? Retrieving lists of Keys and Values
# * You can get a list of keys, values and items(both) from a dictionary:

jjj = {"chuck": 1, "fred": 42, "jane": 100}
print(list(jjj))  # * ['chuck', 'fred', 'jane']
print(jjj.keys())  # * dict_keys(['chuck', 'fred', 'jane'])
print(jjj.values())  # * dict_values([1, 42, 100])
print(jjj.items())  # * dict_items([('chuck', 1), ('fred', 42), ('jane', 100)])

# ? Bonus: Two Iteration Variables:

months = {"january": 1, "february": 42, "march": 100}
for month, quantity in months.items():
    print(month, quantity)
    # * Output:
    # * january 1
    # * february 42
    # * march 100

# ? Exercise:

name = input("Enter file:")
handle = open(name)

counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)  # * the 7

# * Output:
# * Enter file:clown.txt
# * the 7

# ? ________________________________________________________________________

fname = input("Enter File:")
if len(fname) < 1:
    fname = "clown.txt"
hand = open(fname)

dictionary = dict()
for line in hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        # * idiom: retrieve/create/update counter
        dictionary[word] = dictionary.get(word, 0) + 1
        # * print(word, "new", dictionary[word])

print(dictionary)
# * Output: {'the': 7, 'clown': 2, 'ran': 2, 'after': 1, 'car': 3, 'and': 3, 'into': 1, 'tent': 2, 'fell': 1, 'down': 1, 'on': 1}

# ? Now we want to find the most common word:
largest = -1
theword = None

for key, value in dictionary.items():
    # print(key,value)
    if value > largest:
        largest = value
        theword = key  # * capture/remember the word that was largest

print(theword, largest)  # * Output: the 7
