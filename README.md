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

Advanced Data Types - Containers and sequences

Now that we’ve got the basics of strings and numbers down, let’s talk about the advanced data types - list, tuple, dict and set. These are container objects that let us organize other types of objects into one data structure.

It seems like you'd like to include a detailed guide on Python lists in your README file. Here's a formatted version of your notes for the README:

---

# Python Lists Cheat Sheet

Lists are one of the most powerful data types in Python. Generally, they’re container objects used to store related items together.

## List Basics
| **Type**                | `list`                                                                 |
|-------------------------|------------------------------------------------------------------------|
| **Use**                | Used for storing similar items, and in cases where items need to be added or removed. |
| **Creation**           | `[]` or `list()` for an empty list, or `[1, 2, 3]` for a list with items. |
| **Search Methods**     | `my_list.index(item)` or `item in my_list` |
| **Search Speed**       | Searching in a large list is slow. Each item must be checked. |
| **Common Methods**     | `len(my_list)`, `append(item)` to add, `insert(index, item)` to insert in the middle, `pop()` to remove. |
| **Order Preserved?**   | Yes. Items can be accessed by index. |
| **Mutable?**           | Yes |
| **In-place Sortable?** | Yes. Use `my_list.sort()` for in-place sorting. |

---

## Working with Lists

### Creating Lists
1. Create an empty list:
    ```python
    list()
    []
    ```

2. Create a list with items:
    ```python
    names = ["Nina", "Max", "Jane"]
    ```

3. Check the type:
    ```python
    type([])
    ```

### Accessing Elements (Indexes and Indices)
Lists retain the order of items and can be accessed by index. Indexes start at `0`.

Example:
```python
names = ["Nina", "Max", "Jane"]
print(names[0])  # Output: 'Nina'
```

### Updating an Item in a List
```python
names[2] = "Floyd"
```

### Common Errors with Indexing
Accessing an index greater than or equal to the length of the list raises an `IndexError`.

---

## Formatting Lists
- Add new lines after commas for readability.
- Optionally include a trailing comma after the last item.

Example:
```python
names = [
    "Nina",
    "Max",
    "Jane",
]
```

---

## Sorting Lists

### Sorting a Copy
To sort a list without modifying the original:
```python
sorted(lottery_numbers)  # Ascending
sorted(lottery_numbers, reverse=True)  # Descending
```

### Sorting In-place
To sort the list and modify it:
```python
my_list.sort()  # Ascending
my_list.sort(reverse=True)  # Descending
```

### Reversing a List
To reverse the elements:
```python
my_list.reverse()
```

---

## Common Gotchas
1. Forgetting commas between items:
    ```python
    numbers = [1, 2 3]  # SyntaxError
    ```

2. Forgetting the closing bracket:
    ```python
    names = ["Nina"
    ```

---

## Finding Methods
Use `dir()` to explore available methods:
```python
dir(list)
```

For detailed help on a method:
```python
help(list.append)
```

---

It looks like you want to continue documenting Python lists in your README file. Here's a formatted version of "Lists, Part 2" for your README:

---

# Python Lists Cheat Sheet - Part 2

This section covers adding, removing, changing, and finding items in lists.

| **Action**                | **Method**                          | **Returns**       | **Possible Errors**                              |
|---------------------------|--------------------------------------|-------------------|-------------------------------------------------|
| **Check Length**          | `len(my_list)`                      | `int`            | -                                               |
| **Add: To the End**       | `my_list.append(item)`              | `-`              | -                                               |
| **Insert: At Position**   | `my_list.insert(pos, item)`         | `-`              | -                                               |
| **Update: At Position**   | `my_list[pos] = item`               | `-`              | `IndexError` if `pos >= len(my_list)`           |
| **Extend: Add from List** | `my_list.extend(other_list)`        | `-`              | -                                               |
| **Is Item in List?**      | `item in my_list`                   | `True` or `False`| -                                               |
| **Index of Item**         | `my_list.index(item)`               | `int`            | `ValueError` if `item` is not in `my_list`      |
| **Count of Item**         | `my_list.count(item)`               | `int`            | -                                               |
| **Remove an Item**        | `my_list.remove(item)`              | `-`              | `ValueError` if `item` is not in `my_list`      |
| **Remove by Index**       | `my_list.pop()` or `my_list.pop(pos)`| `item`           | `IndexError` if `pos >= len(my_list)`           |

---

## Checking Length
The `len()` function can be used to check the number of items in a list (or other types like strings).

```python
names = ["Nina", "Max"]
print(len(names))  # 2

name = "Nina"
print(len(name))  # 4
```

---

## Adding Items

### Append to the End
Use `my_list.append(item)` to add an item to the end of the list:
```python
names = ["Nina", "Max"]
names.append("John")
print(names)  # ['Nina', 'Max', 'John']
```

### Insert at Position
Use `my_list.insert(pos, item)` to insert an item at a specific position:
```python
names = ["Nina", "Max"]
names.insert(0, "Rose")
print(names)  # ['Rose', 'Nina', 'Max']
```

### Extend with Another List
Use `my_list.extend(other_list)` to add all items from another list:
```python
names = ["Nina", "Max"]
colors = ["Red", "Blue"]
names.extend(colors)
print(names)  # ['Nina', 'Max', 'Red', 'Blue']
```

---

## Looking for Items

### Check if an Item Exists
Use the `in` operator to check if an item exists:
```python
names = ["Nina", "Max", "Phillip", "Nina"]
print("Nina" in names)  # True
print("Rose" in names)  # False
```

### Find the Index of an Item
Use `my_list.index(item)` to find the first index of an item:
```python
names = ["Nina", "Max", "Phillip", "Nina"]
print(names.index("Nina"))  # 0
```
Raises a `ValueError` if the item is not in the list.

### Count Occurrences of an Item
Use `my_list.count(item)` to count how many times an item appears:
```python
names = ["Nina", "Max", "Phillip", "Nina"]
print(names.count("Nina"))  # 2
```

---

## Updating Items

To update an item, assign a new value to its position using square brackets `[]`:
```python
names = ["Nina", "Max"]
names[0] = "Rose"
print(names)  # ['Rose', 'Max']
```

You can also use `my_list.index(item)` to locate the position:
```python
names = ["Nina", "Max"]
pos = names.index("Max")
names[pos] = "Rose"
print(names)  # ['Nina', 'Rose']
```

---

## Removing Items

### Remove by Value
Use `my_list.remove(item)` to remove the first occurrence of an item:
```python
names = ["Nina", "Max", "Rose"]
names.remove("Nina")
print(names)  # ['Max', 'Rose']
```
Raises a `ValueError` if the item is not in the list.

### Remove by Index
Use `my_list.pop()` to remove the last item or `my_list.pop(pos)` to remove an item at a specific position. The removed item is returned:
```python
names = ["Nina", "Max", "Rose"]
print(names.pop())  # 'Rose'
print(names)  # ['Nina', 'Max']

print(names.pop(1))  # 'Max'
print(names)  # ['Nina']
```
Raises an `IndexError` if the index is out of range.

---

It looks like you're creating comprehensive notes for Python data types for your README file. Here's a formatted section for **Tuples**:

---

# Python Tuples Cheat Sheet

Tuples are lightweight collections used to keep track of related but different items. Unlike lists, **tuples are immutable**, meaning that once a tuple is created, its items cannot be changed.

## Tuple Basics
| **Type**                | `tuple`                                                                 |
|-------------------------|------------------------------------------------------------------------|
| **Use**                | Used for storing a snapshot of related items when we don’t plan on modifying, adding, or removing data. |
| **Creation**           | `()` or `tuple()` for an empty tuple. `(1, )` for one item, or `(1, 2, 3)` for a tuple with items. |
| **Search Methods**     | `my_tuple.index(item)` or `item in my_tuple` |
| **Search Speed**       | Searching for an item in a large tuple is slow. Each item must be checked. |
| **Common Methods**     | Can’t add or remove from tuples. |
| **Order Preserved?**   | Yes. Items can be accessed by index. |
| **Mutable?**           | No |
| **In-place Sortable?** | No |

---

## Uses
Tuples are ideal for storing a **snapshot** of data when you don’t need to modify it. For example:
- Storing the information for a row in a spreadsheet.
- Returning multiple values from a function.
- Using as keys in dictionaries or elements of sets (since tuples are immutable).

---

## Examples

### Empty and One-Item Tuples
Creating tuples has a small quirk when it comes to one-item tuples:
```python
# Empty tuple
a = ()
print(type(a))  # <class 'tuple'>

# One-item tuple (requires a trailing comma)
b = (1)
print(type(b))  # <class 'int'> (Not a tuple)

c = (1, )
print(type(c))  # <class 'tuple'>
```

