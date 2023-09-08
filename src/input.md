## Getting input from the user into the program

Use the `input()` function to ask the user of your program for a value. For example:
```python
username = input("Enter your name: ")
print("Hello,", username)
```
Notice that the parameter within the parentheses of the `input()` function is the string that you want to display to the user as a message. That message is called a prompt, and it gets output to the console as part of the `input()` line. In other words, you don't need a separate `print()` statement. Make sure the prompt clearly communicates to the user what information you are asking them to enter. Once they type the value and hit the `<return>` key,
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
print("Next year you will be", user_age + 1)
```
Sample run of the above program:
```
Enter your age: 19
Next year you will be 20
```

Note that the casting can actually be done on the same line as the input. The `input()` function returns a string, which we can immediately cast using the `int()` function. The two lines below behave identically to the three lines of code just above.
```python
user_age = int(input("Enter your age: "))
print("Next year you will be", user_age + 1)
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
