# my_own_wc_tool
Created my own wc linux tool using python script
# https://codingchallenges.fyi/challenges/challenge-wc/#the-challenge---building-wc
# Write Your Own wc Tool
This challenge is to build your own version of the Unix command line tool wc!

The Unix command line tools are a great metaphor for good software engineering and they follow the Unix Philosophies of:

Writing simple parts connected by clean interfaces - each tool does just one thing and provides a simple CLI that handles text input from either files or file streams.
Design programs to be connected to other programs - each tool can be easily connected to other tools to create incredibly powerful compositions.
Following these philosophies has made the simple unix command line tools some of the most widely used software engineering tools - allowing us to create very complex text data processing pipelines from simple command line tools. There’s even a Coursera course on Linux and Bash for Data Engineering.

The provided Python script is a custom implementation of the Unix `wc` command-line tool, which is used to count words, lines, characters, and bytes in a text file. The script accepts various command-line options to specify what type of information to count and can also read from standard input if no filename is provided.

Here's a breakdown of the script's components:

1. **Signal Handling**: The script begins by setting up a signal handler for the Control-C (Ctrl+C) signal. If a user interrupts the script's execution with Ctrl+C, it will gracefully exit without raising an exception.

2. **Counting Functions**:
   - `get_bytes(fileContent)`: This function takes the content of a file as input and returns the number of bytes in the content by encoding it using UTF-8 and calculating the length.
   - `get_words(fileContent)`: This function counts the number of words in the content by splitting it into words based on spaces.
   - `get_lines(fileContent)`: This function counts the number of lines in the content by splitting it into lines using newline characters and checking for empty lines at the end of the file.
   - `get_characters(fileContent)`: This function counts the total number of characters in the content.

3. **Utility Functions**:
   - `basename(filePath)`: This function takes a file path as input and returns the base filename.
   - `output_console(output, filePath)`: This function prints the output along with the basename of the input file.

4. **Main Function (main())**:
   - The `argparse` module is used to define and parse command-line arguments. The script accepts several options, including `-c` (bytes), `-l` (lines), `-w` (words), and `-m` (characters), and also accepts a filename as a positional argument.
   - If a filename is provided as an argument, the script reads the file's content using UTF-8 encoding.
   - Depending on the provided options, the script calls the counting functions and stores the results in variables like `number_bytes`, `number_words`, etc.
   - The script then generates the appropriate output based on the options provided. If no options are given, it assumes the default behavior (equivalent to using `-c`, `-l`, and `-w`) and generates the default output.
   - The output is printed to the console using the `output_console` function.

5. **Execution**: The script's main function is called when the script is executed, and it starts by parsing command-line arguments. If executed directly, the script performs the requested counting and printing.

The script provides similar functionality to the `wc` command and is customizable through command-line options. Users can specify which type of counting they want to perform on a given file, or they can use standard input for counting.

To use the script, you would typically call it from the command line with various options and the filename as an argument, or you can pipe input to it using standard input, as shown in the provided examples.