### Creation
Tuples can store related but different types of data:
```python
student = ("Marcy", 8, "History", 3.5)
```

---

## Accessing Items
You can access tuple items by index, but you **cannot update** them:
```python
student = ("Marcy", 8, "History", 3.5)

# Access by index
print(student[0])  # 'Marcy'

# Attempting to update a tuple (raises an error)
student[0] = "Bob"  # TypeError: 'tuple' object does not support item assignment
```

Tuples also don’t have methods like `append` or `extend`, as they are immutable.

---

## Tuple Unpacking
Tuples allow for an efficient way to consolidate and unpack information:
```python
student = ("Marcy", 8, "History", 3.5)

# Unpacking a tuple
name, age, subject, grade = student
print(name)    # 'Marcy'
print(age)     # 8
print(subject) # 'History'
print(grade)   # 3.5
```

### Returning Tuples from Functions
Functions can return tuples, which can be unpacked:
```python
def http_status_code():
    return 200, "OK"

code, value = http_status_code()
print(code)  # 200
print(value) # 'OK'
```

---

## Key Takeaways
- Tuples are immutable, making them perfect for storing **unchanging data**.
- They are lightweight and can be used as **keys in dictionaries** or **elements in sets**.
- Tuples support quick **unpacking** for efficient data consolidation and retrieval.

---
Here's a detailed and formatted section for **Sets** to include in your README file:

---

# Python Sets Cheat Sheet

Sets are a data type that allows you to store immutable types in an **unordered** way. Each item in a set must be **unique**—duplicates are not allowed. Sets are particularly useful for **fast membership testing** and **set operations** like union, difference, and intersection.

## Set Basics
| **Type**                | `set`                                                                 |
|-------------------------|------------------------------------------------------------------------|
| **Use**                | Used for storing immutable data types uniquely. Easy to compare items in sets. |
| **Creation**           | `set()` for an empty set (`{}` creates an empty dictionary). `{1, 2, 3}` for a set with items. |
| **Search Methods**     | `item in my_set` |
| **Search Speed**       | Very fast for large sets. |
| **Common Methods**     | `my_set.add(item)`, `my_set.discard(item)`, `my_set.update(other_set)` |
| **Order Preserved?**   | No. Items cannot be accessed by index. |
| **Mutable?**           | Yes. Items can be added or removed. |
| **In-place Sortable?** | No, because items are unordered. |

---

## Examples

### Empty Sets
To create an empty set, use `set()`:
```python
my_new_set = {}
print(type(my_new_set))  # <class 'dict'>

my_set = set()
print(type(my_set))  # <class 'set'>
```

### Sets with Items
Sets automatically remove duplicate values:
```python
names = {"Nina", "Max", "Nina"}
print(names)  # {'Max', 'Nina'}
print(len(names))  # 2
```

### Sets Only Contain Immutable Types
Sets use a hashing algorithm to store items, so only **immutable types** can be added:
```python
print(hash("Nina"))  # e.g., 3509074130763756174
print(hash([]))  # TypeError: unhashable type: 'list'

# Adding a mutable type like a list raises an error
my_set = {"Nina"}
my_set.add([])  # TypeError: unhashable type: 'list'
```

### Removing Duplicates from a List
Pass a list into the `set()` constructor to quickly remove duplicates:
```python
colors = ["Red", "Yellow", "Red", "Green", "Green"]
unique_colors = set(colors)
print(unique_colors)  # {'Red', 'Green', 'Yellow'}
```

---

## Set Characteristics

### Unordered
Sets don’t maintain order:
```python
my_set = {1, "a", 2, "b", "cat"}
print(my_set)  # {1, 2, 'cat', 'a', 'b'}
```

### No Indexing
Items in a set cannot be accessed by index:
```python
my_set = {"Red", "Green", "Blue"}
print(my_set[0])  # TypeError: 'set' object does not support indexing
```

### Sorting a Set
To sort a set, convert it to a list or use `sorted()`:
```python
my_set = {"a", "b", "cat", "dog", "red"}
sorted_set = sorted(my_set)
print(sorted_set)  # ['a', 'b', 'cat', 'dog', 'red']
```

---

## Adding and Removing Items

### Add Items
Use `my_set.add(item)`:
```python
colors = {"Red", "Green", "Blue"}
colors.add("Orange")
print(colors)  # {'Orange', 'Green', 'Blue', 'Red'}
```

### Remove Items
Use `my_set.discard(item)` to remove an item. No error occurs if the item is not found:
```python
colors = {"Red", "Green", "Blue"}
colors.discard("Green")
print(colors)  # {'Blue', 'Red'}
colors.discard("Green")  # No error
```

To remove an item and raise an error if it’s not found, use `my_set.remove(item)`:
```python
colors.remove("Green")  # KeyError: 'Green'
```

### Update a Set
Use `my_set.update(sequence)` to add items from another sequence (set, list, or tuple):
```python
colors = {"Red", "Green"}
numbers = {1, 3, 5}
colors.update(numbers)
print(colors)  # {1, 3, 'Red', 5, 'Green'}

# Be careful with strings
numbers = {1, 3, 5}
numbers.update("hello")
print(numbers)  # {1, 3, 'h', 5, 'o', 'e', 'l'}
```

---

## Set Operations

Sets allow quick and easy operations to compare items between sets:

| **Method Operation**     | **Symbol Operation**  | **Result**                                                                        |
|--------------------------|-----------------------|----------------------------------------------------------------------------------|
| `s.union(t)`             | `s | t`              | Creates a new set with all items from both `s` and `t`.                         |
| `s.intersection(t)`      | `s & t`              | Creates a new set containing only items in both `s` and `t`.                    |
| `s.difference(t)`        | `s ^ t`              | Creates a new set containing items not in both `s` and `t`.                     |

### Examples

#### Union
Combine two sets to create a new one containing all unique items:
```python
rainbow_colors = {"Red", "Orange", "Yellow", "Green", "Blue", "Violet"}
favorite_colors = {"Blue", "Pink", "Black"}
combined = rainbow_colors | favorite_colors
print(combined)  # {'Orange', 'Red', 'Yellow', 'Green', 'Violet', 'Blue', 'Black', 'Pink'}
```

#### Intersection
Find common items between two sets:
```python
common = rainbow_colors & favorite_colors
print(common)  # {'Blue'}
```

#### Difference
Find items that are not in both sets:
```python
difference = rainbow_colors ^ favorite_colors
print(difference)  # {'Orange', 'Red', 'Yellow', 'Green', 'Violet', 'Black', 'Pink'}
```

---

## Additional Notes
- **Subset and Superset Checks**: Sets provide methods like `issubset` and `issuperset` for checking relationships between sets.
- **Immutable Sets**: Python provides a `frozenset` type for immutable sets.

For more information, call `help(set)` or read the Python documentation.

---

Here is a formatted section for **Dictionaries** to include in your README file:

---

# Python Dictionaries Cheat Sheet

Dictionaries allow us to store data in **key-value pairs**. They are mutable, but their keys must be immutable types. Dictionaries provide fast access to values associated with specific keys.

## Dictionary Basics
| **Type**                | `dict`                                                                 |
|-------------------------|------------------------------------------------------------------------|
| **Use**                | Use for storing data in key-value pairs. Keys must be immutable types. |
| **Creation**           | `{}` or `dict()` for an empty dictionary. `{1: "one", 2: "two"}` for a dictionary with items. |
| **Search Methods**     | `key in my_dict` |
| **Search Speed**       | Fast for large dictionaries. |
| **Common Methods**     | `my_dict[key]`, `my_dict.get(key)`, `my_dict.items()`, `my_dict.keys()`, `my_dict.values()` |
| **Order Preserved?**   | Yes, as of Python 3.6 (insertion order). Items cannot be accessed by index, only by key. |
| **Mutable?**           | Yes. Keys can be added or removed. |
| **In-place Sortable?** | No. Dictionaries don’t have indices. |

---

## Examples

### Empty Dictionaries
Create an empty dictionary:
```python
my_dict = {}
print(type(my_dict))  # <class 'dict'>

my_dict = dict()
print(type(my_dict))  # <class 'dict'>
```

### Creating Dictionaries with Items
Dictionaries store **key-value pairs**:
```python
nums = {1: "one", 2: "two", 3: "three"}
print(len(nums))  # 3
```

