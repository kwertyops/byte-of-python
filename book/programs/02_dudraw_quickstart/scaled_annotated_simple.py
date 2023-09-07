import dudraw

dudraw.set_canvas_size(600, 400)
dudraw.set_x_scale(0, 600)
dudraw.set_y_scale(0, 400)
dudraw.clear(dudraw.LIGHT_GRAY)
dudraw.set_pen_color(dudraw.DARK_GREEN)
dudraw.filled_triangle(0, 0, 600, 0, 300, 280)  # green triangle mountain
dudraw.set_pen_color(dudraw.YELLOW)    
dudraw.filled_circle(480, 300, 40)              # yellow circle sun
dudraw.show()