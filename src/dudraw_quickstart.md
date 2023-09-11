# Introduction to `dudraw`

## What can you do with `dudraw`?
The Python package `dudraw` is a minimal graphics library developed for teaching a beginning Python programming class. Its starting point was `stddraw`, developed at Princeton University (see [Elements of Programming in Python](https://introcs.cs.princeton.edu/python/code/index.php#programs)). At the University of Denver we modified and enhanced that package to produce `dudraw`.

The `dudraw` package has graphics primitives for drawing points, lines, circles and ellipses, squares and rectangles, triangles, quadrilaterals, polygons, circular and elliptical sectors, annuli and text. You can set the color you want the objects to be, and the width of points, lines and outlines.

You can find out about key-clicks and mouse presses from the user, and respond to them within your program. You can clear the background or use an image from a file as your background. You can save the image you produce to a file.

The `dudraw` package is a paint-style graphics package. In other words, you draw graphical objects, but they cannot be moved or deleted after being drawn.

## How do I get access to `dudraw`?
First make sure that you have followed all the installation steps on the [Python, VSCode, and dudraw Installation](installation.md) page. If you've successfully completed these steps then by starting your Python program with the line

`import dudraw`

you will be able to call any of the functions in `dudraw`.

If you were unable to install `dudraw` with the normal installation instructions, please reach out to a teacher or TA for help and they will have you attempt to install `dudraw` using the command line for your operating system and some command like:

`pip install dudraw`

Again, please ask for help if you're having trouble installing `dudraw`.

## How do I use `dudraw`?

Begin by creating a canvas of a specified size (in pixels), then issue graphics commands. When you are done, call the `show()`function and a window will appear with the image you have created. The parameter to the `show()` function is the number of milliseconds to display the image.  Unless you set the scale, the default scale is from 0 to 1 on the x-axis and 0 to 1 on the y-axis. Here's a simple program, and the image it produces.

```python
{{#include programs/dudraw_quickstart/mountain_and_sun.py}}
```

![Simple Drawing of mountain and sun](img/dudraw_quickstart/mountain.png)

## How do I get more colors?
This is a list of the colors pre-defined in dudraw:

```python
dudraw.WHITE
dudraw.BLACK
dudraw.RED
dudraw.GREEN
dudraw.BLUE
dudraw.CYAN
dudraw.MAGENTA
dudraw.YELLOW
dudraw.DARK_RED
dudraw.DARK_GREEN
dudraw.DARK_BLUE
dudraw.GRAY
dudraw.LIGHT_GRAY
dudraw.ORANGE
dudraw.VIOLET
dudraw.PINK
dudraw.BOOK_BLUE
dudraw.BOOK_LIGHT_BLUE
dudraw.BOOK_RED
```

To create colors of your own, first note that a color on a computer monitor can be defined by an intensity for red light, green light and blue light, each of which is an integer value from 0 to 255. Colors on a compter monitor are additive like light, rather than subtractive like paint. For example, to create yellow light, you add together green light and red light. So the brightest yellow is defined by red=255, green = 255, blue = 0. You can play around with choosing colors with many different programs. On many browsers, if you do an internet search on "color picker" one will show up. Or there are many free ones available on websites, for example here: [color picker website](https://htmlcolorcodes.com/color-picker/).
For example, here's a nice plum color, with values r = 140, g = 40, b = 160:

<img src="img/dudraw_quickstart/plum_color.png" alt="a swatch with a plum color" width="75"/>

Here's a way to make your background this color, or to set your pen color to this color:

```python
dudraw.clear_rgb(140, 40, 160)
dudraw.set_pen_color_rgb(140, 40,160)
```

## May I see some other shapes?

The code below shows some examples of lines and basic shapes that are affected by the pen radius.

```python
{{#include programs/dudraw_quickstart/basic_shapes.py}}
```

![basic shapes](img/dudraw_quickstart/basic_shapes.png)

These are not the only shapes affected by the pen width setting. Others include `dudraw.circle()`, `dudraw.square()`, `dudraw.polygon()`, `dudraw.triangle()`, `dudraw.arc()`, `dudraw.elliptical_sector()`, and `dudraw.annulus()`.

There are also `dudraw` primitives that produce filled regions rather than outlines, and these are not affected by the pen width. Here's a program with some examples of filled regions.

```python
{{#include programs/dudraw_quickstart/basic_filled_shapes.py}}
```

![filled basic shapes](img/dudraw_quickstart/filled_basic_shapes.png)

These are not the only filled shapes. Other examples include `dudraw.filled_triangle()`, dudraw.`filled_circle()`, `dudraw.filled_polygon()`, and `dudraw.filled_annulus()`.

## How do I change the scale?
By default, the scale in a dudraw canvas is [0, 1] x [0, 1], even if the size of the canvas itself is not square. For example, the code below produces the image shown. (The image is annotated to show the coordinates of a few points)

```python
{{#include programs/dudraw_quickstart/stretched_simple.py}}
```

<img src="img/dudraw_quickstart/stretched_simple.png" alt="annotated simple drawing default scale" width="400"/>

But sometimes you might prefer to set the scale to match the pixels, or some other scaling. This is often useful if the canvas is not square. Here's the code to produce a nearly identical drawing, with the scale on the x-axis and y-axis set to be different from each other, and to have one unit be the size of one pixel. The canvas was created with a width of 600 pixels and a height of 400 pixels. The x-scale is set to go from 0 to 600, while the y-scale is set to go from 0 to 400. Notice that each graphics primitive was modified to reflect the change of scale. The image below is annoted to show how the scale on the axes works.

```python
{{#include programs/dudraw_quickstart/scaled_annotated_simple.py}}
```

<img src="img/dudraw_quickstart/scaled_annotated_simple.png" alt="annotated simple drawing pixel scale" width="400"/>

When you create a drawing, the first thing you should do is decide on your scale, since that is the basis for all of the numbers in each shape you draw.

## How do I change the font and the size of text?

To change the font, use the method `dudraw.set_font_family("FontName")`.
To change the size of the font, use `dudraw.set_font_size(size)`.
The size is in points. The default font family is Helvetica, and the default size is 12 points Here is demo code and the resulting image:

```python
{{#include programs/dudraw_quickstart/text_demo.py}}

```

<img src="img/dudraw_quickstart/text_demo.png" alt="sample of fonts and sizes" width="500"/>


## How do I create an animation?

Animation is usually created with a while loop. The following template shows what usually goes in the body of the while loop:
* clear the background
* redraw the next frame of the animation
* call `dudraw.show(wait_time)`

When you pass a parameter to `dudraw.show()`, the program pauses for the given wait_time, which is a `float` value giving the time in milliseconds.

Here is sample code that animates a circle appearing to move from the lower left corner of the canvas to the upper right corner:

```python
{{#include programs/dudraw_quickstart/simple_animation.py}}
```

## How do I found out if the user clicked the mouse?

There are three `dudraw` methods for handling mouse ineraction
The function `dudraw.mouse_is_pressed()` returns a boolean, True if the mouse was pressed. It is typically used within an animation loop.
You can find out the position of the mouse (regardless of whether the mouse is pressed) by calling `dudraw.mouse_x()` and `dudraw.mouse_y()`. Each returns a float with the current position of the mouse. The position of the mouse is relative to the scale that has been set. Here's a sample program showing mouse interaction. Each time the mouse is pressed, a small circle on the canvas at the mouse position.

```python
{{#include programs/dudraw_quickstart/mouse_press_demo.py}}
```

## How do I find out if the user typed a key?

Polling for a key click typically happens within an animation loop. You must first call `dudraw.has_next_key_typed()`, which returns a boolean indicating whether the user has typed a key (or perhaps more than one). If the method returns `True`, then you can make a call to `dudraw.next_key_typed()`, which will return a string containing the next most-recently entered key. As an example, the following code is a modification of the mouse interaction code, with the added feature of quiting when the 'q' key is typed:

```python
{{#include programs/dudraw_quickstart/mouse_and_key_demo.py}}
```

## How do I save my image in a file?

   Use the `dudraw.save()` function. You can output either .png files or .jpg files. The extension you use in the file name determines what file type is output.
   Here's an example of a program that draws a very simple picture, and saves the output to two files, one .png and one .jpg:

```python
{{#include programs/dudraw_quickstart/save_image.py}}
```

Notice that this program does not have a call to `dudraw.show()`. This means that, although the image is saved to both files, a window displaying the image is never opened, and the image is not displayed to the screen.

## How do I get official details on all of the functions?

See here for the official documentation:

[https://cs.du.edu/~intropython/dudraw/](https://cs.du.edu/~intropython/dudraw/)

And here for the source code:

[https://git.cs.du.edu/dudraw/dudraw](https://git.cs.du.edu/dudraw/dudraw)
