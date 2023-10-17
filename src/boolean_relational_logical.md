## Boolean variables
In order to control the flow of a program, we will need a new type of value and variable called a boolean. In python the name of the type is `bool`. Boolean variables can only have two possible values: `True` or `False`.

Boolean variables are used much like other variables in python. For example, when creating an animated (moving) drawing in `dudraw`, we may want a variable called `is_moving` to keep track of whether one of our objects is continuing to move. Here is some code that would create and access that variable:

<table>
<tr>
<th> Code </th>
<th> Output </th>
</tr>
<tr>
<td nowrap>

```python
is_moving = True
print(is_moving)
print(type(is_moving))
```
</td>
<td>

```
True
<class 'bool'>
```
</td>


</tr>
</table>

## Relational operators
Relational operators can be used to compare two values to produce a boolean (`True` or `False`) result.

|Relational operator|What it does| Example (x=4, y=8)|
|:-:|:-:|:-:|
|`==`|`True` if the two sides are **equal**, `False` otherwise|`x==y`&rarr;`False`|
|`!=`|`True` if the two sides are **not equal**, `False` otherwise|`x!=y`&rarr;`True`|
|`>`|`True` if the left side is **greater than**  the right side, `False` otherwise|`x>y`&rarr;`False`|
|`<`|`True` if the left side is **less than**  the right side, `False` otherwise|`x<y`&rarr;`True`|
|`>=`|`True` if the left side is **greater than or equal to** the right side, `False` otherwise|`x>=y`&rarr;`False`|
|`<=`|`True` if the left side is **less than or equal to** the right side, `False` otherwise|`x<=y`&rarr;`True`|

## Boolean Expressions

A *Boolean expression* is an expression that evaluates to either `True` or `False`.

Examples: Suppose the following code has executed:

```python
x = 5
y = 3
z = 10
g = 2
```
Evaluate the following boolean expressions:

|Boolean expression...|...evaluates to:|
|:-:|:-:|
|`x * g == z` | `True`|
|`2 + y > z` | `False`|
|`x - z >= g`| `False`|
|`x * g <= z` | `True`|

## Logical Operators
Logical operators are used to construct more complicated boolean expressions from simpler boolean expressions.
The three logical operators we will use in python are `not`, `and`, and `or`.
<table>
<tr>
<td>Logical operator</td>
<td>What it does</td>
<td> 

Example (`x = True, y = False`)

</td>
</tr>
<tr>
<td>

`not`
</td>
<td>

Negate the value - meaning a `True` boolean expression becomes `False` and a `False` boolean expression becomes true.</td>
<td>


`not x` &rarr; `False`

`not y` &rarr; `True`
</td>
</tr>
<tr>
<td>

`and`
</td>
<td>

`True` **only if both boolean expressions are true**, otherwise `False`.

"I completed homework **and** read a book", evaluates to `True` only if you have done **both**.
</td>
<td>

`x and y` &rarr; `False`

`x and (not y)` &rarr; `True`
</td>
</tr>
<tr>
<td>

`or`
</td>
<td>

`True` **if either boolean expression is true**, otherwise `False`.

"I completed homework **or** read a book" evaluates as `True` if you have done one or the other or both.
</td>

<td>

`x or y` &rarr; `True`

`(not x) or y` &rarr; `False`

`x or (not y)` &rarr; `True`
</td>
</tr>
</table>

Note that in the English language, sometimes people use the word "or" to mean one or the other but *not* both. That is an alternate meaning that in Computer Science and mathematics is called *exclusive or*. But in programming and in mathematics, `or` **always** means *one or the other or both*.

## Precedence of Logical Operators

The order of precedence for logical operators is
- `not`, then
- `and`, then
- `or`.

Just like in arithmetic, the order of precedence can be overridden with parentheses.
Sometimes people forget whether `and` or `or` has higher precedence. So you are urged to use parentheses in logical expressions even if they are not required, to avoid ambiguity and to improve the clarity of your code to others who read it.

Examples:
Suppose the following code has executed:
```python
x = 5
y = 3
z = 10
g = 2
```
Evaluate the following boolean expressions:

|Boolean expression...|...evaluates to:|
|:-:|:-:|
|`x * g == z or not (x * x < y)` | `True`|
|`(2 * y < z and z <= g) or x != 5` | `False`|
|`not (x == 7)`|`True`|

Note: In the above examples, none of the parentheses are required, but they improve readability of the code.

Note: In the last example `not (x == 7)` is equivalent to `x != 7 `.
