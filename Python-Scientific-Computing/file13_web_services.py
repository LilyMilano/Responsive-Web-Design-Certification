import xml.etree.ElementTree as ET
import json

# ? XML AND JSON
# ? XML: eXtensible Markup Language
# * Primary purpose is to help information systems share structured data.

data = """ <person>
    <name>Chuck</name>
    <phone type="int1"> +1 734 303 4456
    </phone>
    <email hide="yes"/>
</person>"""

tree = ET.fromstring(data)

name_element = tree.find("name")
if name_element is not None:
    print("Name:", name_element.text)

email_element = tree.find("email")
if email_element is not None:
    hide_attribute = email_element.get("hide")
    print("Attr:", hide_attribute)

# Output:
# Name: Chuck
# Attr: yes

# __________________________________________________________________________

input = """<stuff>
    <users>
        <user x="2">
            <id>001</id>
            <name>Chuck</name>
        </user>
        <user x="7">
            <id>009</id>
            <name>Brent</name>
        </user>
    </users>
</stuff>"""

stuff = ET.fromstring(input)
lst = stuff.findall("users/user")
print("User count:", len(lst))
for item in lst:
    name_element = item.find("name")
    if name_element is not None:
        print("Name", name_element.text)

    id_element = item.find("id")
    if id_element is not None:
        print("Id", id_element.text)
    print("Attribute", item.get("x"))

    # User count: 2
    # Name Chuck
    # Id 001
    # Attribute 2
    # Name Brent
    # Id 009
    # Attribute 7

    # * In this code, before accessing the text attribute of the name and id elements, we first check if the result of find() is not None. This helps to avoid the warning and ensures that we only access the text attribute when the element is found.

# ? JSON: JavaScript Object Notation:
# * JSON represents data as nested "lists" and "dictionaries."

data = """{
    "name" : "Chuck",
    "phone" : {
        "type" : "int1",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}"""

info = json.loads(data)
print("Name:", info["name"])  # Name: Chuck
print("Hide:", info["email"]["hide"])  # Hide: yes

# __________________________________________________________________________

input = """[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Lily"
    }
]"""

info = json.loads(input)
print("User count:", len(info))
for item in info:
    print("Name", item["name"])
    print("Id", item["id"])
    print("Attribute", item["x"])

    # User count: 2
    # Name Chuck
    # Id 001
    # Attribute 2
    # Name Lily
    # Id 009
    # Attribute 7

    # _______________________________________________________________________

    data = """
[
    { "id" : "001",
    "x" : "2",
    "name" : "Quincy"
    } ,
    { "id" : "009",
    "x" : "7",
    "name" : "Mrugesh"
    }
]
"""
info = json.loads(data)
print(info[1]["name"])  # Mrugesh
