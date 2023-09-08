#-------------------------------------------------
# demo of mouse presses and key presses in dudraw
#-------------------------------------------------
import dudraw

dudraw.set_canvas_size(500,500)
done = False

# animation loop
while not done:
    # when mouse is pressed, draw a circle of radius 0.02 at the mouse location
    if dudraw.mouse_pressed():
        dudraw.filled_circle(dudraw.mouse_x(), dudraw.mouse_y(), 0.02)
    # pause for 200th of a second
    dudraw.show(50)
    if dudraw.has_next_key_typed() and dudraw.next_key_typed()=='q':
        done = True