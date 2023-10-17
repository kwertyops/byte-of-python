## Loops and conditional statements can be nested

`for`-loops can be nested within conditional statements, and conditional statements can be nested within loops.


## `for`-loops within conditional statements

Here is the structure of a `for`-loop nested within an `if`-statement:
```python
if <condition>:
    for i in range(...):
        # indented code block
```
In this case, the loop executes if the condition evaluates to `True`, otherwise it is skipped.

Another possibility is `for`-loops nested within an `if-else` statement:
```python
if <condition>:
    for i in range(...):
        # indented code block
else <condition>:
    for i in range(...):
        # indented code block
```

Examples: Trace the following code examples, confirming the output.
<table>
<tr>
<td>Code</td><td>Output</td><td>Notes</td>
</tr>
<tr>
<td nowrap >

```python
a = 5
b = 1

if a > b:
    for i in range(5):
        print("a")
else:
    for i in range(5):
        print("b")
```
</td>
<td>

```
a
a
a
a
a
```
</td>
<td> 

The condition `a>b` evaluates to `True`, so the `for`-loop within the `if` block is executed. Five `"a"`s are output.
</tr>
<td nowrap >

```python
a = 5
b = 10

if a > b:
    for i in range(5):
        print("a")
else:
    for i in range(5):
        print("b")
```
</td>
<td>

```
b
b
b
b
b
```
</td>
<td> 

The condition `a>b` evaluates to `False` this time, so the `for`-loop within the `else` block is executed. Five `"b"`s are output.
</table>

## Conditional statements within `for`-loops

Here is the structure of an `if` statement nested within a `for`-loop:

```python
for i in range(...):
    if <condition>:
        # indented code block
```

In this case, the condition is checked newly on *each iteration* of the loop. In some of the iterations it may evaluate `True`, and then in others it may be `False`. The check is done independently each time.  The indented code block only executes on the iterations where the condition comes out to be `True`.

Of course, inside the `for`-loop we may instead have an `if-else` statement or an `if-else` ladder.

Examples: trace the following code examples, confirming the output.

<table>
<tr>
<td>Code</td><td>Output</td><td>Notes</td>
</tr>
<tr>
<td nowrap >

```python
for i in range(8):
    if i % 2 == 0:
            print(i)
```
</td>
<td>

```
0
2
4
6
```
</td>
<td>

Each time through the loop, the variable `i` will take the next value from the sequence `0, 1, 2, 3, 4, 5, 6, 7`. Each time, the `if` statement checks if `i % 2 == 0`, in other words, if `i` is even. Each time that condition is `True`, the value is output, resulting in `0 2 4 6`.
</td>
</tr>
</table>

## Putting it all together

Here's a complete program that uses an `if-else` statement nested within a `for`-loop. Carefully trace the program and predict the image that results. You can run the code to test if you were correct.

```python
"""
Produce a drawing of randomly-placed circles in two colors
Mystery output: Trace the code to find out. Run it to check.
Author: COMP 1351 Instructor
Date:
File: two_colors.py
Course: COMP 1351
Assignment: Preview assignment for for-loops
Collaborators: 1351 Instructors
Internet Sources: None
"""

import dudraw
from random import random

dudraw.set_canvas_size(500, 500)
dudraw.clear(dudraw.LIGHT_GRAY)

for i in range(10000):
    # generate random x and y locations:
    x = random()
    y = random()
    # set color based on position
    if y > 0.5:
        # Magenta is a hot-pink color
        dudraw.set_pen_color(dudraw.MAGENTA)
    else:
        # Cyan is a turquoise color
        dudraw.set_pen_color(dudraw.CYAN)

    # draw the circle at the randomly-chosen location:
    dudraw.filled_circle(x, y, 0.01)
    # outline the circle with a black edge:
    dudraw.set_pen_color(dudraw.BLACK)
    dudraw.circle(x, y, 0.01)

# display the final image until the window is closed
dudraw.show(float('inf'))
```