### Keys Must Be Immutable
Keys can only be **immutable types** (e.g., `int`, `str`, `tuple`). Mutable types like `list` or `dict` cannot be used as keys:
```python
my_dict = {1: "one", (2, 3): "tuple_key"}
# Raises an error:
my_dict = {[]: "list_key"}  # TypeError: unhashable type: 'list'
```

---

## Accessing Items
Access values using square-bracket notation with the key:
```python
nums = {1: "one", 2: "two", 3: "three"}
print(nums[1])  # 'one'
```

### Handling Missing Keys
If a key is not found, square-bracket access raises a `KeyError`:
```python
nums = {1: "one"}
print(nums[2])  # KeyError: 2
```

Use `my_dict.get(key)` to avoid errors and return `None` if the key is missing:
```python
result = nums.get(2)
print(result)  # None
```

Provide a default value if the key is missing:
```python
result = nums.get(2, "default")
print(result)  # 'default'
```

---

## Adding and Updating Items

### Adding a Key-Value Pair
Use square brackets to add a new key-value pair:
```python
nums = {1: "one", 2: "two"}
nums[3] = "three"
print(nums)  # {1: 'one', 2: 'two', 3: 'three'}
```

### Updating a Value
Assigning a value to an existing key will overwrite it:
```python
nums[2] = "updated_two"
print(nums)  # {1: 'one', 2: 'updated_two'}
```

### Updating with Another Dictionary
Use `my_dict.update(other_dict)` to merge dictionaries:
```python
colors = {"r": "Red", "g": "Green"}
numbers = {1: "one"}
colors.update(numbers)
print(colors)  # {'r': 'Red', 'g': 'Green', 1: 'one'}
```

---

## Removing Items
Use `del` to remove a key-value pair:
```python
nums = {1: "one", 2: "two"}
del nums[2]
print(nums)  # {1: 'one'}
```

---

## Working with Items, Keys, and Values

### Getting All Keys
Use `my_dict.keys()`:
```python
nums = {1: "one", 2: "two"}
print(nums.keys())  # dict_keys([1, 2])
```

### Getting All Values
Use `my_dict.values()`:
```python
print(nums.values())  # dict_values(['one', 'two'])
```

### Getting All Items
Use `my_dict.items()` to retrieve key-value pairs as tuples:
```python
print(nums.items())  # dict_items([(1, 'one'), (2, 'two')])
```

---

## Complex Dictionaries
Dictionaries can store other sequences like lists or tuples:
```python
colors = {"Green": ["Spinach"]}
colors["Green"].append("Apples")
print(colors)  # {'Green': ['Spinach', 'Apples']}
```

---

### Key Takeaways
- Dictionaries provide fast access to values using keys.
- Keys must be immutable types.
- Use `get()` to handle missing keys without raising errors.
- Use `update()` to merge dictionaries.

---

Here is a formatted section for **Mutability** to include in your README file:

---

# Mutability Cheat Sheet

**Mutability** refers to whether the contents of an object can be changed after it is created. Immutable objects cannot be modified, while mutable objects can.

---

## Simple Types (Immutable)

All the simple data types are **immutable**:

| **Type**                  | **Use**                | **Mutable?** |
|---------------------------|------------------------|--------------|
| `int`, `float`, `decimal` | Store numbers          | No           |
| `str`                     | Store strings          | No           |
| `bool`                    | Store `True` or `False`| No           |

---

## Container Types

Here’s a quick reference for the mutability of the container types we’ve covered:

| **Container Type** | **Use**                                                                                     | **Mutable?** |
|---------------------|--------------------------------------------------------------------------------------------|--------------|
| `list`             | Ordered group of items, accessible by position                                              | Yes          |
| `set`              | Mutable unordered group consisting only of immutable items. Useful for set operations like membership, intersection, and difference. | Yes          |
| `tuple`            | Ordered group of items in an **immutable** collection                                       | No           |
| `dict`             | Key-value pairs                                                                            | Yes          |

---

Here’s how you can organize the **Practice** section on **Lists, Dictionaries, Tuples, and Sets** with examples and explanations for your README file:

---

# Practice: Lists, Dictionaries, Tuples, and Sets

This section provides practical examples and operations for Python's key data structures: **Lists**, **Dictionaries**, **Tuples**, and **Sets**. Along with examples, it includes notes on **mutability**.

---

## Lists

Lists are great for storing an **ordered sequence** of objects. You can modify their contents, access individual items, and use slicing for sublists.

### Examples:
```python
# Creating a list
my_list = ["h", "e", "l", "l", "o"]

# Add to the list
my_list.append("!")
print(my_list)  # ['h', 'e', 'l', 'l', 'o', '!']

# Slicing the list
print(my_list[4:6])  # ['l', '!'] (indexes 4 and 5)
print(my_list[4:])   # ['l', '!'] (everything from index 4 onward)
print(my_list[-2:])  # ['l', '!'] (last two elements)

# Modify elements
my_list.remove("l")   # Remove the first 'l'
my_list.insert(2, "l")  # Add 'l' back at index 2

# Deleting and popping
del my_list[0]       # Delete the first element
last_item = my_list.pop()  # Remove and return the last element
print(last_item)     # '!'

# Other operations
print(my_list[2])    # Access by index
print("!" in my_list)  # Check for membership in list

# Sorting
my_list.sort(reverse=True)  # Sort in reverse order (in-place)
sorted_list = sorted(my_list)  # Get a new, sorted list (not in-place)
```

---

## Sets

Sets are **unordered collections** of unique items. They are ideal for **membership testing** and **set operations** like union, intersection, and difference.

### Examples:
```python
# Creating sets
my_set = set()  # Empty set
my_set = {1, 2, 3}  # Set with initial items

# Adding and removing items
my_set.add(4)
my_set.remove(2)

# Membership testing
print(2 in my_set)  # False

# Unique items only
my_set.add(3)  # Duplicate values are ignored
print(my_set)  # {1, 3, 4}

# Set operations
my_other_set = {1, 2, 3}
print(my_set.union(my_other_set))        # {1, 2, 3, 4} (all items)
print(my_set.intersection(my_other_set))  # {1, 3} (common items)
print(my_set.difference(my_other_set))    # {4} (items in my_set but not in my_other_set)
```

---

## Tuples

Tuples are **immutable** collections often used to store related data. They are lightweight and can be unpacked into variables.

### Examples:
```python
# Creating tuples
my_tuple = (1,)  # Single-item tuple (requires a trailing comma)
my_tuple = (1, 2, 3)

# Accessing tuple elements
person = ("Jim", 29, "Austin, TX")
name, age, hometown = person  # Unpacking a tuple
print(name)      # 'Jim'
print(age)       # 29
print(hometown)  # 'Austin, TX'

# Tuples are immutable
my_tuple[0] = 42  # TypeError: 'tuple' object does not support item assignment
```

---

## Dictionaries

Dictionaries are **key-value pairs** where keys must be unique and immutable. They are great for **fast lookups** and organizing data.

### Examples:
```python
# Creating dictionaries
my_dict = {"key": "value"}
my_dict["hello"] = "world"
my_dict["foo"] = "bar"

# Accessing values
print(my_dict["hello"])  # 'world'
print(my_dict.get("baz", "default"))  # 'default' (if key doesn't exist)

# Adding and updating
my_dict["new_key"] = "new_value"  # Add or update key-value pair
print(my_dict)

# Keys, values, and items
print(my_dict.keys())    # dict_keys(['key', 'hello', 'foo', 'new_key'])
print(my_dict.values())  # dict_values(['value', 'world', 'bar', 'new_value'])
print(my_dict.items())   # dict_items([('key', 'value'), ('hello', 'world'), ...])

# Iterating over items
for key, value in my_dict.items():
    print(f"{key}: {value}")
```

---

## Mutability in Practice

Mutability defines whether an object can be **changed** after its creation.

| **Type**         | **Mutable?** | **Notes**                                                                 |
|-------------------|--------------|---------------------------------------------------------------------------|
| `list`           | Yes          | Items can be added, removed, or changed.                                 |
| `set`            | Yes          | Items can be added or removed, but indexing is not supported.            |
| `tuple`          | No           | Immutable. Once created, its contents cannot change.                     |
| `dict`           | Yes          | Keys and values can be added, removed, or updated.                       |

### Examples:
```python
# Lists are mutable
my_list = [1, 2, 3]
my_list[0] = "a"
print(my_list)  # ['a', 2, 3]

# Sets are mutable
my_set = {1, 2, 3}
my_set.add("a")
print(my_set)  # {1, 2, 3, 'a'}

# Dictionaries are mutable
my_dict = {"key": "value"}
my_dict["new_key"] = "new_value"
print(my_dict)  # {'key': 'value', 'new_key': 'new_value'}

# Tuples are immutable
my_tuple = (1, 2, 3)
my_tuple[0] = "a"  # TypeError: 'tuple' object does not support item assignment
```

