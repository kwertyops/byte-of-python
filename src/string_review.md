## Python strings (type `str`) - review

You've already learned quite a bit about strings. Here's a summary review:
- In python the string type (`str`) is used for storing text.
- You can define strings by enclosing them within either double-quotes or single-quotes.
- You can get text input from the user with the `input()` function, which returns a `str`.
    ```python
    name = input("What is your name? ")
    print(type(name)))  # outputs <class `str'>
    ```
- You can combine strings for output in multiple ways, such as
    - Pass multiple expressions to `print()`, separated by commas. In the output, a space is automatically inserted between the strings.
        ```python
        name = input('What is your name? ')
        print('Hello', name, ', I am glad to meet you!') 
        ```
        Sample output:
        ```
        What is your name? Buttercup
        Hello Buttercup , I am glad to meet you!
        ```
        Notice the unfortunate extra space before the comma!
    - Concatenate using the `+` operator. This means joining together two strings, one following the other. It gives us complete control over the spaces - you must include any needed spaces.

        ```python
        name = input("What is your name? ")
        print("Hello " + name + ", I'm glad to meet you!")
        ```
        Sample output:
        ```
        What is your name? Fezzik
        Hello Fezzik, I'm glad to meet you!
        ```

        Notice that the code above uses double quotes rather than single quotes for each of the strings. This was an intentional choice. The text `"I'm glad to meet you"` has an apostrophe in it, which is the same character as a single quote. If we try to define that string using a single quote, then python assumes we are ending the string when we reach the single quote. The problem is solved by using double-quotes. 

    -  Use an `f`-string (formatted string) to define a string that includes the value of expression(s). Put each expression with a pair of curly braces `{}`
        ```python
        name = input("What is your name? ")
        print(f"Hello {name}, I'm glad to meet you!")
        ```
        Sample output:
        ```
        What is your name? Vizzini
        Hello Vizzini, I'm glad to meet you!
        ```
- A backslash (`\`) denotes a special character. This is called *escaping*. Examples include `\n` (new line), `\t` (tab), `\\` (backslash), `\'` (for including single quote within a single-quoted string), `\"` (for including a double quote within a double-quoted string). This example uses `\\` and `\n`:
    ```python
    print('\\n - newline\n\\t - tab')
    ```
    outputs
    ```
    \n - newline
    \t - tab
    ```
    This next example shows two different ways to get single quotes and double quotes within a quoted string:
    ```python
    print("I'm telling you, a \"python\" is a snake!")
    print('I\'m telling you, a "python" is a snake!')
    ``` 
    Output:
    ```
    I'm telling you, a "python" is a snake!
    I'm telling you, a "python" is a snake!
    ```