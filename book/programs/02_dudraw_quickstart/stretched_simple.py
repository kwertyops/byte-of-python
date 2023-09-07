import dudraw

dudraw.set_canvas_size(600,400)
dudraw.clear(dudraw.LIGHT_GRAY)
dudraw.set_pen_color(dudraw.DARK_GREEN)
dudraw.filled_triangle(0, 0, 1, 0, 0.5, 0.7) # green triangle mountain
dudraw.set_pen_color(dudraw.YELLOW)
dudraw.filled_circle(0.8, 0.75, 0.1)         # yellow circle sun
dudraw.show()