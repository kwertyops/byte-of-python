## Functions that take parameters

You're already familiar with calling functions that take input values (*parameters*). For example:

```python
# The `print()` function accepts a parameter - the string to output to the console
print("Hello!")

# The dudraw ellipse function takes four parameters
# x-location of center, y-location of center, half-width, and half-height
dudraw.line(0, 0, 1, 0.5)
```
Notice that when you call (i.e., *use*) a function that has parameters, you put those values within the parentheses of the function call. These values are also called *arguments*. You must pass the correct number of arguments (i.e., the number of values the defined function is expecting), and they must be passed in the correct order.

We will now learn how to create user-defined functions that accept parameters. Just like variables, the parameters each have a name (that name can be accessed only within the function definition). Here is the template:

```python
def function_name(parameter1_name: parameter1_type, parameter2_name: parameter2_type,...) -> None:
    # Code defining the function
```

Example 1: In the program below, the simple function `greet_user()` outputs `"Hello, world!"` to the console multiple times. The parameter to the function determines how many times the line is output. The parameter gives a way of passing information (the number of greetings to output) from the line that calls the function to the function itself.

<table>
<tr><td>Code</td><td>Output</td></tr>
<tr>
<td nowrap>

```python
def greet_user(num_greetings: int) -> None:
    for i in range(num_greetings):
        print(f"Hello, world!")

def main():
    greet_user(5)

# Run the program:
if __name__ == '__main__':
    main()
```
</td>

<td>

```
Hello, world!
Hello, world!
Hello, world!
Hello, world!
Hello, world!
```
</tr>
</table>

Example 2: Here we see the definition of a simple function that takes two parameters: the number of greetings to output, and the name of the user.

<table>
<tr><td>Code</td><td>Output</td></tr>
<tr>
<td nowrap>

```python
def greet_user(num_greetings: int, name: str) -> None:
    for i in range(num_greetings):
        print(f"Hello, {name}")

def main():
    username = input("What is your name? ")
    num = int(input("How many greetings do you want? "))
    greet_user(num, username)

# Run the program:
if __name__ == '__main__':
    main()
```
</td>

<td>

```
What is your name? Mahsa
How many greetings do you want? 3
Hello, Mahsa
Hello, Mahsa
Hello, Mahsa
```
</tr>
</table>

In this course, we will have a standard for commenting functions. After the `def` line, put a block comment (a docstring) explaining the purpose of the function as well as any parameters and what their purpose is. For example:

```python
def greet_user(num_greetings: int, name: str) -> None:
    """ Give greetings to the user, including their name
        parameters:
            num_greetings: number of repetitions of greeting (type: int)
            name: username, to be included in greeting (type: str)
        return: None
    """
    for i in range(num_greetings):
        print(f"Hello, {name}")
```