---

Here’s how the **Boolean Logic** section can be added to your README file:

---

# Boolean Logic

Boolean Logic allows you to test your assumptions and control the flow of your program. It is the foundation of decision-making in Python.

---

Here is the Truthiness section formatted for inclusion in your README file:
Truthiness in Python

Evaluating expressions to determine their truthiness (True or False) helps control the flow of a program. Here's a cheat sheet and practical examples to help understand Python's truthiness rules.
Truthiness Cheat Sheet
Type	Truthiness Rule
int	0 is False, all other numbers (including negatives) are True.
Containers (list, tuple, set, dict)	Empty containers are False, containers with items are True.
None	Always evaluates to False.
Boolean Basics

True and False are keywords in Python. Avoid naming variables as True or False to prevent conflicts.
Python

>>> True
True
>>> False
False

# Test assumptions using the bool() function
>>> bool(3 < 5)
True

Numbers

    0 evaluates to False.
    All other numbers, including negative numbers, evaluate to True.

Python

>>> bool(0)    # Integer 0
False
>>> bool(1)    # Positive Integer
True
>>> bool(-1)   # Negative Integer
True

Sequences (Lists, Tuples, Sets, Dictionaries)

    Empty sequences always evaluate to False.
    Non-empty sequences always evaluate to True.

Python

# Empty sequences
>>> bool("")    # Empty String
False
>>> bool([])    # Empty List
False
>>> bool(set()) # Empty Set
False
>>> bool({})    # Empty Dictionary
False
>>> bool(())    # Empty Tuple
False

# Non-empty sequences
>>> bool("Hello")   # Non-empty String
True
>>> bool([1])       # Non-empty List
True
>>> bool({1})       # Non-empty Set
True
>>> bool({1: 1})    # Non-empty Dictionary
True
>>> bool((1,))      # Non-empty Tuple
True

None

The None type in Python represents nothing and always evaluates to False.
Python

>>> bool(None)
False

# Be careful when checking if a variable is declared or contains an empty sequence
>>> my_name = None
>>> bool(my_name)  # Variable is None
False
>>> my_name = ""
>>> bool(my_name)  # Variable is an empty string
False

>>> my_list = None
>>> bool(my_list)  # Variable is None
False
>>> my_list = []
>>> bool(my_list)  # Variable is an empty list
False

Key Takeaways

    Use the bool() constructor to test the truthiness of an expression.
    Be cautious when differentiating between None and empty sequences, as both evaluate to False.




---

# Comparisons in Python

Python provides a variety of operators to compare values. These comparisons return a boolean (`True` or `False`) and are useful for controlling program flow.

---

## Order Comparisons

Order comparisons are used to compare values based on their size.

### Cheat Sheet
| **Operator** | **Means**                     |
|--------------|--------------------------------|
| `<`          | Less-than                     |
| `<=`         | Less-than-or-equal-to         |
| `>`          | Greater-than                  |
| `>=`         | Greater-than-or-equal-to      |

### Examples
Comparing numbers is straightforward:
```python
>>> 1 < 10  # 1 is less than 10
True
>>> 20 <= 20  # 20 is less than or equal to 20
True
>>> 10 > 1  # 10 is greater than 1
True
>>> -1 > 1  # -1 is greater than 1
False
>>> 30 >= 30  # 30 is greater than or equal to 30
True
```

Strings are compared **lexicographically** (based on ASCII values):
```python
>>> "T" < "t"  # Uppercase letters are "lower" valued than lowercase letters
True
>>> "a" < "b"  # Alphabetical order
True
>>> "bat" < "cat"  # Lexicographic comparison checks characters one by one
True
```

---

## Equality Comparisons

Equality operators compare the **contents** of two values and return a boolean.

### Cheat Sheet
| **Operator** | **Means**            |
|--------------|-----------------------|
| `==`         | Equals               |
| `!=`         | Not-equals           |

### Examples
Equality for simple data types:
```python
>>> a = 1
>>> b = 1
>>> a == b  # Are a and b equal?
True
>>> a != b  # Are a and b not equal?
False

>>> a = "Nina"
>>> b = "Nina"
>>> a == b
True
>>> a != b
False
```

Equality for container types:
```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b  # Lists have the same contents
True
>>> a != b
False
```

---

## Identity Comparisons

### Cheat Sheet
| **Operator** | **Means**                                   |
|--------------|---------------------------------------------|
| `is`         | Is the same object in memory? (not equality)|
| `is not`     | Is not the same object in memory?           |

> **Note:** Equality (`==`) is not the same as identity (`is`). The `is` operator checks if two objects point to the same memory location, while `==` checks if their **contents** are the same.

### Examples
```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]

>>> a == b  # Equality: Do a and b have the same contents?
True
>>> a is b  # Identity: Are a and b the same object in memory?
False
```

#### When to Use `is`:
The `is` operator is typically used when comparing a value to Python's built-in types like `None`, `True`, or `False`.

```python
>>> a = True
>>> a is True
True

>>> b = False
>>> b is False
True
>>> b is not True  # Opposite of `is b True` (i.e., is b False?)
True

>>> c = None
>>> c is None
True
>>> c is not None
False
```

---



---

# Boolean Operators: `and`, `or`, `not`

Boolean operators (`and`, `or`, `not`) allow you to compare expressions and determine their truthiness. These operators are a core part of programming, enabling logical decision-making in your code.

In Python, these operators prioritize **readability** by using English words (`and`, `or`, `not`) instead of symbolic representations like `&&`, `||`, or `!`.

---

## Cheat Sheet

| **Operation** | **Result**                                                                                   |
|---------------|----------------------------------------------------------------------------------------------|
| `a or b`      | If `a` is `False`, then `b`, else `a`.                                                       |
| `a and b`     | If `a` is `False`, then `a`, else `b`.                                                       |
| `not a`       | If `a` is `False`, then `True`, else `False`.                                                |

---

## `and`

- Returns the second value (`b`) if the first value (`a`) is `True`.
- Returns the first value (`a`) if it is `False`.

### Examples:
```python
>>> a = True
>>> b = True
>>> a and b  # Both are True
True

>>> a = False
>>> b = True
>>> a and b  # a is False, so a is returned
False

# With "truthiness"
>>> bool(0)  # 0 is False
False
>>> bool(1)  # 1 is True
True
>>> 0 and 1  # 0 is False, so 0 is returned
0
```

---

## `or`

- Returns the first value (`a`) if it is `True`.
- Returns the second value (`b`) if the first value (`a`) is `False`.

### Examples:
```python
>>> a = True
>>> b = True
>>> a or b  # a is True, so a is returned
True

>>> a = False
>>> b = True
>>> a or b  # b is True, so b is returned
True

# With "truthiness"
>>> 0 or 1  # 0 is False, so 1 is returned
1
>>> 0 or None  # Both are False, so None is returned
None
```

---

## `not`

- Reverses the boolean value of `a`.
- If `a` is `True`, it returns `False`. If `a` is `False`, it returns `True`.

### Examples:
```python
>>> a = True
>>> not a  # Opposite of True is False
False

>>> a = False
>>> not a  # Opposite of False is True
True

# With numbers
>>> bool(1)  # 1 is True
True
>>> not 1    # Opposite of True is False
False

>>> bool(0)  # 0 is False
False
>>> not 0    # Opposite of False is True
True
```

---

## Combining Boolean Operators

You can combine multiple operators to test complex assumptions. Use parentheses for readability:
```python
>>> a = True
>>> b = True
>>> c = False

>>> a and (b or c)  # True and (True or False) = True
True

# Testing if both values are False
>>> a = False
>>> b = False
>>> not (a or b)  # Opposite of (False or False) = True
True
```

---

## Truthiness in Practice

Some values in Python are **truthy** (e.g., non-zero numbers, non-empty sequences), while others are **falsey** (e.g., `0`, `None`, empty sequences).

| **Operation** | **Result**                                                                 |
|---------------|----------------------------------------------------------------------------|
| `x or y`      | If `x` is `False`, then `y`, else `x`.                                     |
| `x and y`     | If `x` is `False`, then `x`, else `y`.                                     |

### Examples:
```python
>>> bool(0)      # 0 is False
False
>>> bool(1)      # 1 is True
True
>>> bool(None)   # None is False
False

>>> 1 or 0       # 1 is True, so 1 is returned
1
>>> 1 and 0      # 1 is True, but 0 is False, so 0 is returned
0
>>> 0 or None    # Neither is True, so None is returned
None
```

