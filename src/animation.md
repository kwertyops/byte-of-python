## Animations using `dudraw`

Animations are usually created with `while`-loops. The following template shows what usually goes in the body of the loop:
* clear the background
* redraw the next frame of the animation
* call `dudraw.show(wait_time)`

When you pass a parameter to `dudraw.show()`, the program pauses for the given `wait_time``, which is a `float` value giving the time in milliseconds.

Here is sample code that animates a circle appearing to move from the lower left corner of the canvas to the upper right corner:

<table>
<tr><td>Code</td><td>Animation</td></tr>
<tr>
<td nowrap style="display:inline-block; width:500px;">

```python
""" Demo showing a simple animation,
    A circle moves diagonally across the canvas
    File Name: simple_animation.py
    Author: COMP 1351 instructor
    Date:
    Course: COMP 1351
    Assignment: Notes on animation
    Collaborators: COMP 1351 instructors
    Internet Source: None
"""
import dudraw

def main():
    # (x, y) is the position of the center of the circle
    x_center = 0
    y_center = 0 

    # animation loop (loop forever - we'll improve this
    # in a later example):
    while True:
        # clear the background (erase previous frame) to prepare
        # for the next frame
        dudraw.clear(dudraw.LIGHT_GRAY)
        # Update circle to the new position.
        x = x + 0.01
        y = y + 0.01
        # Redraw circle at curent position, radius is constant, 0.05
        dudraw.filled_circle(x, y, 0.05)
        # Display the next frame, and pause 20 milliseconds
        dudraw.show(40)

# Run the program:
if __name__ == '__main__':
    main()
```
</td>
<td>

<video width="400" height = "400" controls style="margin: 5px auto;">
    <source src="img/animation/moving_circle.mov" type="video/mp4">
</video>
</td
</tr>
</table>



## How do I find out if the user clicked the mouse?

Here are three `dudraw` methods for handling mouse interaction (see documentation for other options)
- `dudraw.mouse_clicked()`
- `dudraw.mouse_x()`
- `dudraw.mouse_y()`

The function `dudraw.mouse_clicked()` returns a boolean, `True` if there is an unprocessed mouse click. It is typically used within an animation loop.
You can find out the position of the mouse (regardless of whether the mouse is pressed) by calling `dudraw.mouse_x()` and `dudraw.mouse_y()`. Each returns a `float` with the current position of the mouse. The position of the mouse is given relative to the scale that has been set. Here's a sample program showing mouse interaction. Each time the mouse is clicked, a small circle is drawn on the canvas at the current mouse position. This program does not repeatedly clear the screen in the animation loop, so the circles drawn remain there as further circles are added.

<table>
<tr><td>Code</td><td>Animation</td></tr>
<tr>
<td nowrap style="display:inline-block; width:500px;">

```python
""" Demo showing how to detect mouse clicks
    This happens by calling dudraw.mouse_clicked()
    within an animation loop
    File Name: mouse_click_processing.py
    Author: COMP 1351 instructor
    Date:
    Course: COMP 1351
    Assignment: Notes on animation, key presses
    Collaborators: COMP 1351 instructors
    Internet Source: None
"""
import dudraw

def main():
    dudraw.set_canvas_size(500,500)

    # animation loop
    while True:
        # when mouse is clicked, draw a circle of radius 0.02 at the mouse location
        if dudraw.mouse_clicked():
            dudraw.filled_circle(dudraw.mouse_x(), dudraw.mouse_y(), 0.02)
        # pause for 200th of a second
        dudraw.show(50)


# Run the program:
if __name__ == '__main__':
    main()
```
</td>
<td>

<video width="400" height = "400" controls style="margin: 5px auto;">
    <source src="img/animation/mouse_clicks.mov" type="video/mp4">
</video>
</td
</tr>
</table>



## How do I find out if the user typed a key?

As with mouse clicks, polling for a key click typically happens within an animation loop. Use the function `dudraw.next_key()`, which will return a string containing the next most-recently entered key. If no key has been pressed, the function returns an empty string. As an example, the following code is a modification of the mouse interaction code, with the added feature of terminating (quitting) the program when the `'q'` key is typed:

```python
""" Demo showing how to detect key presses
    This happens within an animation loop,
    by calling dudraw.next_key()
    File Name: detect_key_presses.py
    Author: COMP 1351 instructor
    Date:
    Course: COMP 1351
    Assignment: Notes on animation, key presses
    Collaborators: COMP 1351 instructors
    Internet Source: None
"""
import dudraw

def main():
    dudraw.set_canvas_size(500,500)
    done = False

    # animation loop
    while not done:
        # when mouse is clicked, draw a circle of radius 0.02 at the mouse location
        if dudraw.mouse_clicked():
            dudraw.filled_circle(dudraw.mouse_x(), dudraw.mouse_y(), 0.02)
        # pause for one 20th of a second
        dudraw.show(50)
        # detect key presses, look for 'q' to quit program
        if dudraw.next_key()=='q':
            done = True


# Run the program:
if __name__ == '__main__':
    main()
```

In the above example, if you would like to accept either an upper-case or lower-case letter, here is one option for checking the condition:
```python
        # find out the next key pressed
        key = dudraw.next_key()
        # then check to see if it is either a lowercase q or an uppercase Q
        if key == 'q' or key == 'Q':
            done = True
```

Here is another option for allowing either uppercase or lowercase:
```python
        # Get the value of the next key and immediately convert it to lowercase
        # If an uppercase 'Q' is entered, it is converted to a lowercase 'q'
        # before we check
        if dudraw.next_key().lower() == 'q'
            done = True
```
The above option uses a string method called `lower()` which converts a string to lower case. We will learn more about string manipulation in a later section.

Please note the following two common errors in using the `dudraw.next_key()` function:
- In the following INCORRECT CODE, note that on each side of the `or`, we need a full boolean expression
    ```python
            # This code is incorrect!
            # The following line is wrong!
            if dudraw.next_key() == 'q' or 'Q'
                done = True
    ```
- The error in the INCORRECT CODE below is a little subtle. Here the function `dudraw.next_key()` is mistakenly invoked twice. If a `Q` is entered, that key click is processed in the first call to `dudraw.next_key()`. You can think of it as being *used up*. So on the second call to `dudraw.next_key()`, the `Q` is gone, and there are no key presses left to check. The result is that a `q` will quit the program, but a `Q` will not.
    ```python
            # This code is incorrect!
            if dudraw.next_key() == 'q' or dudraw.next_key() == 'Q'
                done = True
    ```


