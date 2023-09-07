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