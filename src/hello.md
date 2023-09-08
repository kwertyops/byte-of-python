# Your first python program.
It is traditional in Computer Science for your first program in any language to output the phrase "Hello, world!" to the console. This is a way of checking that your IDE (Integrated Development Environment) is working completely.
In python, the bare-bones "Hello, world!" program is just one line. Our version will be longer, to illustrate some other important programming practices.

In the VSCode application, open the browswer window and create a new file called `hello.py`. It's important that the name you choose ends with `.py`, so that your IDE knows to interpret your file as a python program. Paste the following:
```python
"""
First python program, that outputs "Hello, world!"
File Name: hello.py
Date: 
Course: COMP1351
Assignment: first python program
Collaborators: 1351 Instructors
Internet Sources: None
"""

def main():
    # Here's the guts of the program, just one line:
    print("Hello, world!")

# Run the program:
if __name__ == '__main__':
    main()
```
Key points to notice and remember:
- Use the `print()` function to output to the console. Put the text you want to output inside of the parentheses. Text in python (called a *string literal*) is enclosed either within double quotes ("text") or single quotes ('text').
- *Comments* in a computer program are lines that python itself ignores. Comments are there for the benefit of humans (including your future self) reading your program. There are two kinds of comments in python: *block comments* and *in-line comments*. 
- You can see that the first 9 lines of this program is a block comment, since it is enclosed between lines of three double-quotes. Every python program that you turn in this quarter will start with a block comment giving your name, the purpose of the program, the name of the file it is stored in, the date, the course it is for, the assignment it is fulfilling, your collaborators, and any internet sources you used.
- An inline comment starts with a `#`-sign. Anything on the line after a `#` is a comment that python ignores. Placing in-line comments in your code to explain your thought process while writing the code is an essential part of writing good code. Write the comments either before or during the coding process, **not after**.
- The lines
    ```python
    def main():
        # Here's the guts of the program, just one line:
        print("Hello, world!")
    ```
    define the main function of the program. This function has one comment, and one line of executable code.
- At the end of the program, the lines
    ```python
    if __name__ == '__main__':
        main()
    ```
    have the effect of *calling* (also called *invoking* or *executing*) the main function. Notice that the definition of the         function itself (`def main()`) has the line `print("Hello, world!")`. But that line doesn't get executed until the `main()`       function itself is called.
