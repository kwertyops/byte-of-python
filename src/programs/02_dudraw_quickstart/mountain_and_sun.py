import dudraw

# open a square window, parameters are width and height, in pixels
dudraw.set_canvas_size(200,200)

# fill the canvas with the given color
dudraw.clear(dudraw.LIGHT_GRAY)

# once the pen color is set, that is the color used until it is changed again
dudraw.set_pen_color(dudraw.DARK_GREEN)

# draw a triangle with vertices (0, 0), (1, 0) and (0.5, 0.7)
dudraw.filled_triangle(0, 0, 1, 0, 0.5, 0.7)
dudraw.set_pen_color(dudraw.YELLOW)

# Draw a circle with center at (0.8, 0.75), with a radius of 0.1
dudraw.filled_circle(0.8, 0.75, 0.1)

# Display the canvas
dudraw.show()