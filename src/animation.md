## Animations using `dudraw`

Animation is usually created with a `while`-loop. The following template shows what usually goes in the body of the loop:
* clear the background
* redraw the next frame of the animation
* call `dudraw.show(wait_time)`

When you pass a parameter to `dudraw.show()`, the program pauses for the given wait_time, which is a `float` value giving the time in milliseconds.

Here is sample code that animates a circle appearing to move from the lower left corner of the canvas to the upper right corner:

<table>
<tr><td>Code</td><td>Animation</td></tr>
<tr>
<td nowrap style="display:inline-block; width:400px;">

```python
""" Demo showing a simple animation,
    A circle moves diagonally across the canvas
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

    # animation loop (loop forever - we'll update this later):
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

There are three `dudraw` methods for handling mouse interaction:
- `dudraw.mouse_is_pressed()`
- `dudraw.mouse_x()`
- `dudraw.mouse_y()`

The function `dudraw.mouse_is_pressed()` returns a boolean, `True` if the mouse is pressed at the moment when the function is called. It is typically used within an animation loop.
You can find out the position of the mouse (regardless of whether the mouse is pressed) by calling `dudraw.mouse_x()` and `dudraw.mouse_y()`. Each returns a `float` with the current position of the mouse. The position of the mouse is given relative to the scale that has been set. Here's a sample program showing mouse interaction. Each time the mouse is pressed, a small circle is drawn on the canvas at the current mouse position. This program does not repeatedly clear the screen in the animation loop, so the circles drawn remain there as further circles are added. Finally, note that the cal to `dudraw.mouse_is_pressed()`, must occur within an animation loop, otherwise the user would be unlikely for the user to happen to press the mouse at the exact moment that one call to `dudraw.mouse_is_pressed()` is executing.

<table>
<tr><td>Code</td><td>Animation</td></tr>
<tr>
<td nowrap style="display:inline-block; width:400px;">

```python
""" Demo showing how to detect mouse presses
    This happens by calling dudraw.mouse_is_pressed()
    within an animation loop
    File Name: simple_animation.py
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
        # when mouse is pressed, draw a circle of radius 0.02 at the mouse location
        if dudraw.mouse_is_pressed():
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

As with mouse presses, polling for a key click typically happens within an animation loop. You must first call `dudraw.has_next_key_typed()`, which returns a boolean indicating whether the user has typed a key (or perhaps more than one). If the method returns `True`, then you can make a call to `dudraw.next_key_typed()`, which will return a string containing the next most-recently entered key. As an example, the following code is a modification of the mouse interaction code, with the added feature of quitting when the `'q'` key is typed:

```python
""" Demo showing how to detect key clicks
    This happens by, within an animation loop,
    calling dudraw.has_next_key_typed() and
    then if it returns True, then dudraw.next_key_typed()
    File Name: simple_animation.py
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
        # when mouse is pressed, draw a circle of radius 0.02 at the mouse location
        if dudraw.mouse_is_pressed():
            dudraw.filled_circle(dudraw.mouse_x(), dudraw.mouse_y(), 0.02)
        # pause for one 20th of a second
        dudraw.show(50)
        if dudraw.has_next_key_typed() and dudraw.next_key_typed()=='q':
            done = True


# Run the program:
if __name__ == '__main__':
    main()
```