---

---

# Practice: Boolean Logic and Comparisons

This section provides practice examples for **comparison operators**, **truthiness**, and **boolean operators** in Python.

---

## Comparisons

Python offers a variety of operators to compare values. These operators test the **value** of objects, while `is` and `is not` test whether two objects are the **same in memory**.

### Comparison Operators Cheat Sheet
| **Operator** | **Means**                     |
|--------------|--------------------------------|
| `<`          | Less-than                     |
| `<=`         | Less-than-or-equal-to         |
| `>`          | Greater-than                  |
| `>=`         | Greater-than-or-equal-to      |
| `==`         | Equals                        |
| `!=`         | Not-equals                    |

### Examples:
```python
>>> 10 > 5       # True
>>> 5 > 10       # False
>>> 10 > 10      # False
>>> 10 >= 10     # True
>>> 5 < 10       # True
>>> 5 < 5        # False
>>> 5 <= 5       # True
>>> 5 == 5       # True
>>> 5 != 10      # True
```

---

## Truthiness

In Python, all objects can be tested for **truthiness**. An object is considered `True` unless:
- It is a "falsey" object, such as `0`, `None`, or an empty container (e.g., `[]`, `{}`).

### Key Points:
- **Equality (`==`)** checks if two objects have the same value.
- **Truthiness** checks if an object satisfies the condition in an `if` or `while` statement.

### Examples:
```python
>>> 5 == True  # False. The number 5 does not equal True.
>>> if 5:
...     print("The number 5 is truthy!")
... # Output: "The number 5 is truthy!"

# True and False can also be represented by 1 and 0
>>> 1 == True   # True
>>> 0 == False  # True
```

---

## Boolean Operators

Boolean operators (`and`, `or`, `not`) allow logical operations and return one of their operands rather than strict `True` or `False`.

### Boolean Operators Cheat Sheet
| **Operation** | **Result**                                                                 |
|---------------|----------------------------------------------------------------------------|
| `x or y`      | If `x` is false, then `y`, else `x`                                       |
| `x and y`     | If `x` is false, then `x`, else `y`                                       |
| `not x`       | If `x` is false, then `True`, else `False`                                |

### Examples:
```python
# OR Operator
>>> True or False      # True
>>> [] or [1, 2, 3]    # [1, 2, 3]
>>> "Hello" or None    # "Hello"

# AND Operator
>>> True and False     # False
>>> 5 and 0            # 0
>>> [1] and [1, 2, 3]  # [1, 2, 3]
>>> "Hello" and None   # None

# NOT Operator
>>> not True           # False
>>> not False          # True
>>> not 0              # True
>>> not 1              # False
```

---

## Combining Boolean Operators

You can combine multiple boolean operators to test complex assumptions. Use parentheses for clarity.

### Examples:
```python
# Using OR
>>> a = False
>>> b = False
>>> c = False
>>> a or b or c      # False
>>> b = True
>>> a or b or c      # True

# Using AND
>>> a and b and c    # False
>>> a = True
>>> c = True
>>> a and b and c    # True
```

---



---

# Loops and Control Statements

Loops and control statements allow us to control the logical flow of our program. These structures enable us to repeat actions, make decisions, and manage the execution of code based on specific conditions.

---


---

# Looping in Python

Loops are essential for iterating over sequences and controlling the flow of a program. Python makes looping simpler and more readable compared to other programming languages.

---

## `for` Loop Cheat Sheet

### Syntax:
```python
for single_item in items:
    # Body of the loop
```

The `for` loop iterates over each item in a sequence (e.g., list, tuple, string, dictionary) using the `in` keyword.

---

### Example: Looping Over a List
```python
colors = ["Red", "Green", "Blue", "Orange"]
for color in colors:
    print(f"The color is: {color}")
# Output:
# The color is: Red
# The color is: Green
# The color is: Blue
# The color is: Orange
```

---

## Looping Over a Range of Numbers

The `range()` function generates numbers from a start (inclusive) to a stop (exclusive). Optionally, you can define a step.

### Examples:
1. **Default Range (0 to 4)**:
    ```python
    for num in range(5):  # 0 to 4
        print(f"The number is: {num}")
    # Output:
    # The number is: 0
    # The number is: 1
    # The number is: 2
    # The number is: 3
    # The number is: 4
    ```

2. **Custom Range (1 to 4)**:
    ```python
    for num in range(1, 5):  # Start at 1, stop before 5
        print(f"The number is: {num}")
    # Output: 1, 2, 3, 4
    ```

3. **Custom Step (2 to 10, step by 2)**:
    ```python
    for num in range(2, 11, 2):  # Start at 2, step by 2
        print(f"The number is: {num}")
    # Output: 2, 4, 6, 8, 10
    ```

---

## Looping Over Items with Index Using `enumerate()`

Use `enumerate()` to loop through a sequence while accessing both the **index** and the **item**.

### Example:
```python
colors = ["Red", "Green", "Blue", "Orange"]
for index, color in enumerate(colors):
    print(f"Item: {color} is at index: {index}.")
# Output:
# Item: Red is at index: 0.
# Item: Green is at index: 1.
# Item: Blue is at index: 2.
# Item: Orange is at index: 3.
```

---

## Looping Over a Dictionary

Dictionaries store key-value pairs. By default, looping over a dictionary iterates through its **keys**.

### Loop Over Keys:
```python
hex_colors = {"Red": "#FF0000", "Green": "#008000", "Blue": "#0000FF"}
for color in hex_colors:
    print(f"The value of color is actually: {color}")
# Output:
# The value of color is actually: Red
# The value of color is actually: Green
# The value of color is actually: Blue
```

### Loop Over Key-Value Pairs Using `.items()`:
```python
for color, hex_value in hex_colors.items():
    print(f"For color {color}, the hex value is: {hex_value}")
# Output:
# For color Red, the hex value is: #FF0000
# For color Green, the hex value is: #008000
# For color Blue, the hex value is: #0000FF
```

---

### Common Error: Forgetting `.items()` When Looping Over Key-Value Pairs
Attempting to unpack key-value pairs without `.items()` results in a `ValueError`:
```python
for color, hex_value in hex_colors:
    print(f"For color {color}, the hex value is: {hex_value}")
# Error:
# ValueError: too many values to unpack (expected 2)
```

---

## Additional Notes

### Inclusive vs. Exclusive Ranges:
- **Inclusive**: Start value is included in the range.
- **Exclusive**: Stop value is not included in the range.

### Debugging `range()`:
To see the output of a `range()` call for debugging:
```python
print(list(range(5)))  # [0, 1, 2, 3, 4]
```
Avoid using this in production code for large ranges as it is inefficient.

---

## Additional Resources

For a deeper understanding of Pythonic looping, watch Raymond Hettinger’s talk: **Transforming Code into Beautiful, Idiomatic Python**.

---



---

# `if`, `else`, `elif`: Conditional Statements in Python

Conditional statements (`if`, `else`, `elif`) allow you to control the flow of your program by running specific blocks of code based on conditions.

---

## The `if` Statement

The `if` statement runs a block of code only when its condition evaluates to `True`.

### Syntax:
```python
if condition:
    # Code to run if the condition is True
```

### Example:
```python
if 3 < 5:
    print("Hello, World!")
# Output: Hello, World!
```

---

### Using `not` With `if` Statements
Use the `not` keyword to trigger code when the condition is `False`.

```python
b = False
if not b:
    print("Negation in action!")
# Output: Negation in action!
```

---

### `if` Statements and Truthiness

Python evaluates truthiness for conditions:
- `False-y`: `0`, `None`, empty containers (e.g., `[]`, `{}`).
- `Truth-y`: Non-zero numbers, non-empty containers.

```python
message = "Hi there."

a = 0
if a:   # 0 is False-y
    print(message)

b = -1
if b:   # -1 is Truth-y
    print(message)
# Output: Hi there.

c = []
if c:   # Empty list is False-y
    print(message)

d = [1, 2, 3]
if d:   # Non-empty list is Truth-y
    print(message)
# Output: Hi there.
```

---

### `if` Statements in Functions

You can use `if` statements in functions. Be mindful of the indentation.

```python
def modify_name(name):
    if len(name) < 5:
        return name.upper()
    else:
        return name.lower()

name = "Nina"
print(modify_name(name))
# Output: NINA
```

---

### Nested `if` Statements

You can nest `if` statements to test additional conditions.

```python
def num_info(num):
    if num > 0:
        print("Greater than zero")
        if num > 10:
            print("Also greater than 10.")

num_info(1)
# Output: Greater than zero

num_info(15)
# Output:
# Greater than zero
# Also greater than 10.
```

