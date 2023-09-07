## Outputting information from the program to the user

In python, use the `print()` function to output information to the user.

Here is a run-of-the-mill print statement:
```
print("Hello, World!")
```
When you run this line of code, the following is output this to the console:
```
Hello, World!
```

The following two lines show that when you have two print statements, they get executed in order. 
```
print("Hello")
print("World")
```
The output shows that each print statement automatically takes you to the next line on the console.
```
Hello
World
```

You can put two or more strings in a print statement, separated by a comma:
```
print("Hello", "World", "!")
```
The output shows that a space automatically is inserted between each parameter:
```
Hello World !
```

You can use the `+` operator for *concatenation* (Concatenation means putting two strings together by tacking the second one onto the end of the first one).
```
print("Hello"+"World")
```
The output shows that when concatenating strings, a space does **not** automatically get inserted:
```
HelloWorld
```

Here are several ways to put a space between two different strings:
```
print("Hello", "World")
print("Hello " + "World")
print("Hello" + " World")
print("Hello" + " " + "World")
```
Use `\n` to insert a new line in the middle of a string:
```
print("Hello\nWorld")
```
Here's the output:
```
Hello
World
```

## Getting input from the user into the program

Use the `input()` function to ask the user of your program for a value. For example:
```
username = input("Enter your name: ")
print("Hello,", username)
```
Notice that the parameter to the `input()` function within the parentheses is a string that you want to display to the user as a message. That message is called a prompt, and it gets output to the console as part of the `input()` line. (In other words, you don't need a separate `print()` statement). Make sure the prompt clearly communicates to the user what information you are asking them to enter. Once they type the value and hit the `<return>` key,
the `input` function returns the value they entered. In the above example, the user's response is stored in a variable called `username`.
Here's a sample run of the above program:
```
Enter your name: Sam
Hello, Sam
```

Note that the type that the `input` function returns is a string. So
```
username = input("Enter your name: ")
print(type(username))
```
will output
```
<class 'str'>
```
Often we want the user to input a numerical value rather than a string (text) value. In this case we must cast the result to convert it to a numerical type. For example:
```
user_age = input("Enter your age: ")
user_age = int(user_age)
print("Next year you will be", user_age + 1)
```
Sample run of the above program:
```
Enter your age: 19
Next year you will be 20
```

Note that the casting can actually be done on the same line as the input. The `input()` function returns a string, which we immediately cast using the `int()` function:
```
user_age = int(input("Enter your age: "))
print("Next year you will be", user_age + 1)
```

## Putting it all together
Here's a full sample program:
```
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
    print("You walked", num_of_miles, "miles today")

# Run the program:
if __name__ == '__main__':
    main()
```

Sample run from the above program:
```
Program that computes number of miles from steps walked
How many steps did you walk today? 10000
You walked 4.444444444444445 miles today
```