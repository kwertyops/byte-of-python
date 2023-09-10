#--------------------------------
# demo of mouse presses in dudraw
#--------------------------------
import dudraw

dudraw.set_canvas_size(500,500)

# animation loop
while True:
    # when mouse is pressed, draw a circle of radius 0.02 at the mouse location
    if dudraw.mouse_is_pressed():
        dudraw.filled_circle(dudraw.mouse_x(), dudraw.mouse_y(), 0.02)
    # pause for 200th of a second
    dudraw.show(50)