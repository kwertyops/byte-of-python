#-----------------------------------
# demo of saving to a file in dudraw
#-----------------------------------
import dudraw

# draw a red circle on a field of white
dudraw.set_canvas_size(300,300)
dudraw.set_pen_color(dudraw.RED)
dudraw.filled_circle(0.5, 0.5, 0.25)
dudraw.save("red_circle.jpg")