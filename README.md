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