---

### Best Practices for `if` Statements

Avoid explicitly comparing conditions to `True` or `False` using `==` or `is`.

**Warning: Don't do this!**
```python
if (3 < 5) == True:
    print("Hello")
if (3 < 5) is True:
    print("Hello")
```

**Do this instead:**
```python
if 3 < 5:
    print("Hello")
# Output: Hello
```

---

## The `else` Statement

Use the `else` statement to define code that runs if the `if` condition is `False`.

### Example:
```python
a = True
if a:
    print("Hello")
else:
    print("Goodbye")
# Output: Hello

a = False
if a:
    print("Hello")
else:
    print("Goodbye")
# Output: Goodbye
```

**Note:**
- `else` must directly follow the `if` block.
- You cannot have unrelated code between an `if` and its `else`.

```python
if a:
    print("Hello")
else:
    print("Goodbye")
# Output: Goodbye
```

---

## The `elif` Statement

The `elif` (short for "else if") statement allows you to test multiple conditions. Python evaluates `elif` conditions in order and executes the first one that evaluates to `True`. Remaining `elif` blocks are skipped.

### Example:
```python
a = 5
if a > 10:
    print("Greater than 10")
elif a < 10:
    print("Less than 10")
elif a < 20:
    print("Less than 20")
else:
    print("Dunno")
# Output: Less than 10
```

You can use as many `elif` statements as needed.

---



---

# `while` Loops in Python

`while` loops are a special type of loop in Python. Unlike `for` loops, which iterate over a sequence, `while` loops continue to run as long as a condition is `True`. They are particularly useful when the number of iterations isn’t predetermined.

---

## Syntax:
```python
while condition:
    # Code to execute as long as the condition is True
```

---

## Example: Using a Sentinel Value

A **sentinel value** is a variable that changes during the loop to eventually make the loop condition `False`.

```python
counter = 0
max = 4

while counter < max:
    print(f"The count is: {counter}")
    counter = counter + 1
# Output:
# The count is: 0
# The count is: 1
# The count is: 2
# The count is: 3
```

---

## Warning: Infinite Loops

If the sentinel value is not updated, the condition will always evaluate to `True`, resulting in an **infinite loop**. You can stop an infinite loop by pressing `Ctrl-C`.

### Example of an Infinite Loop:
```python
counter = 0
max = 4

while counter < max:
    print(f"The count is: {counter}")
# Output (repeats forever):
# The count is: 0
# The count is: 0
# The count is: 0
# ...
# Press Ctrl-C to exit.
```

To avoid infinite loops, always ensure the sentinel value is updated within the loop.

---



---

# `break`, `continue`, and `return`

`break`, `continue`, and `return` are essential control statements in Python that allow you to manage the flow of your loops and functions.

---

## Using `break`

The `break` statement **completely exits** the current loop, skipping any remaining iterations or statements within the loop.

### Example:
```python
names = ["Rose", "Max", "Nina", "Phillip"]
for name in names:
    print(f"Hello, {name}")
    if name == "Nina":
        break
# Output:
# Hello, Rose
# Hello, Max
# Hello, Nina
```

---

## Using `continue`

The `continue` statement skips the remaining code in the current iteration and moves to the next iteration of the loop.

### Example:
```python
for name in names:
    if name != "Nina":
        continue
    print(f"Hello, {name}")
# Output:
# Hello, Nina
```

---

## `break` and `continue` Visualized

Consider this example:
```python
names = ["Jimmy", "Rose", "Max", "Nina", "Phillip"]

for name in names:
    if len(name) != 4:
        continue  # Skip names that do not have 4 characters

    print(f"Hello, {name}")

    if name == "Nina":
        break  # Exit the loop if "Nina" is found
print("Done!")
# Output:
# Hello, Rose
# Hello, Max
# Hello, Nina
# Done!
```

---

## `break` and `continue` in Nested Loops

`break` and `continue` affect only the **current loop**. For nested loops, `break` will exit the inner loop, and the outer loop will continue to run.

### Example:
```python
names = ["Rose", "Max", "Nina"]
target_letter = 'x'

for name in names:
    print(f"{name} in outer loop")
    for char in name:
        if char == target_letter:
            print(f"Found {name} with letter: {target_letter}")
            print("breaking out of inner loop")
            break
# Output:
# Rose in outer loop
# Max in outer loop
# Found Max with letter: x
# breaking out of inner loop
# Nina in outer loop
```

---

## Using `break` and `continue` in `while` Loops

You can use `break` and `continue` in `while` loops as well. This is especially useful for indefinite (`while True`) loops.

### Example:
```python
count = 0
while True:
    count += 1
    if count == 5:
        print("Count reached")
        break  # Exit the loop when the count reaches 5
# Output:
# Count reached
```

**Warning:** Ensure your condition eventually evaluates to `True` to avoid infinite loops.

---

## Using `return` in Loops

The `return` statement **exits the loop and the function** immediately, returning a specified value.

### Example:
```python
def name_length(names):
    for name in names:
        print(name)
        if name == "Nina":
            return "Found the special name"

names = ["Max", "Nina", "Rose"]
result = name_length(names)
print(result)
# Output:
# Max
# Nina
# Found the special name
```

---


Practice: Control Statements and Looping

This section provides examples and exercises for mastering Python's control statements (if, else, elif) and looping constructs (for, while, break, continue, return).
Branching with if, else, and elif
Example 1: Testing Numbers

The if, elif, and else statements allow you to add branching logic to your code.
Python

def test_number(number):
    if number < 100:
        print("This is a pretty small number")
    elif number == 100:
        print("This number is alright")
    else:
        print("This number is huge!")

test_number(5)
test_number(99)
test_number(100)
test_number(8675309)
# Output:
# This is a pretty small number
# This is a pretty small number
# This number is alright
# This number is huge!

Example 2: if Statements with Multiple Conditions

Using and or or in if statements:
Python

def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz!")

fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)
# Output:
# Fizzbuzz!

Example 3: Testing for Empty Lists

Use if to check for empty lists or special values like None:
Python

def my_func(my_list):
    if my_list:
        for item in my_list:
            if item is None:
                print("Got None!")
            else:
                print(item)
    else:
        print("Got an empty list!")

my_func([1, 2, 3])
my_func([2, None, "hello", 42])
my_func([])
# Output:
# 1
# 2
# 3
# 2
# Got None!
# hello
# 42
# Got an empty list!

Looping with for, range(), and enumerate()
Example 1: Iterating Over a List
Python

my_list = [0, 1, 2]
for num in my_list:
    print(f"Next value: {num}")
# Output:
# Next value: 0
# Next value: 1
# Next value: 2

Example 2: Using range()

Loop over a range of numbers:
Python

for num in range(0, 3):
    print(f"Next value: {num}")
# Output:
# Next value: 0
# Next value: 1
# Next value: 2

Example 3: Using enumerate()

Get the index and value of each item in a list:
Python

my_list = ["foo", "bar", "baz"]
for index, item in enumerate(my_list):
    print(f"Item {index}: {item}")
# Output:
# Item 0: foo
# Item 1: bar
# Item 2: baz

Looping Over Dictionaries
Example 1: Looping Over Keys
Python

my_dict = {"foo": "bar", "hello": "world"}
for key in my_dict:
    print(f"Key: {key}")
# Output:
# Key: foo
# Key: hello

Example 2: Looping Over Values
Python

for value in my_dict.values():
    print(f"Value: {value}")
# Output:
# Value: bar
# Value: world

Example 3: Looping Over Key-Value Pairs
Python

for key, value in my_dict.items():
    print(f"Item {key} = {value}")
# Output:
# Item foo = bar
# Item hello = world

Using break, continue, and return
Example 1: Using break

Exit the loop when a condition is met:
Python

for num in range(0, 100):
    print(f"Testing number {num}")
    if num == 3:
        print("Found number 3!")
        break
# Output:
# Testing number 0
# Testing number 1
# Testing number 2
# Testing number 3
# Found number 3!

Example 2: Using continue

Skip the rest of the loop and go to the next iteration:
Python

for num in range(0, 100):
    print(f"Testing number {num}")
    if num < 3:
        continue
    elif num == 5:
        print("Found number 5!")
        break
    print("Not yet...")
# Output:
# Testing number 0
# Testing number 1
# Testing number 2
# Testing number 3
# Not yet...
# Testing number 4
# Not yet...
# Testing number 5
# Found number 5!

Example 3: Using return

Exit a loop within a function and optionally return a value:
Python

