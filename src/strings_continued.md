This section contains some new information about using python strings.

## "Arithmetic" on strings

You've seen the `+` concatenation operator, which  naturally can be extended to the `+=` shorthand operator.
```python
name = "Iron"
# Concatenate "Man" to end of "Iron", reassigning to name:
name += "Man"  #name now stores "IronMan"
# Convert int 3 to string "3", concatenate to end of "IronMan", reassigning to name:
name += str(3)
print(name) # outputs IronMan3
```
An uncommonly-used but cute feature of python is multiplying a string by an integer. This results in the string being repeated multiple times.
```python
print("Hello!"*5)
```
outputs
```
Hello!Hello!Hello!Hello!Hello!
```

## Accessing individual elements of strings

Many of the operations you've learned on lists also work on strings (and some do not).

The `len()` function returns the number of characters in a string.
```python
greeting = "Welcome to the wonderful world of strings."
print(len(greeting))  # outputs 42, the number of characters in greeting
```

Just like lists, strings are ordered. So we can use an index to access individual characters in a string. Similarly, they can be sliced.
```python
greeting = "Welcome to the wonderful world of strings."
print(greeting[0])   # outputs the first character, "W"
print(greeting[-1])  # outputs the last character, "."
print(greeting[:10]) # outputs first 10 characters, "Welcome to"
print(greeting[-5:]) # outputs from 5th to last up to last, "ings."
```
## Iterating over the characters in a string (`for`-loops)

You can use a for loop to traverse the characters in a string, either by iterating over the index values, or iterating over the characters themselves.

Here's an index-based loop that counts the number of `"o"`s in the string:

```python
count = 0  # initial value, zero o's
# iterate over all index values. i ranges from 0 to 41
for i in range(len(greeting)):
    # greetings[i] is the next character in the string
    if greeting[i] == "o":
        # if the current character is an "o", count it
        count += 1
# output the formatted result
print(f"Number of o's in the greeting is {count}.")
```
The code below is the content-based version of the same code. This time the variable `character` iterates over each character in the greeting, starting from `W` and ending with `.`, the last character. The variable `character` takes the value of each character in turn, so we don't need worry about the length of the string, nor keep track of the value of the index.
```python
count = 0  # initial value, zero o's
# iterate over all characters, from "W" to "."
for character in greeting:
    # character is the next character in the string
    if character == "o":
        # if the current character is an "o", count it
        count += 1
# output the formatted result
print(f"Number of o's in the greeting is {count}.")
```

## Strings are immutable

Unlike lists, strings are immutable. This means their contents cannot be changed. While I can access an individual character in a string with an index in square brackets, attempting to modify an individual character fails with a `TypeError`

```python
greeting = "Welcome to the wonderful world of strings."
greeting[0] = 'V'
```
outputs
```
TypeError: 'str' object does not support item assignment
```
This doesn't mean that the value stored in a variable can't be changed. But because of the immutability of strings, we must re-assign a new string to the variable, rather than changing the contents of the string itself. Here's one possible way to do this:
```python
greeting = "Welcome to the wonderful world of strings."
# Build an entirely new string, starting with "V", then concatenating all but the first character of the original
greeting = "V" + greeting[1:] 
print(greeting)
```
outputs
```
Velcome to the wonderful world of strings.
```


