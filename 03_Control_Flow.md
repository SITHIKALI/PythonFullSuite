# Boolean Logic

Boolean Logic allows you to test your assumptions and control the flow of your program. It is the foundation of decision-making in Python.

---

## Truthiness in Python

Evaluating expressions to determine their truthiness (`True` or `False`) helps control the flow of a program. Here's a cheat sheet and practical examples to help understand Python's truthiness rules.

### Truthiness Cheat Sheet
| Type | Truthiness Rule |
|------|-----------------|
| `int` | `0` is False, all other numbers (including negatives) are True. |
| Containers (`list`, `tuple`, `set`, `dict`) | Empty containers are False, containers with items are True. |
| `None` | Always evaluates to False. |

### Boolean Basics

`True` and `False` are keywords in Python. Avoid naming variables as `True` or `False` to prevent conflicts.

```python
>>> True
True
>>> False
False

# Test assumptions using the bool() function
>>> bool(3 < 5)
True
```

### Numbers

*   `0` evaluates to `False`.
*   All other numbers, including negative numbers, evaluate to `True`.

```python
>>> bool(0)    # Integer 0
False
>>> bool(1)    # Positive Integer
True
>>> bool(-1)   # Negative Integer
True
```

### Sequences (Lists, Tuples, Sets, Dictionaries)

*   Empty sequences always evaluate to `False`.
*   Non-empty sequences always evaluate to `True`.

```python
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
```

### None

The `None` type in Python represents nothing and always evaluates to `False`.

```python
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
```

### Key Takeaways

*   Use the `bool()` constructor to test the truthiness of an expression.
*   Be cautious when differentiating between `None` and empty sequences, as both evaluate to `False`.

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

# Loops and Control Statements

Loops and control statements allow us to control the logical flow of our program. These structures enable us to repeat actions, make decisions, and manage the execution of code based on specific conditions.

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

## Practice: Control Statements and Looping

This section provides examples and exercises for mastering Python's control statements (`if`, `else`, `elif`) and looping constructs (`for`, `while`, `break`, `continue`, `return`).

### Branching with if, else, and elif

#### Example 1: Testing Numbers
The `if`, `elif`, and `else` statements allow you to add branching logic to your code.

```python
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
```

#### Example 2: if Statements with Multiple Conditions
Using `and` or `or` in `if` statements:

```python
def fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz!")

fizzbuzz(3)
fizzbuzz(5)
fizzbuzz(15)
# Output:
# Fizzbuzz!
```

#### Example 3: Testing for Empty Lists
Use `if` to check for empty lists or special values like `None`:

```python
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
```

### Looping with for, range(), and enumerate()

#### Example 1: Iterating Over a List

```python
my_list = [0, 1, 2]
for num in my_list:
    print(f"Next value: {num}")
# Output:
# Next value: 0
# Next value: 1
# Next value: 2
```

#### Example 2: Using range()
Loop over a range of numbers:

```python
for num in range(0, 3):
    print(f"Next value: {num}")
# Output:
# Next value: 0
# Next value: 1
# Next value: 2
```

#### Example 3: Using enumerate()
Get the index and value of each item in a list:

```python
my_list = ["foo", "bar", "baz"]
for index, item in enumerate(my_list):
    print(f"Item {index}: {item}")
# Output:
# Item 0: foo
# Item 1: bar
# Item 2: baz
```

### Looping Over Dictionaries

#### Example 1: Looping Over Keys

```python
my_dict = {"foo": "bar", "hello": "world"}
for key in my_dict:
    print(f"Key: {key}")
# Output:
# Key: foo
# Key: hello
```

#### Example 2: Looping Over Values

```python
for value in my_dict.values():
    print(f"Value: {value}")
# Output:
# Value: bar
# Value: world
```

#### Example 3: Looping Over Key-Value Pairs

```python
for key, value in my_dict.items():
    print(f"Item {key} = {value}")
# Output:
# Item foo = bar
# Item hello = world
```

### Using break, continue, and return

#### Example 1: Using break
Exit the loop when a condition is met:

```python
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
```

#### Example 2: Using continue
Skip the rest of the loop and go to the next iteration:

```python
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
```

#### Example 3: Using return
Exit a loop within a function and optionally return a value:

```python
def is_number_in_list(number_to_check, list_to_search):
    for num in list_to_search:
        print(f"Checking {num}...")
        if num == number_to_check:
            return True
    return False

my_list = [1, 2, 3, 4, 5]
print(is_number_in_list(27, my_list))  # Output: False
print(is_number_in_list(2, my_list))  # Output: True
```

### while Loops

#### Example 1: Basic while Loop
Loop while a condition is met:

```python
counter = 0
while counter < 3:
    print(f"Counter = {counter}")
    counter += 1
# Output:
# Counter = 0
# Counter = 1
# Counter = 2
```

#### Example 2: Infinite Loop with break

```python
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
```

### Nested Loops

#### Example 1: Breaking Out of Inner Loops

```python
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
```

#### Example 2: Inner and Outer Loop Interaction

```python
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
```