def is_number_in_list(number_to_check, list_to_search):
    for num in list_to_search:
        print(f"Checking {num}...")
        if num == number_to_check:
            return True
    return False

my_list = [1, 2, 3, 4, 5]
print(is_number_in_list(27, my_list))  # Output: False
print(is_number_in_list(2, my_list))  # Output: True

while Loops
Example 1: Basic while Loop

Loop while a condition is met:
Python

counter = 0
while counter < 3:
    print(f"Counter = {counter}")
    counter += 1
# Output:
# Counter = 0
# Counter = 1
# Counter = 2

Example 2: Infinite Loop with break
Python

counter = 0
while True:
    print(f"Counter = {counter}")
    if counter == 3:
        break
    counter += 1
# Output:
# Counter = 0
# Counter = 1
# Counter = 2
# Counter = 3

Nested Loops
Example 1: Breaking Out of Inner Loops
Python

names = ["Rose", "Max", "Nina"]
target_letter = 'x'
found = False

for name in names:
    for char in name:
        if char == target_letter:
            found = True
            break
    if found:
        print(f"Found {name} with letter: {target_letter}")
        break
# Output:
# Found Max with letter: x

Example 2: Inner and Outer Loop Interaction
Python

for x in range(0, 5):
    for y in range(0, 5):
        print(f"x = {x}, y = {y}")
        if y == 2:
            break
# Output:
# x = 0, y = 0
# x = 0, y = 1
# x = 0, y = 2
# x = 1, y = 0
# ...

---

# Working With Python Programs

The Python REPL (Read-Eval-Print Loop) is an incredibly useful tool for quickly learning new Python concepts and testing your assumptions. However, it is not ideal for saving or sharing code. 

To ensure your code can be reused and shared, save it into project files. By doing this, you can run the code repeatedly and share it with others for collaboration or review.

---



---

# How to Run Python Programs

This section explains how to create and execute Python files, including tips for naming files and running them via VS Code or a terminal.

---

## Creating Python Files with the *.py Extension

A file is recognized as a Python program when its name ends with a `.py` extension.

### Naming Tips
Python’s PEP8 guidelines suggest the following best practices for naming Python files:
- Filenames should be **all lowercase**.
- Use underscores (`_`) to separate words.
- Keep filenames **short**.

#### ✅ Good Examples:
- `apis.py`
- `exceptions.py`
- `personal_blog.py`

#### ⛔️ Bad Examples:
- `MYFILE.PY`
- `CamelCaseFile.py`
- `really_long_over_descriptive_project_file_name.py`

---

## What Are *.pyc Files?

- Python code can be compiled into intermediary `.pyc` files for optimization.
- **Good news:** You don’t have to worry about these files in most cases.
- **Bad news:** Occasionally, stale versions of `.pyc` files can cause problems.

To safely delete `.pyc` files from the current project directory, run:
```bash
find . -name "*.pyc" -delete
```
*(Linux or macOS)*

---

## Git Tip: Use a `.gitignore` for Python

When using Git for source control, ensure that `.pyc` files are ignored to avoid committing them to your repository.

To do this, add a standard `.gitignore` file for Python to your project.

---

## Running Python Files From VS Code

### Creating New Python Files
1. Open a new file in VS Code:
   - **Windows/Linux:** `Ctrl+N`
   - **Mac OS:** `⌘N` (Command + N)
2. Save the file with a `.py` extension.

#### Example:
Create a file called `hello.py` in your project directory with the following contents:
```python
# in file: hello.py
greetings = ["Hello", "Bonjour", "Hola"]

for greeting in greetings:
    print(f"{greeting}, World!")
```

---

### Opening the VS Code Terminal
1. Open the terminal in VS Code:
   - **Shortcut:** `Ctrl + `` (backtick)`
2. If the Python REPL is open, switch to a shell-enabled terminal (e.g., one labeled `1:`).

---

### Running the File
1. Open the command palette:
   - **Windows/Linux:** `Ctrl+Shift+P`
   - **Mac OS:** `⌘⇧P` (Command + Shift + P)
2. Select **Python: Run Python File in Terminal**.

#### Output:
You should see:
```
Hello, World!
Bonjour, World!
Hola, World!
```

---

## Running Python Files From a Non-VS Code Terminal

To run a Python file from any terminal:
1. Open your terminal.
2. Navigate to the directory containing your Python file:
   ```bash
   cd /path/to/your/code
   ```
3. Run the Python file:
   ```bash
   python hello.py
   ```

#### Example Output:
```
Hello, World!
Bonjour, World!
Hola, World!
```

This also works in the VS Code terminal.

---



---

# Printing Tips in Python

When running Python scripts from files, the output doesn’t automatically appear like it does in the REPL. To see any output, you’ll need to use the `print()` function. This section also covers debugging with `print()` and formatting your terminal output for better readability.

---

## **Basic Printing**

In the Python REPL, typing a variable name automatically displays its value:
```python
>>> name = "Nina"  
>>> name  
'Nina'
```

However, when running Python files, you must explicitly use `print()` to see output.

### Example:
```python
# file: name.py
name = "Nina"
name
```
**Output:**
```
(env) $ python name.py
# No output
```

```python
# file: print_name.py
name = "Nina"
print(name)
```
**Output:**
```
(env) $ python print_name.py
Nina
```

---

## **Debugging Your Code with `print()`**

The `print()` function is a great tool for beginners to debug their code by displaying variable values or program flow.

### Example:
```python
# file: mystery.py
def mystery():
    num = 10 * 3

    if num == 10:
        print("Num was equal to 10")
        num = num * 10
    if num == 20:
        print("Num was equal to 20")
        num = num * 20
    if num == 30:
        print("Num was equal to 30")
        num = num * 30

    print(f"Value of returned num is: {num}")
    return num

mystery()
```
**Output:**
```
Num was equal to 30
Value of returned num is: 900
```

⚠️ **Tip:** Remove debugging `print()` statements before sharing or deploying your code. As you advance, consider using a debugger like Python’s built-in `pdb` for a deeper understanding of your code.

---

## **Output Formatting Tips**

### Use New Lines and Tabs
Control characters like `\n` and `\t` allow you to format your output for better readability.

#### Example:
```python
# file: formatting_example.py
print("\nExtra New Line Before")
print("One Print\nTwo New Lines!")
print("Extra New Line After\n")

print("\t Here's some tabbed output.")

print("\nOne Print\n\tOne Tab")
```

**Output:**
```
Extra New Line Before
One Print
Two New Lines!
Extra New Line After

         Here's some tabbed output.

One Print
        One Tab
```

---

## **Pretty Printing with `pprint`**

When printing large data structures like lists or dictionaries, the default output can be hard to read. Python's `pprint` module formats the output in a more readable way.

### Example:
```python
long_list = list(range(23))

# Normal print
print(long_list)

# Pretty print
from pprint import pprint
pprint(long_list)
```

**Output:**
```
# Normal print
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

# Pretty print
[0,
 1,
 2,
 3,
 4,
 5,
 6,
 7,
 8,
 9,
 10,
 11,
 12,
 13,
 14,
 15,
 16,
 17,
 18,
 19,
 20,
 21,
 22]
```

`pprint` is especially useful as your programs grow in complexity.

--- 


---

# The `main` Method in Python

As your Python programs grow in complexity, you may want to include a `main` method. The purpose of the `main` method is to ensure that certain parts of your code only run when the program is executed as a standalone script, not when it’s imported as a module into another program.

---

## **Why Use a `main` Method?**

When Python imports a file as a module, all code outside of functions or classes is executed immediately. This can lead to unintended behavior if the imported file contains print statements or other executable code.

### Example: Without `main`
**File: `name_lib.py`**
```python
def name_length(name):
    return len(name)

def upper_case_name(name):
    return name.upper()

def lower_case_name(name):
    return name.lower()

name = "Nina"
length = name_length(name)
upper_case = upper_case_name(name)

print(f"The length is {length} and the uppercase version is: {upper_case}")
```

When running the file directly:
```bash
(env) $ python name_lib.py
The length is 4 and the uppercase version is: NINA
```

But when importing it:
**File: `other_program.py`**
```python
import name_lib

my_name = "Fred"

my_length = name_lib.name_length(my_name)
my_lower_case = name_lib.lower_case_name(my_name)

print(f"In my code, my length is {my_length} and my lower case name is: {my_lower_case}")
```

Running the file:
```bash
(env) $ python other_program.py
The length is 4 and the uppercase version is: NINA
In my code, my length is 4 and my lower case name is: fred
```

Unintended output (`Nina`’s details) appears because the code in `name_lib.py` is executed when imported.

---

## **Using the `__name__` Variable**

