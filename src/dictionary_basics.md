## Creating dictionaries in python

A dictionary is a collection of key/value pairs. The keys must be unique, and must be of an *immutable* type (such as `int`, `str`, `float`, `tuple`, but *not* `list`). The dictionary itself *is* mutable.

One way to define a dictionary in python is to use a *dictionary literal*. We list the items separated by commas, and surround the list with curly brackets `{}`. Each item is defined as `key:value`. For example, here's a dictionary that stores phone numbers associated with each unique name:

```python
phonebook = {'Jane': '213-665-1234', 
             'Milagros': '720-933-5418', 
             'Kebede': '847-439-4312',
             'Desta': '847-439-4312' }
```
Each name is the key, and the phone numbers are the associated values. The key type is `str`, which is immutable as required. Here, the value is also a `str`, but note that the value *is allowed* to be mutable. For example, the value could be a list of associated phone numbers. Duplicate names are not allowed, but duplicate values are.

Another way to create a dictionary is with the `dict()` function. Pass a list of tuples representing the key/value pairs. The `phonebook` above could equally have been created with this line:

```python
phonebook = dict([('Jane', '213-665-1234'), 
             ('Milagros', '720-933-5418'), 
             ('Kebede', '847-431-1729'),
             ('Desta', '847-439-4312')])
```
Read the above definition of phonebook carefully: it has a pair of outermost parentesis `()` for the funtion call to `dict()`, it has a pair of square brackets `[]` for the beginning and end of the list of tuples, and each tuple in the list is defined with a pair of parentheses `()`, and consists of a key/value pair.

You can create a new empty dictionary in either of these two ways:
```python
empty_dictionary1 = {}
empty_dictionary2 = dict()
```

## Accessing, modifying and adding items to a dictionary

We can access individual elements of a dictionary using the same square-bracket syntax we use for an index in lists and strings. Put the key in the square brackets. 
```python
print(phonebook['Desta']) # outputs 847-439-4312
milagros_number = phonebook['Milagros'] # look up and store Milagros number in a variable
```
Think of this as a *lookup*. The expression `phonebook['Desta']` looks up in the dictionary for an item with key `Desta`. The expression then gives the value associated with the key `Desta`.

That same syntax can be used to add a new item to the dictionary or to modify an existing element

```python
phonebook['HuanHuan'] = '602-654-3210' # adds a new item to the dictionary with key 'HuanHuan'
phonebook['Jane'] = '808-647-1234' # changes phone number for key 'Jane'
```

If you try to access a key that does not exist in the dictionary, a `KeyError` is produced.
```python
# The program crashes on this line with a KeyError
# since there is  no item in phonebook with key "Kai"
print(f"Kai's number: {phonebook['Kai']}")
```
## Deleting items from a dictionary
To remove an item from a dictionary, we can use the `del` operator:

```python
print(phonebook['Kebede']) # outputs '847-431-1729'
del phonebook['Kebede']    # removes item with key `Kebede`
print(phonebook['Kebede']) # crashes with a KeyError
```

## Checking for membership in a dictionary

To check if a key exists in a dictionary, use the `in` operator.
The expression
`<key> in <dictionary>` is a boolean expression that evaluates to `True` if the `key` matches an item in the dictionary, `False` otherwise.

This gives us a way to avoid accessing a non-existent element, thus avoiding a `KeyError`
```python
if `Kebede` in phonebook:
    print(f"Kebede's number is {phonebook['Kebede']}")
else:
    print("No  known phone number for Kebede.")
```

Note: you could alternately handle key errors by accessing the dictionary within a `try` block and handling `KeyError`s with the `except` block.

## Practice exercises

```python
# Exercise 1: create an empty phonebook and print it:
phonebook = dict()
print(f"empty: {phonebook}")

# Exercise 2: Reinitialize the phonebook with two number in 2 different ways
#first way:
phonebook = {"Alice": "123-145-2541", "Bob": "145-145-7514"}
print(f"Phonebook with 2 items: {phonebook}")
# second way:
phonebook = dict([("Alice", "123-145-2541"), ("Bob", "145-145-7514")])
print(f"Same phonebook with 2 items: {phonebook}")

# Exercise 3: Add two more names to phonebook and output it
phonebook["Hong"] = "145-134-5614"
phonebook["Emily"] = "145-146-7316"
print(f"Phonebook after adding two more items: {phonebook}")

# Exercise 4: Print a phone number from the phonebook, then modify it, then print it again
print(f"Before: {phonebook['Alice']}")
phonebook["Alice"] = "111-111-1111"
print(f"After: {phonebook['Alice']}")

# Exercise 5: Try printing a phone number for a key that doesn't exist (producing a KeyError)
print(phonebook["Marcelo"]) # crashes with Key Error

# Exercise 6: Fix the code above to check for membership before accessing a nonexistent key
if "Marcelo" in phonebook:
    print(phonebook["Marcelo"]) # output Marcelo's number if found
else:
    print("Marcelo is not in the phonebook")

# Exercise 7: Delete and item and print the dictionary
del phonebook["Alice"]
print(phonebook)
```