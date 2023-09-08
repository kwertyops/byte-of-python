# Simple demo program of animation
# Animate a circle moving diagonally across the canvas
import dudraw

# (x, y) is the position of the center of the circle
x = 0 
y = 0 

# animation loop:
while True:
    # clear the background to prepare for the next frame
    dudraw.clear(dudraw.GRAY)
    # Update circle to the new position.
    x = x + 0.01
    y = y + 0.01
    # Draw circle at curent position, radius is a constant 0.05
    dudraw.filled_circle(x, y, 0.05)
    # Display the next frame, and pause 20 milliseconds
    dudraw.show(20)