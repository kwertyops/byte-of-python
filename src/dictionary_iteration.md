## Iterating over dictionaries

Dictionaries are primarily used for their fast implementation of searching for an item, removing an item, adding an item and modifying an item. In python dictionaries, each of these actions are made to execute fast by performing them without having to traverse through the entire dictionary. You'll learn about how this is accomplished in the first Data Structures and Algorithms class.

Occasionally, we are forced to traverse through all items in a dictionary. This operation runs slowly, so we avoid traversing dictionaries whenever possible. When it is unavoidable, there are three methods we use to iterate over dictionary tiems, keys, and values:

```python
your_dictionary.keys()   # returns a view object of all keys
your_dictionary.values() # returns a view object of all values
your_dictionary.items()  # returns a view object of tuples with key/value pairs for each item
```

## Example 1
The following examples demonstrates creating a dictionary, then traversing its keys, its values, and its items. The dictionary stores names and corresponding phone numbers.

```python
from random import randint

# list of names that were randomly generated:
names_list = [
    "Kelly Mathis", "Alisha Duran", "Marcella Robison", "Adyson Felton",
    "Magnus Jewell", "Luciano Leal", "Krew Temple", "Chance Chamberlain",
    "Romina Xiong", "Adina Looney", "Ayush Beal", "Finnley Broussard",
    "Robbie Donahue", "Titan Connelly", "Faris Kenney", "Kimber Murphy"]

# Create an empty dictionary to store a phonebook
phonebook = {}
# Add eaach name to the phonebook, giving them a randomly-generated phone number
for name in names_list:
    phonebook[name] = str(f"{randint(200, 999)}-{randint(100, 999)}-{randint(0, 9999)}")

# Iterate over all keys (names) in the phonebook:
for name in phonebook.keys():
    print(name)  # outputs all the keys (names) in the phonebook

# Iterate over all values (phone numbers) in the phonebook:
for phone_number in phonebook.values():
    print(phone_number)  # outputs all the values (phone numbers) in phonebook

# Iterate over all items (name/phone number tuples) in phonebook:
for item in phonebook.items():
    print(item)  # outputs all tuples (name/phone number pair) in phonebook

# Iterate over all keys in phonebook, outputting info for all names that start with 'A'
for name in phonebook.keys():
    if name.lower().startswith('a'):
        print(f"{name}: {phonebook[name]}")

# Another strategy for previous exercise:
# Iterate over all items in phonebook, outputting info for all names that start with 'A'
for item in phonebook.items():
    if item[0].lower().startswith('A'):
        print(f"{item[0]}: {item[1]}")
```

## Example 2
In this example, we create a dictionary whose keys are the name of a state, and the corresponding value is a list of that state's largest cities. The value is *not* a single city, but an entire list. Note that the key of the dictionary is a string, which is immutable as required. But the value can be mutable, in this case a list. We can change the value associated with a state by changing it to an entirely new list. Or, we can modify the list itself associated with a particular state.

```python
# Create a dictionary of the largest few cities in several state/territories
largest_cities = {"Alabama": ["Huntsville", "Montgomery", "Birmingham", "Mobile", "Tuscaloosa"],
                  "Alaska": ["Anchorage", "Fairbanks", "Juneau", "Wasilla", "Sitka"],
                  "American Samoa": ["Tafuna", "Nu'uuli", "Pago Pago", "Ili'ili", "Pava'ia'i"],
                  "Arizona": ["Phoenix", "Tucson", "Mesa", "Chandler", "Scottsdale"],
                  "California": ["Los Angeles", "San Diego", "San Jose", "San Francisco", "Fresno"]
                }

# Change the dictionary entry for American Samoa to refer to an entirely new list:
largest_cities["American Samoa"] = ["Pago Pago", "Tafuna", "Leone", "Faleniu", "Aua"]

# Add a new item to the dictionary. Key is "Colorado", and its value is a list of cities
largest_cities["Colorado"] = ["Denver", "Colorado Springs", "Aurora"]
print(largest_cities["Colorado"])

# Add a city to Colorado's list. Note that largest_cities["Colorado"] is a list.
# We are appending a new city to that list
largest_cities["Colorado"].append("Fort Collins")
print(largest_cities["Colorado"])
```