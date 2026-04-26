# Advanced Functions and Comprehensions

Python provides several advanced functional programming tools that allow you to write cleaner, more "Pythonic" code.

## Comprehensions

Comprehensions provide a concise way to create lists, dictionaries, and sets.

### List Comprehensions
Instead of writing a `for` loop to build a list, you can do it in one line.
```python
# Old way
squares = []
for i in range(5):
    squares.append(i * i)

# List Comprehension
squares = [i * i for i in range(5)]
print(squares)  # Output: [0, 1, 4, 9, 16]

# With conditionals
evens = [i for i in range(10) if i % 2 == 0]
print(evens)  # Output: [0, 2, 4, 6, 8]
```

### Dictionary Comprehensions
```python
squares_dict = {i: i * i for i in range(3)}
print(squares_dict)  # Output: {0: 0, 1: 1, 2: 4}
```

## Lambda Functions

A lambda function is a small anonymous function. It can take any number of arguments, but can only have one expression.

```python
# lambda arguments: expression
multiply = lambda a, b: a * b
print(multiply(5, 6))  # Output: 30
```

## Map, Filter, and Reduce

These built-in functions are commonly used with lambdas.

*   **map()**: Applies a function to all items in an input list.
*   **filter()**: Creates a list of elements for which a function returns true.
*   **reduce()**: Applies a rolling computation to sequential pairs of values in a list.

```python
numbers = [1, 2, 3, 4, 5]

# map
squared = list(map(lambda x: x*x, numbers))
# [1, 4, 9, 16, 25]

# filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
# [2, 4]

from functools import reduce
# reduce
summed = reduce(lambda x, y: x + y, numbers)
# 15
```

## Generators and `yield`

Generators are a simple way of creating iterators. Instead of using `return` in a function, you use `yield`. Generators don't store the entire result in memory; they yield one result at a time.

```python
def count_up_to(max):
    count = 1
    while count <= max:
        yield count
        count += 1

counter = count_up_to(3)
print(next(counter))  # 1
print(next(counter))  # 2
print(next(counter))  # 3
# Calling next() again would raise a StopIteration exception
```

## Decorators

Decorators allow you to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# Output:
# Something is happening before the function is called.
# Hello!
# Something is happening after the function is called.
```
