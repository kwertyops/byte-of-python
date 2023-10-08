## String methods

In python, strings come with many built-in methods that allow us to examine and compute results about text. A *string method* is a special kind of function that is executed on a specific string.
Execute a string method with the syntax `your_string.method_name()`.  We will learn just a few of the many available string methods. 

## Documentation
The full details of the entire list of string methods is not something people typically memorize. Instead you are encouraged to look up the details when you need them. The full list can be found at [Python string documentation by w3schools](https://www.w3schools.com/python/python_ref_string.asp) or [Offical python documentation on string methods](https://www.w3schools.com/python/python_ref_string.asp). While there are many options for free on-line tutorials and helpful documentation, note that often in the interest of brevity they contain small inaccuracies. See the official documentation for the final accurate word on all details.

## Summary of a few string methods
Here is the list methods you'll learn:
- boolean informational methods: `islower()`, `isupper()`, and `endswith()`
- methods for creating a modified copy: `lower()`, `upper()`, `replace()` and `rstrip()` (each return a new modified string, leaving the original string unchanged)
- informational methods for searching within strings: `index()`, `find()`, `count()`, and the `in` keyword
- break the string into parts: `split()`


Here is how to use these methods.

<ul>
<li> 

`islower()->bool` and `isupper()->bool`

The call  `your_string.islower()` returns `True` if the letters in `your_string` are only lower-case, `False` otherwise. Similarly, `your_string.isupper()` returns `True` if the letters in `your_string` are all upper case, `False` otherwise.

```python
quote = 'These are not the droids you are looking for.'
if quote.islower():
    print("The quote is all lower case")
else:
    print("The quote is not all lower case")  # this gets output
movie_name = "ET"
if movie_name.isupper():
    print("The movie name is all upper case") # this gets output
else:
    print("The movie name is not all upper case")
```
</li>

<li> 

`lower()->str` and `upper()->str`

The call `your_string.lower()` returns a new string in which all letters are converted to lower case. The original string is not modified. Similarly, `your_string.upper()` returns a new string in which all letters are converted to upper case, leaving the original string unchanged. Note that non-letters are unaffected (digits, spaces, punctuation, special characters are *uncased*, they do not have two versions, and are unchanged by these methods).

```python
names = "R2D2 and C3PO"
print(names.upper()) # outputs "R2D2 AND C3PO"
print(names.lower()) # outputs "r2d2 and c3po"
print(names)         # outputs "R2D2 and C3PO", the original unchanged string
```

 If you want the value stored in the variable to be converted, then you  must re-assign it to the value returned by the method. For example
 ```python
 names = "R2D2 and C3PO"
 names = names.upper()
 print(names) # outputs "R2D2 AND C3PO" because the value of names was changed by the reassignment
 ```
</li>

<li>

`endswith()->bool`

A call to `your_string.endswith(pattern)` checks to see if the end of `your_string` matches the string `pattern`, returning `True` if so, and `False` otherwise.

```python
filename = input("Enter the filename of your program: ")
if not filename.endswith(".py"):
    print(f"Error: {filename} is not a python program.")
```
Sample output:
```
Enter the filename of your program: pacman.java
Error: pacman.java is not a python program.
```


</li>
<li>

`index(sub: str)->int`

This method is analogous to the `index()` method for lists. The call `your_string.index(sub)` finds and returns the index of the first location where the string `sub` appears as a substring of `your_string`. If the string `sub` does not appear at all in the string, then the program crashes with a `ValueError`

```python
poem = 'Roses are red, violets are blue'
print(poem.index('red'))   # outputs 10, since 'red' appears at index 10
print(poem.index('green')) # crashes with a ValueError: substring not found
```

The `index()` method also allows you to specify an optional `int` as a second parameter. This parameter represents the index in the string where you want to start the search:
```python
text = "XXXXXHello, Xiomara!"
print(text.index('X'))     # output 0, first 'X' as at index 0
print(text.index('X', 4))  # outputs 4, starting at index 4, first 'X' is at index 4
print(text.index('X', 5))  # outputs 12, starting at index 5, first 'X' is at index 12
```
<li>

`find(sub: str)->int`

Similar to `index()`, `find()` finds and returns the index of the first location where the string `sub` is found in `your_string`. But for `find()`, if `sub` does not appear at all in the string then `-1` is returned, rather than throwing a `ValueError`. It also accepts an optional second parameter to use as the start index. For example:

```python
poem = 'Roses are red, violets are blue'
print(poem.find('are'))     # outputs 6, since 'are' appears at index 6
print(poem.find('are', 10)) # outputs 23, the first location of 'are' after index 10
print(poem.find('green'))   # outputs -1, since 'green' does not appear in poem
```
The `find()` is method is specific to strings - there is no `find()` method for lists.
</li>

<li> 

The membership operators `in` and `not in`

Like in lists, you can use the `in` and `not in` keywords to determine if a string appears as a substring in another string. For example:

- the boolean expression `'them' in 'Chrysanthemum'` evalutes to `True`
- the boolean expression `'i' not in 'team'` evalutes to `True`

Note that `in` and `not in` are *not methods*, so you do not call them with the familiar `your_string.method()` syntax.

</li>

<li>

`string.count(sub: str)->int`

This method is analogous to the `count()` method for lists. The call `your_string.count(sub)` returns the number of times that the substring `sub` appears in `your_string`. An optional `int` parameter gives a start index to begin the search.

```python
poem = 'Roses are red, violets are blue'
print(poem.count('night'))   # outputs 0, since 'night' does not appear in the string
print(poem.count('are'))     # outputs 2, since 'are' appears twice in poem
print(poem.count('are', 10)) # outputs 1, since starting at index 10, 'are' appears once
```

</li>

<li>

`replace(old: str, new: str)->str`

The call `your_string.replace(old, new)` produces a new string with every occurence of the substring `old` replaced with `new`. The new string is returned, and `your_string` is unchanged. An optional 3rd `int` parameter gives the *number* of replacements to make.
```python
poem = 'Roses are red, violets are blue'
print(poem.replace('are', 'shine'))  # outputs 'Roses shine red, violets shine blue'
print(poem.replace('are', 'shine', 1)) # outputs 'Roses shine red, violets are blue'
print(poem) # outputs 'Roses are red, violets are blue', since poem is unchanged
```
</li>

<li>

`rstrip()->str`

The call `your_string.rstrip()` returns a new string with all whitespace at the end of the string removed. Think of it as *right strip*. (technical detail: whitespace in python includes spaces, tabs, newlines, vertical tabs, line feeds and carriage returns). Note that `your_string` is not modified. You can optionally pass a `str` parameter to `rstrip()` to specify a different list of characters to strip from the right end of `your_string`. Also, there are analogous methods `lstrip()` and `strip()`. See the documentation for additional details.

This method will be very important when we read from files, since we will often want to remove newlines from the end of each line we read.

```python
movie_quote = "What is the airspeed velocity of an unladen swallow?  \n"
print(len(movie_quote))   # outputs 55, the number of characters in the string
# The next line makes a copy of the quote, with the '  \n' stripped off,
# then reassigns movie_quote to refer to the new string
movie_quote = movie_quote.rstrip() 
# On the next line, you will be able to see that the newline is gone,
# (though you won't be able to tell on the console that the spaces are missing)
print(movie_quote)
# The next line outputs 52, proving that the last three characters are gone
print(len(movie_quote))
```

</li>

<li>

`split()->list[str]`

The call `your_string.split()` returns a list of substrings. By default, the list is split at whitespace characters (and the whitespace is removed). So you can think of this method as a way to split a sentence into words. Note that the return value is not a string, but it is a list of strings!
```python
movie_quote = "What is the airspeed velocity\nof an unladen swallow?"
words = movie_quote.split()
print(words)
print(len(words)) # Number of elements in returned list = number of words in original string
```
Output:
```
['What', 'is', 'the', 'airspeed', 'velocity', 'of', 'an', 'unladen', 'swallow?']
9
```

You can optionally give a parameter to the `split()` method which is a string containing the character(s) you want to use as the delimeter instead of the default whitespace.
```python
# Split text into substrings, assuming they are separated by commas
states = "Alabama,Alaska,Arizona,Arkansas"
state_list = states.split(",") # Use a comma delimeter
print(state_list) # outputs ['Alabama', 'Alaska', 'Arizona', 'Arkansas']

# Split text into a list of lines
text = 'Line 1\nLine2\nLine3'
lines = text.split('\n') # Use a newline delimeter
print(lines) # outputs ['Line 1', 'Line2', 'Line3']
```
</li>



</ul>