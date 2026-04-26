# Modern Python Features

Python is actively developed, and recent versions (Python 3.8 to 3.11+) have introduced incredibly powerful features that improve code readability, performance, and structure.

## Type Hinting

Python is dynamically typed, meaning you don't explicitly declare variable types. However, **Type Hinting** allows you to optionally specify expected data types. This improves IDE autocompletion and allows tools like `mypy` to catch bugs before you run the code.

```python
from typing import List, Dict, Optional

# The function expects a string and returns a string
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Type hinting lists and dictionaries
def process_scores(scores: List[int]) -> float:
    return sum(scores) / len(scores)

# Optional types (can be string or None)
def get_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None
```

## The Walrus Operator (`:=`)

Introduced in Python 3.8, the assignment expression operator (nicknamed the "walrus operator") allows you to assign and return a value in the same expression.

```python
# The old way
data = "some long string"
n = len(data)
if n > 10:
    print(f"String is too long ({n} characters)")

# With the Walrus Operator
data = "some long string"
if (n := len(data)) > 10:
    print(f"String is too long ({n} characters)")
```
It is particularly useful in `while` loops:
```python
# Continuously read user input until they type 'quit'
while (command := input("> ")) != "quit":
    print(f"You entered: {command}")
```

## Structural Pattern Matching (`match` / `case`)

Introduced in Python 3.10, structural pattern matching is similar to `switch` statements in other languages, but it's much more powerful. It can unpack data structures and match complex patterns.

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            # The underscore acts as the default / wildcard catch-all
            return "Something's wrong with the internet"

print(http_error(404))
```

Matching with unpacking:
```python
def handle_point(point):
    match point:
        case (0, 0):
            print("Origin")
        case (0, y):
            print(f"Y={y}")
        case (x, 0):
            print(f"X={x}")
        case (x, y):
            print(f"X={x}, Y={y}")
        case _:
            print("Not a point")

handle_point((0, 5)) # Output: Y=5
```