Python provides a special variable `__name__` to check how a file is being executed:
- If the file is executed directly, `__name__` is set to `"__main__"`.
- If the file is imported as a module, `__name__` is set to the name of the file (minus the `.py` extension).

### Example:
**File: `name_lib.py`**
```python
print(f"The value of __name__ is: {__name__}")
```

Running the file directly:
```bash
(env) $ python name_lib.py
The value of __name__ is: __main__
```

Importing the file:
```bash
(env) $ python other_program.py
The value of __name__ is: name_lib
```

---

## **Adding a `main` Conditional**

To prevent unintended execution, wrap your executable code in a conditional block:
```python
if __name__ == "__main__":
    # Code here runs only when the file is executed directly
```

### Updated Example:
**File: `name_lib.py`**
```python
def name_length(name):
    return len(name)

def upper_case_name(name):
    return name.upper()

def lower_case_name(name):
    return name.lower()

if __name__ == "__main__":
    name = "Nina"
    length = name_length(name)
    upper_case = upper_case_name(name)

    print(f"The length is {length} and the uppercase version is: {upper_case}")
```

Now, when running `other_program.py`:
```bash
(env) $ python other_program.py
In my code, my length is 4 and my lower case name is: fred
```

No unintended output from `name_lib.py` appears.

---

## **Benefits of Using `main`**
- Ensures your program works correctly when both executed directly and imported as a module.
- Encourages reusable and modular code.
- Follows a common Python programming pattern, improving code readability and maintainability.

---


---

# Working With Files in Python

Python makes it easy to work with files using the built-in `open()` function. This section covers the basics of opening, reading, and working with files safely using context managers.

---

## **Opening Files with `open()`**

The `open()` function allows you to open files in various modes. It returns a file object that can be used to read or write data.

### Syntax:
```python
open(file, mode='r')
```

### Common Modes:
| Mode | Description |
|------|-------------|
| `'r'` | Open for reading (default). |
| `'w'` | Open for writing, truncating the file first. |
| `'x'` | Open for exclusive creation; fails if the file already exists. |
| `'a'` | Open for writing, appending to the file if it exists. |
| `'b'` | Binary mode. |
| `'t'` | Text mode (default). |
| `'+'` | Open for updating (reading and writing). |

### Examples:
```python
# Open a file for reading
my_file = open("my_file.txt")

# Open a file for writing (replaces any existing file)
my_file = open("my_file.txt", "w")

# Open a file for appending (adds to the end of the file)
my_file = open("my_file.txt", "a")
```

### Important:
Always close the file after you're done working with it to avoid leaving open file handles:
```python
my_file.close()
```

---

## **Using Context Managers**

A **Context Manager** ensures that resources like files are properly opened and closed, even if an error occurs. The `open()` function can be used as a context manager with the `with` statement.

### Example:
```python
# Safely open and read a file
with open("my_file.txt") as my_file:
    contents = my_file.read()
# File is automatically closed after the 'with' block
```

Benefits of using a context manager:
- Automatically closes the file when the block is exited.
- Ensures proper cleanup, even if an exception occurs.

---

## **Working with JSON Files**

You can work with JSON files by using the `json` module. This is especially useful for structured data.

### Example:
1. **Create a JSON File:**
   Assume you have a file called `cities.json` with the following contents:
   ```json
   [
       {"name": "New York", "pop": 8550405},
       {"name": "Los Angeles", "pop": 3971883},
       {"name": "Chicago", "pop": 2720546},
       {"name": "Houston", "pop": 2296224},
       {"name": "Philadelphia", "pop": 1567442}
   ]
   ```

2. **Read the JSON File:**
   ```python
   import json

   with open("cities.json") as cities_file:
       cities_data = json.load(cities_file)
       print(cities_data)
   # Output:
   # [{'name': 'New York', 'pop': 8550405}, {'name': 'Los Angeles', 'pop': 3971883}, 
   # {'name': 'Chicago', 'pop': 2720546}, {'name': 'Houston', 'pop': 2296224}, 
   # {'name': 'Philadelphia', 'pop': 1567442}]
   ```

The `json.load()` function parses the JSON data into Python objects, such as lists and dictionaries.

---

## **Key Takeaways**
- Use `open()` to work with files.
- Always close files using `.close()` or, better yet, use a context manager (`with` statement) to handle file operations safely.
- Use the `json` module for working with JSON files.



---

# Practice: Running Code

This section walks through writing and running Python programs with a focus on the `main()` function, file handling, and exception management.

---

## **Creating a Basic Framework**

Start with a basic `main()` function and a standard conditional to run it:

```python
def main():
    pass

if __name__ == "__main__":
    main()
```

### Running the File
Save the file as `file_exercise.py` and run it using the following command:
```bash
python file_exercise.py
```

### What Happens?
When run directly, the `__name__` variable is set to `"__main__"`, triggering the `if` block to call the `main()` function. The `pass` keyword is used as a placeholder to prevent a syntax error. 

This pattern is common in Python programs and allows the file to work both as a standalone program and as an importable module.

---

## **Working with Files**

### Loading JSON Data
Let’s expand the `main()` function to read and parse a JSON file named `cities.json`, which contains the top 5 U.S. cities by population:

**File: `file_exercise.py`**
```python
import json

def main():
    cities_file = open("cities.json")
    cities_data = json.load(cities_file)
    print(cities_data)

if __name__ == "__main__":
    main()
```

**Command Line Output:**
```bash
[{'name': 'New York', 'pop': 8550405}, {'name': 'Los Angeles', 'pop': 3971883}, {'name': 'Chicago', 'pop': 2720546}, {'name': 'Houston', 'pop': 2296224}, {'name': 'Philadelphia', 'pop': 1567442}]
```

---

### Formatting Output with `enumerate()`
Use `enumerate()` to print the data in a user-friendly way:

```python
import json

def main():
    cities_file = open("cities.json")
    cities_data = json.load(cities_file)

    print("Largest cities in the US by population:")
    for index, entry in enumerate(cities_data):
        print(f"{index + 1}: {entry['name']} - {entry['pop']}")

if __name__ == "__main__":
    main()
```

**Command Line Output:**
```bash
Largest cities in the US by population:
1: New York - 8550405
2: Los Angeles - 3971883
3: Chicago - 2720546
4: Houston - 2296224
5: Philadelphia - 1567442
```

---

## **Using Context Managers**

To ensure files are properly closed, use the `with` keyword to handle file opening and closing automatically:

```python
import json

def main():
    with open("cities.json") as cities_file:
        cities_data = json.load(cities_file)

        print("Largest cities in the US by population:")
        for index, entry in enumerate(cities_data):
            print(f"{index + 1}: {entry['name']} - {entry['pop']}")

    print("The file is now closed.")

if __name__ == "__main__":
    main()
```

**Command Line Output:**
```bash
Largest cities in the US by population:
1: New York - 8550405
2: Los Angeles - 3971883
3: Chicago - 2720546
4: Houston - 2296224
5: Philadelphia - 1567442
The file is now closed.
```

---

## **Handling Exceptions**

Parsing files often involves dealing with errors. For example, if the `cities.json` file is malformed (e.g., missing the closing `]`), you’ll see a traceback with helpful debugging information.

### Example Traceback:
```bash
Traceback (most recent call last):
  File "file_exercise.py", line 6, in main
    cities_data = json.load(cities_file)
  File "/usr/lib/python3.9/json/__init__.py", line 293, in load
    return loads(fp.read(), ...)
json.decoder.JSONDecodeError: Expecting ',' delimiter: line 1 column 123 (char 122)
```

To handle this gracefully, use a `try`-`except` block:

```python
import json

def main():
    with open("cities.json") as cities_file:
        try:
            cities_data = json.load(cities_file)

            print("Largest cities in the US by population:")
            for index, entry in enumerate(cities_data):
                print(f"{index + 1}: {entry['name']} - {entry['pop']}")

        except json.decoder.JSONDecodeError as error:
            print("Sorry, there was an error decoding that JSON file:")
            print(f"\t{error}")

    print("The file is now closed.")

if __name__ == "__main__":
    main()
```

**Command Line Output (with malformed JSON):**
```bash
Sorry, there was an error decoding that JSON file:
	Expecting ',' delimiter: line 1 column 123 (char 122)
The file is now closed.
```

---

## **Key Points**
1. **`main()` Function**: Provides a reusable entry point for your program.
2. **JSON Handling**: Use the `json` library for parsing structured data.
3. **Context Managers**: Use `with` to safely handle file operations.
4. **Error Handling**: Use `try`-`except` blocks to catch and handle errors gracefully.

