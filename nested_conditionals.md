## Nested conditional statements

Recall that an ordinary `if-else` statement has this syntax:

```python
if <condition>:
    # Indented statement block
else:
    # Indented statement block
```

It is possible for the indented statement blocks themselves to include *another* `if` or `if-else` statement. This is called *nesting*, and it is both useful and common. Nesting might look like this (another `if/else` within the outer `if` block):

```python
if <condition 1>:
    if <condition 2>:
        # Indented statement block
    else:
        # Indented statement block
else:
    # Indented statement block
```

or like this (another `if/else` within each of the outer `if` and the outer `else` blocks):
```python
if <condition 1>:
    if <condition 2>:
        # Indented statement block
    else:
        # Indented statement block
else:
    if <condition 3>:
        # Indented statement block
    else:
        # Indented statement block
```

or even like this: (an `if/else` within the outer `if`, then another `if/else` within the inner `if`)
```python
if <condition 1>:
    if <condition 2>:
        if <condition 3>:
            # Indented statement block
        else:
            # Indented statement block
    else:
        # Indented statement block
else:
    # Indented statement block
```

Notice that the last two cases each have three `if` conditions, but they are very different from each other. The last one has three levels of nesting, while the previous one has only two levels.  In python, we always pay close attention to the indentation, because it tells us which inner block is part of which outer block. That placement controls the logical flow of the program. An inner block only gets executed if the condition for its outer block evaluates to `True`.

## Examples of nested conditionals

<table>
<tr>
<td>Code</td><td>Output</td><td>Notes</td>
</tr>
<tr>
<td nowrap>

```python
x = 5
y = 7
z = 10

if x < y:
    print("A")
    if z >= 20:
        print("B")
    else:
        print("C")
else:
    print("D")
```
</td>
<td>

```
A
C
```
</td>
<td>

The condition for the outer `if` is `True` (`x < y`), so the outer `if` block is executed and
`"A"` is output. Next, the inner condition is checked. But `z >= 20` is `False`, so the `else`
block of the inner `if-else` is executed, and `"C"` is output.
</td>
<tr>
<td nowrap>

```python
x = 5
y = 7
z = 50

if x < y:
    print("A")
    if z >= 20:
        print("B")
    else:
        print("C")
else:
    print("D")
```
</td>
<td>

```
A
B
```
</td>
</td>
<td>

The condition for the outer `if` is `True` (`x < y`), so the outer `if` block is executed and
`"A"` is output. Next, the inner condition is checked. Now `z >= 20` is `True`, so the `if`
block of the inner `if-else` is executed, and `"B"` is output.
</td>
</tr>
<tr>
<td nowrap>

```python
x = 5
y = 1
z = 50

if x < y:
    print("A")
    if z >= 20:
        print("B")
    else:
        print("C")
else:
    print("D")
```
</td>
<td>

```
D
```
</td>
</td>
<td>

The condition for the outer `if` is `False`, so the outer `else` block is executed and `"D"` is output.
</td>
</tr>
<td nowrap>

```python
x = 5
y = 1
z = 50

if x < y:
    print("A")
    if z >= 20:
        print("B")
    else:
        print("C")
else:
    print("D")
    if x % 2 == 0:
        print("E")
    else:
        print("F")
```
</td>
<td>

```
D
F
```
</td>
</td>
<td>

The condition for the outer `if` is `False`, so the outer `else` block is executed and
`"D"` is output. Next, the inner condition is checked. And `x % 2 == 0` is `False` (since `x` is odd), so the `else`
block of the inner `if-else` is executed, and `"F"` is output.
</td>
<tr>



</table>

Exercise: For the last code block in the above examples, can you come up with initial values for `x`, `y`, and `z` so that the output is `D E`? Can you come up with initial values for `x`, `y`, and `z` so that the output is `A F`?

## Putting it all together

The code below on the left checks if the user can vote in an upcoming election. It checks that the user is a US citizen, is 18 or over, and has registered to vote. The flowchart on the right shows the flow of control through the program, as it checks the three conditions.

<table>
<tr>
<td>Code</td>
<td>Flowchart</td>
</tr>
<tr>
<td nowrap>

```python
"""
A simple program that determines uer elifibiity to vote
Author: COMP 1351 Instructor
Filename: voting.py
Date:
Course: COMP 1351
Assignment: Preview of nested conditional statements
Collaborators: 1351 Instructors
Internet Sources: None
"""
# Check citizenship requirement
is_citizen = input("Are you a US citizen? Y for yes, N for no. ")
if is_citizen == 'Y':
    # Check age requirement
    age = int(input("How old are you? "))
    if age >= 18:
        # Check registration requirement
        is_registered = input("Are you registered to vote? Y for yes, N for no. ")
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
</td>
<td>
<figure>
<img src="img/voting_flowchart.png" alt="Flowchart for the voting program" class="center", width="300">
</figure>
</td>
</table>

Key points:
- Notice that this program has three levels of nesting.
- Notice that if the user enters `N` to the first question, then no further questions are asked. Similarly, if they are too young, they are not asked the last question. This is accomplished using the structure of the `if-else` nesting.
- The indentation is vital. Look at the code above and carefully notice how each `if` lines up directly above the `else` that pairs with it. 
- Copy/paste the above program into VSCode and run it. To test completely, you have to try all possible combinations of inputs, so that every possible line of code in the program gets tested. This means running the program multiple times and entering multiple possibilities at each input line. What happens if the user enters `P` instead of `Y` or `N`? Why?