#----------------------------------------------------
# demonstration of some basic filled shapes in dudraw
#----------------------------------------------------
import dudraw

# open a 600x200 pixel canvas, and set the scale to one unit per pixel
dudraw.set_canvas_size(600,200)
dudraw.set_x_scale(0,600)
dudraw.set_y_scale(0,200)
dudraw.clear(dudraw.LIGHT_GRAY)

# draw a vertical line, from (10,10) to (10,100)
dudraw.line(10, 10, 10, 190)

# change the color, and change the width of the pen to 4 units (which is 4 pixels in this example).
dudraw.set_pen_color(dudraw.VIOLET)
dudraw.set_pen_width(4)
dudraw.line(30, 10, 30, 190)

# make a green filled rectangle with a thick outline
dudraw.set_pen_color(dudraw.DARK_GREEN)
dudraw.filled_rectangle(100, 100, 50, 90) # center at (100,100), half-width=50, half-height = 90

# red ellipse
dudraw.set_pen_color(dudraw.RED)
dudraw.filled_ellipse(200, 100, 30, 90) # center at (200, 100), half-width = 30, half-height = 90

# filled Blue quadrilateral
dudraw.set_pen_color(dudraw.DARK_BLUE)

# The four vertices are (250, 10), (250, 190), (300,190), (275, 10)
dudraw.filled_quadrilateral(250, 10, 250, 190, 300, 190, 275, 10) 

# Sector, notice that the color was not changed, this sector is also dark blue.
# The center is at (350, 100). The radius is 50. The last two parameters give the starting and
# ending angles, in degrees. Angles are measured as typical in mathematics,
# counter-clockwise starting at the positive x-axis
dudraw.filled_sector(350, 100, 50, 30, 330)

# points: size is controlled by the pen width, parameters are just the location of the point
# The points are left in this drawing you so can compare to the images of unfilled regions
dudraw.set_pen_color(dudraw.CYAN)
dudraw.set_pen_width(10)
dudraw.point(450, 150)
dudraw.point(500, 150)

# filled elliptical sector: give the center point, the radius in the x-direction, the radius in
# the y-direction, and the start/stop angles.
# Angles are measured as typical in mathematics, counter-clockwise starting at the positive x-axis
dudraw.set_pen_color(dudraw.PINK)
dudraw.filled_elliptical_sector(475, 150, 50, 100, 200, 340)
dudraw.show()