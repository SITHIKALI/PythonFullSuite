# PythonFullSuite

# About Python 🐍
Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Python is widely used for web development, data analysis, artificial intelligence, scientific computing, and more.

Key features of Python:
- Easy to learn and use
- Extensive standard library
- Cross-platform compatibility
- Strong community support
- Dynamic typing and memory management

Python's philosophy emphasizes code readability, as reflected in its design and the use of significant indentation.

# What’s all this about Python 2 vs Python 3

This part is a bit of a stain on Python’s history. Python 3 was released 2008, and its adoption was slow. First and foremost because it took popular packages a fair amount of time to port over their code.

This debate is now over. Python 2 will reach end-of-life in 2020, meaning that important updates - including security updates - will stop being released. That’s why this course focuses on Python3 only.

# Why Python?

Python the language is open source.

Python has a wide variety of applications such as:

    AI/ML
        SciPi
        NumPy
        Pandas
        PyTorch
    Hardware & Micro-controllers
        Raspberry Pi
        MicroPython
        CircuitPython
    Web Development
        Django
        Flask
    Scripting
        DevOps Configuration scripts

Python has an incredibly rich fully featured standard library, as well as the PyPI Package Index for 3rd party packages, which as of February 2019 contains 167,107 packages.

Python is considered to be a “batteries included” language, because the standard library contains a majority of the libraries and packages you’ll need in a standard application.

# Anatomy of a Python Program

# vriables
Variables in Python are used to store data values. They are created when you assign a value to a name using the `=` operator. For example:

```python
x = 10
name = "Alice"
is_active = True
```

Python variables are dynamically typed, meaning you don't need to declare their type explicitly. The type is inferred based on the value assigned. Variable names should follow the naming conventions and cannot start with a number or use special characters (except `_`).

# dir(type)
The dir() function is used to list the attributes and methods of an object. It is helpful for introspection and understanding what you can do with an object.
Ex : dir(type) / print(dir(str))
# help()
The help() function provides detailed documentation about an object, including its purpose, methods, and usage. It is useful for understanding how to use a specific function, class, or module.
Ex help(str)/help(print)
# exit()/ctrl+D
It is used to close the Python Interpreter

# Strings 
Strings in Python are sequences of characters enclosed in either single quotes (`'`) or double quotes (`"`). They are immutable, meaning their content cannot be changed after creation.

## Creating Strings
```python
# Single quotes
string1 = 'Hello'

# Double quotes
string2 = "World"

# Triple quotes for multi-line strings
string3 = '''This is
a multi-line
string.'''
```

## String Operations
- **Concatenation**: Combine strings using the `+` operator.
    ```python
    greeting = "Hello" + " " + "World"
    ```
- **Repetition**: Repeat strings using the `*` operator.
    ```python
    repeated = "Hi! " * 3
    ```
- **Indexing**: Access individual characters using their index (starting from 0).
    ```python
    first_char = string1[0]
    ```
- **Slicing**: Extract substrings using slicing.
    ```python
    substring = string1[1:4]
    ```

## Common String Methods
- `lower()`: Converts the string to lowercase.
- `upper()`: Converts the string to uppercase.
- `strip()`: Removes leading and trailing whitespace.
- `replace(old, new)`: Replaces occurrences of a substring.
- `split(delimiter)`: Splits the string into a list.
- `join(iterable)`: Joins elements of an iterable into a string.

Example:
```python
text = "  Hello, Python!  "
print(text.lower())  # "  hello, python!  "
print(text.strip())  # "Hello, Python!"
```

## String Formatting
- **f-strings** (Python 3.6+):
    ```python
    name = "Alice"
    age = 25
    print(f"My name is {name} and I am {age} years old.")
    ```
- **`format()` method**:
    ```python
    print("My name is {} and I am {} years old.".format(name, age))
    ```

Strings are a fundamental data type in Python and are widely used for text processing and manipulation.

# Functions
## Functions

Functions in Python are reusable blocks of code that perform a specific task. They help in organizing code, improving readability, and reducing redundancy.

### Defining a Function
A function is defined using the `def` keyword, followed by the function name and parentheses. The code block within the function is indented.

```python
def greet():
    print("Hello, World!")
```

### Calling a Function
To execute a function, you call it by its name followed by parentheses.

```python
greet()  # Output: Hello, World!
```

### Function with Parameters
Functions can accept parameters to make them more flexible.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!
```

### Return Statement
Functions can return a value using the `return` statement.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # Output: 8
```

---

## Arguments in Functions

Arguments are the values passed to a function when it is called. Python supports several types of arguments:

### 1. **Positional Arguments**
Arguments are matched to parameters in the order they are provided.

```python
def subtract(a, b):
    return a - b

print(subtract(10, 5))  # Output: 5
```

### 2. **Keyword Arguments**
Arguments are passed using the parameter name, allowing them to be provided in any order.

```python
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

introduce(age=30, name="Bob")  # Output: My name is Bob and I am 30 years old.
```

### 3. **Default Arguments**
Parameters can have default values, which are used if no argument is provided.

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()           # Output: Hello, Guest!
greet("Charlie")  # Output: Hello, Charlie!
```

### 4. **Variable-Length Arguments**
- **`*args`**: Allows a function to accept any number of positional arguments as a tuple.
    ```python
    def sum_all(*args):
        return sum(args)

    print(sum_all(1, 2, 3, 4))  # Output: 10
    ```
- **`**kwargs`**: Allows a function to accept any number of keyword arguments as a dictionary.
    ```python
    def print_details(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    print_details(name="Alice", age=25, city="New York")
    # Output:
    # name: Alice
    # age: 25
    # city: New York
    ```

Functions and arguments are essential for writing modular and reusable code in Python. They allow you to break down complex problems into smaller, manageable pieces.
