## Outputting information from the program to the user

In Python, use the `print()` function to output information to the user.

Here is a run-of-the-mill print statement:
```python
print("Hello, World!")
```
When you run this line of code, the following is output this to the console:
```
Hello, World!
```

The following two lines show that when you have two print statements, they get executed in order. 
```python
print("Hello")
print("World")
```
The output shows that each print statement automatically takes you to the next line on the console.
```
Hello
World
```

You can put two or more strings in a `print()` statement, separated by commas. Usually, one or more of these string values comes from a variable. Note that the comma inside the quotes is part of the output, while the commas between strings are part of the syntax of the `print()` statement:
```python
username = "Sam"
print("Hello,", username, "!")
```
The output shows that a space automatically is inserted between each parameter:
```
Hello, Sam !
```

Another way to build strings for output is to use the `+` operator for *concatenation* (Concatenation means putting two strings together by tacking the second one onto the end of the first one).
```python
print("Hello," + username + "!")
```
The output below shows that when concatenating strings, a space does **not** automatically get inserted:
```
HelloSam!
```

Here are ways to put a space between two different strings
```python
print("Hello", username)
print("Hello " + username)
```
Use `\n` to insert a new line in the middle of a string:
```python
print("Hello\nWorld")
```
Here's the output:
```
Hello
World
```

The backslash symbol `\`  in `\n` is called an *escape character*. It tells Python that the letter following the backslash should be interpreted together with the `\` as a pair with special meaning. Other examples include 
- `\t` for tab, 
- `\"` and `\'` to put a double quote or single quote into a string literal, and
- `\\` to insert a backslash.

For example, see if you can write a `print()` statement to produce the following tricky output:
```
"\n" is a newline,
while "\'" is a single quote.
```
Answer:
```python
print("\"\\n\" is a newline,\nwhile \"\\\'\" is a single quote.")
```

A third way in Python to combine multiple strings together and to include variable values within a string is a *formatted string literal*, commonly called an *f-string*. Create an f-string by prefixing the string with an `f`, then include any variable values within a pair of curly braces `{}`. For example:
```python
print(f"Hello, {username}!")
```
outputs
```
Hello, Sam!
```
With f-strings, you can have rich and control over the formatting.
For example
```python
import math
print(f"pi to 5 decimal places is {math.pi:.5f}, and e to 3 decimal places is {math.e:.3f}.")
```
outputs
```
pi to 5 decimal places is 3.14159, and e to 3 decimal places is 2.718.
```

Here's an online tutorial if you want to investigate more capabilities of f-strings:
[https://builtin.com/data-science/python-f-string](https://builtin.com/data-science/python-f-string)

Finally, it sometimes causes us problems that a call to `print()` automatically includes a newline at the end of the output. Occasionally we want to suppress that. We do this by specifying in a second parameter to `print()` that the end should be an empty string `""` rather than the default `"\n"`. Here's an example showing how two calls to `print()` can both output on the same line of the console:

```python
print("Hello, world! ", end="")
print("It's a beautiful day! ")
```

Output:
```
Hello, world! It's a beautiful day! 
```



## Getting input from the user into the program

Use the `input()` function to ask the user of your program for a value. For example:
```python
username = input("Enter your name: ")
print("Hello,", username)
```
Notice that the parameter within the parentheses of the `input()` function is the string that you want to display to the user as a message. That message, called a prompt, is output to the console when the `input()` line is executed. In other words, you don't need a separate `print()` statement. Make sure the prompt clearly communicates to the user what information you are asking them to enter. Once they type the value and hit the `<return>` key,
the `input()` function returns the value they entered. In the above example, the user's response is stored in a variable called `username`.
Here's a sample run of the above program:
```
Enter your name: Sam
Hello, Sam
```

Note that the `input()` function always returns a string (of type `str`). To clarify,
```python
username = input("Enter your name: ")
print(type(username))
```
will output
```python
<class 'str'>
```
But often we want the user to input a numerical value rather than a string (text) value. In this case we must *cast* the result to convert it to a numerical type. This is mandatory any time you want to do arithmetic with the number the user enters. For example:
```python
user_age = input("Enter your age: ")
user_age = int(user_age)
print(f"Next year you will be {user_age + 1}.")
```
Sample run of the above program:
```
Enter your age: 19
Next year you will be 20.
```

Note that the casting can actually be done on the same line as the input. The `input()` function returns a string, which we can immediately cast using the `int()` function. The two lines below behave identically to the three lines of code just above.
```python
user_age = int(input("Enter your age: "))
print(f"Next year you will be {user_age + 1}.")
```

## Putting it all together
Here's a full sample program:
```python
"""
Demo of creating and using variables and user input

File Name: variables_and_user_input.py
Date:
Course: COMP1351
Assignment: Preclass Assignment 2
Collaborators: 1351 Instructors
Internet Sources: None
"""

def main():
    print("Program that computes number of miles from steps walked")
    # Find out step count from user
    step_count = int(input("How many steps did you walk today? "))
    # On average there are 2250 steps per mile
    num_of_miles = step_count/2250
    # Report result to user
    print(f"You walked {num_of_miles:.2f} miles today.")


# Run the program:
if __name__ == '__main__':
    main()
```

Sample run from the above program:
```
Program that computes number of miles from steps walked
How many steps did you walk today? 10000
You walked 4.44 miles today.
```
