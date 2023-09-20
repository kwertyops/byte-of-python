## Why we need while loops

Note that `for`-loops of the form
```python
for i in range(N):
    # indented block of code
```
repeat a block of code for a set number of iterations. But there are many cases when the number of repetitions is not known ahead of time.  For each of the following examples, you must use a `while`-loop, not a `for`-loop, because the number of repetitions is not known when the loop begins.
- Prompt a user to enter a password, asking repeatedly until they get it correct. You don't know in advance how many times it will take.
- Create an animation that continues until the user enters a `q` to quit. The animation must continue until they choose to quit, and until then the animation must continue an unknown number of frames.
- Write a game for two players who take turns. You don't know how many turns it will take for someone to win.

## Syntax of a `while` statement:
```python
while <condition>:
    # indented block of code
# rest of program
```
The `<condition>` is a boolean expression. If it evalutes to `True`, then the indented block of code is executed, and the program returns to the `while` statement to check the condition again. This repeats until the condition evaluates to `False`, when the loop stops executing, and the program continues on the next line.

Here is the flowchart that shows visually the path of execution through a `while`-loop:

<figure>
<img src="img/while/while_flowchart.png" alt="4 houses, scaled and shifted variously" class="center", width="200">
</figure>

## Example

The following program repeatedly asks the user `"What is the answer to life, the universe and everything?"`, until the user correctly answers `"42"`.

```python
life_meaning = input("What is the answer to life, the universe and everything? ")

while life_meaning != "42":
    life_meaning = input("What is the answer to life, the universe and everything? ")

print("Correct!")
```

Here is a sample run of the program:
```
What is the answer to life, the universe and everything? string cheese
What is the answer to life, the universe and everything? zoroastrian dualism
What is the answer to life, the universe and everything? photobombing giraffe
What is the answer to life, the universe and everything? 42
Correct!
```

## Should I use a `for`-loop or a `while`-loop?

It is possible to use a `while`-loop instead of a `for`-loop. The two code blocks shown below behave the same, each of them outputting the integers from `0` to `9`:

<table>
<tr>
<td>

`for`-loop</td>
<td>

`while`-loop</td></tr>

<tr>
<td>

```python
for i in range(10):
    print(i)
```
</td>

<td>

```python
i = 0
while i < 10:
    print(i)
    i = i + 1
```
</td></tr>
</table>

Although the above code snippets show that it is *possible* to replace a `for`-loop with a `while`-loop, this is not advised. Instead, use the following guidelines to determine which type of loop to use:

- Use a `while`-loop when the number of iterations is **unknown** before the loop completes.
- Use a `for`-loop when before the loop starts, you know how many iterations you need. 
- It's still better to use a `for`-loop if the number of iterations is unknown while you are writing the program, but is determined during the program (in other words, `for i in range(variable)`), since in this case the value is known by the time the loop begins.

## Putting it all together

### Example 1
Here's an example of a full program that uses a `while`-loop. It simulates rolling a die, to see how many rolls before we roll a 6. Note that a `for`-loop is not possible here, since we do not know how many rolls of the die it will take until we finally roll a 6.

<table>
<tr><td>Code</td><td>Sample output</td></tr>
<tr>
<td nowrap style="display:inline-block; width:500px;">

```python
"""
Count how many rolls of a die it takes to roll a 6
Author: COMP 1351 Instructor
File Name: dice_roll_simulator.py
Date:
Course: COMP 1351
Assignment: while-loop notes
Collaborators: 1351 Instructors
Internet Sources: None
"""

from random import random

def main():
    # generate a random integer. Multiplying a number in 
    # the interval [0, 1) by 6 stretches its value so it
    # lies inthe interval [0, 6). Adding 1 shifts its value 
    # so it lies in the interval [1, 7). Truncating to an 
    # integer gives values in the list 1, 2, 3, 4, 5, 6
    dice_roll = int(random() * 6 + 1)
    roll_count = 1

    while dice_roll != 6:
        print(f"We rolled a {dice_roll}")
        # Roll again, then increment our count
        dice_roll = int(random() * 6 + 1)
        roll_count += 1

    # Output how many rolls it took before we rolled a 6.
    print(f"We rolled a 6 and it took {roll_count} rolls.")

# Run the program:
if __name__ == '__main__':
    main()
```
</td>

<td>

```
We rolled a 1
We rolled a 2
We rolled a 2
We rolled a 5
We rolled a 6 and it took 5 rolls.
```
</td>
</tr>
</table>

### Example 2:
In the following example, we improve a program from a previous section. This time, we will check that each of the user's inputs is valid. If not, we use a `while`-loop to continue asking them the question until they enter something sensible.

```python
"""
A simple program that determines user eligibiity to vote
Author: COMP 1351 Instructor
Filename: voting.py
Date:
Course: COMP 1351
Assignment: Preview of nested conditional statements
Collaborators: 1351 Instructors
Internet Sources: None
"""
# Check citizenship requirement
is_citizen = input("Are you a US citizen? (Enter Y or N) ")
# Continue to ask for input until they enter either Y or N
while is_citizen != 'Y' and is_citizen != 'N':
    is_citizen = input("Invalid input. Are you a US citizen? (Enter Y or N) ")

if is_citizen == 'Y':
    # Check age requirement
    age = int(input("How old are you? "))
    # Continue to ask for input until they enter a non-negative age.
    while age < 0:
        age = int(input("Invalid age. How old are you? "))

    if age >= 18:
        # Check registration requirement
        is_registered = input("Are you registered to vote? (Enter Y or N) ")
        # Continue to ask for input until they enter either Y or N
        while is_registered != 'Y' and is_registered != 'N':
            is_registered = input("Invalid input. Are you registered to vote? (Enter Y or N) ")

        if is_registered == 'Y':
            print("You can go ahead and vote.")
        else:
            # Cannot vote because unregistered
            print("You must be registered to vote.")
    else:
        # Cannot vote due to age
        print("You must be 18 years or older to vote.")
else:
    # cannot vote due to citizenship
    print("You must be a US citizen to vote.")
```
