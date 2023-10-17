## Programs can interact with files on your file system

Up to this point, in all programs we have written, data is either hard-coded into the program or is input from the user. As a similar limitation, we have always output results to the console. These limitations have the following disadvantages:
- Hard-coded data can't be changed without modifying the program itself.
- It's inconvenient to hard-code large sets of data within a program.
- Output written to the console is not saved permanently.

File input/output (reading from a file and writing to a file) allows us to input data into a program from a file and store output from a program into a file. This way, we can modify the data by modifying the file rather than the actual program. This is especially important when the amount of data is large, since it's better practice to have large files rather than large programs. Finally, if our programs write data to files stored on the file system, then they can be used even after the program terminates. For example, another program could use that output as its input.

When we talk about input and output, we are taking a perspective from inside a running program. So *input* refers to getting information into the program from a file, and *output* refers to information coming from the program and being stored in a file.