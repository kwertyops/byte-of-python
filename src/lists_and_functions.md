## Functions can take lists as parameters, or can return lists

Recall the syntax for defining a function:

```python
def functon_name(optional parameters)->return type:
    # Indented code block
    # Optional return statement
```

Recall that we have seen parameter types and return types such as `None`, `float`, `str`, or `int`. What is new in this section is to define functions that takes parameters that are `list`s, or whose return type is a `list`.

Here's a template for the definition of a function that takes a list of `int`s as a parameter:

```python
def foo(some_list: list[int])->None:
    # code block
```

Here is a template for the definition of a function that returns a list of `str`s:

```python
def bar()->list[str]
    # code block
    return a_list_of_strings
```

## Putting it all together
The program below demonstrates taking a `list` as a parameter to a function, and returning a `list` from a function. The first function checks to see if a list has only positive values. The second function extracts all of the nonpositive values from a list, returning a new list with just the nonpositive values.

The main program creates a list of random numbers. Then it checks to see if they are all positive. If so, it outputs them. Otherwise, it outputs the list of numbers that weren't positive.

```python
from random import random

def is_all_positive(some_list: list[float])->bool:
    """
    Determines if every element in the given list is positive

    parameters:
        some_list : a list of float values
    return:
        True if all values are positive and False otherwise
    """
    for element in some_list:
        # As soon as you find a nonpositive number, return False
        if element <= 0:
            return False
    
    # If we make it this far, then they are all positive
    return True

def get_all_nonpositives(some_list: list[float])->list[float]:
    """
    Build a new list containing all nonpositive values from some_list

    parameters:
        some_list : a list of float values
    return:
        A new list containing nonpositive float values (type: list[float])
    """
    nonpositives = []

    # iterate over all elements, append each negative one to the new list
    for element in some_list:
        if element < 0:
            nonpositives.append(element)

    return nonpositives

def main():
    # start with an empty list
    a_list = []

    # Make a list of 5 random floats between -100 and 100
    for i in range(5):
        # random() gives a float in [0, 1)
        # random()*200 gives a float in [0, 200)
        # random() * 200 - 100 gives a float in [-100, 100)
        a_list.append(random() * 200 - 100)

    # If they all came out positive, show the list
    if is_all_positive(a_list):
        print(f"The list is all positive: {a_list}")
    # If they weren't all positives, output the ones that aren't:
    else:
        nonpositives = get_all_nonpositives(a_list)
        print(f"Here are the {len(nonpositives)} nonpositive elements: {nonpositives}")



# Run the program:
if __name__ == '__main__':
    main()
```