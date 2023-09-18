## Generating random numbers

Often when programming we would like to use random numbers. For example, if we want to put a circle on a `dudraw` canvas at a random location, then for the `(x, y)` location we would use two random numbers of type `float`, chosen between `0` and `1`. Or perhaps we want to write a program to play a guessing game where the user has to guess a number from `1` to `100`, so we would need to generate an integer in that range.

Note that on a computer, there is no such thing as a true random number, since the processes on a computer are deterministic. However, randomness can be simulated using complex mathematical functions. Numbers generated this way are called *pseudorandom numbers*.

## Generating random `float` values

Begin by importing the `random` package. Then use the `random()` function from that package to generate a (pseudo)random `float` in the interval `[0,1)`. For example:

```python
import random

def main():
    print(random.random())

# Run the program:
if __name__ == '__main__':
    main()
```
gives the following possible output (of course when you run it, a different number will be generated, since the number produced is random).

```
0.9654798677156062
```

A note about `import`: it is possible to import just a single function from a package rather than the entire package. If you do this, then you can refer to the function by its name `function_name`, rather than `package_name.function_name`. The following code is functionally identical to the example above:

```python
from random import random

def main():
    print(random())

# Run the program:
if __name__ == '__main__':
    main()
```

## Generating `float` values within an interval

Use the `random.uniform()` function if you want a random `float`, but not necessarily from the interval `[0,1)`. For example,

```python
import random

def main():
    print(random.uniform(2, 5))

# Run the program:
if __name__ == '__main__':
    main()
```
outputs a random decimal number in the range `[2, 5)`, such as
```
2.7178618144891766
```

## Generating random `int` values

One way to generate random integer values is to use the `randint()` function from the `random` package. The parameters are the lower bound and the upper bound you want for the integers. Unlike other functions in python, the stop value **is** included in the possible outcomes. For example:

```python
    print(random.randint(2, 5))
```
will output one of `2`, `3`, `4`, or `5`.

## Putting it all together

The example below draws a circle at a random location on a `1x1` `dudraw` canvas, with a radius from `0.05` to `0.1` and with a random color. A possible output image is shown.

<table>
<tr>
<td>Code demonstrating use of random `float` and `int` numbers </td>
<td>Image</td>
</tr>
<tr>
<td nowrap>

```python
import random
import dudraw


def main():
    # Set up the canvas, 400x400 pixels
    dudraw.set_canvas_size(400,400)
    # Background light gray
    dudraw.clear(dudraw.LIGHT_GRAY)
    # Pick two random values from the interval [0,1]
    # for the center of the circle.
    x_center = random.random()
    y_center = random.random()
    # Random from 0.05 up to 0.1 for the radius
    radius = random.uniform(0.05, 0.1)
    # three values from 0-255 (inclusive) for the rgb color
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    # Set pen color then draw the circle
    dudraw.set_pen_color_rgb(red, green, blue)
    dudraw.filled_circle(x_center, y_center, radius)
    # Display the result for 10 seconds
    dudraw.show(10000)

# Run the program:
if __name__ == '__main__':
    main()
```


</td>
<td>

<figure>
<img src="img/random_numbers/random_circle.jpg" alt="randomly sized circle, random location, random colors class="center", width="300">
</figure>

</td>
</tr>

</table>




