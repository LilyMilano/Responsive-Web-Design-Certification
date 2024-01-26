# ? The Tuples Collection
# ? Tuples are another kind of sequence that functions much like a list - they have elements which are indexed starting at 0.

x = ("Glenn", "Sally", "Joseph")
print(x[2])
# Joseph

y = (1, 9, 2)
print(y)  # (1, 9, 2)
print(max(y))  # 9

for iter in y:
    print(iter)
    # 1
    # 9
    # 2

# * but... Tuples are "immutable."
# * Unlike a list, once you created a tuple, you cannot alter its contents -similar to a string:
# z = (5, 4, 3)
# z[2] = 0
# Traceback (most recent call last):
# TypeError: 'tuple' object does not support item assignment

t = tuple()
print(dir(t))
# * ['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'count', 'index']

# * TUPLES ARE MORE EFFICIENT THAN LISTS.

# ? Tuples and Assignment:______________________________________________
# * We can also put a tuple on the left-hand side of an assignment statement.
# * We can omit the parentheses.

(x, y) = (4, "fred")
print(y)  # fred

(a, b) = (99, 98)
print(a)  # 99

# ? Tuples and Dictionaries:______________________________________________
# * The items() method in dictionaries returns a list of (key, value) tuples.

d = dict()
d["csev"] = 2
d["cwen"] = 4

for k, v in d.items():
    print(k, v)
    # csev 2
    # cwen 4

tups = d.items()
print(tups)
# dict_items([('csev', 2), ('cwen', 4)])

# ? Tuples are Comparable:_________________________________________________
# * The comparison operators work with tuples and other sequences. If the first item is equal, Python goes on the next element, and so on, until it finds elements that differ:

result = (0, 1, 2) < (5, 1, 2)  # type: ignore
print(result)  # * This will print True

print((0, 1, 20000000) < (0, 3, 4))  # type: ignore
# * True

print(("Jones", "Sally") < ("Jones", "Sam"))  # type: ignore
# * True

print(("Jones", "Sally") > ("Adams", "Sam"))  # type: ignore
# * True

# ? Exercise _______________________________________________________________

d = dict()
d["quincy"] = 1
d["beau"] = 5
d["kris"] = 9

for k, i in d.items():
    print(k, i)
    # quincy 1
    # beau 5
    # kris 9

# ? Comparing and Sorting Tuples ___________________________________________

d = {"a": 10, "b": 1, "c": 22}
print(d.items())  # dict_items([('a', 10), ('b', 1), ('c', 22)])
print(sorted(d.items()))  # [('a', 10), ('b', 1), ('c', 22)]

for k, v in sorted(d.items()):
    print(k, v)
    # a 10
    # b 1
    # c 22

# * Sort by values instead of keys:
# * If we could construct a list of tuples of the form (value, key) we could sort by value.
# * We do this with a for loop that creates a list of  tuples.
c = {"a": 10, "b": 1, "c": 22}
tmp = list()

for k, v in c.items():
    tmp.append((v, k))

print(tmp)  # * [(10, 'a'), (1, 'b'), (22, 'c')]
tmp = sorted(tmp, reverse=True)
print(tmp)  # * [(22, 'c'), (10, 'a'), (1, 'b')]

# ? Exercise: The top 10 most common words:________________________________
fhand = open("quixote.txt")
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

    # Output:
    # a 18
    # and 17
    # the 13
    # was 10
    # to 10
    # of 10
    # that 8
    # on 8
    # he 8
    # his 7

# * EVEN SHORTER VERSION: Sort by values instead of keys
# * List comprehension creates a dynamic list. In this case, we make a list of reversed tuples and then sort it.

c = {"a": 10, "b": 1, "c": 22}

print(sorted([(v, k) for k, v in c.items()]))

#   [(1, 'b'), (10, 'a'), (22, 'c')]

# https://wiki.python.org/moin/HowTo/Sorting
