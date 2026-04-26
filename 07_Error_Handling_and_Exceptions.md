# Error Handling and Exceptions

When writing programs, things will inevitably go wrong. Whether it’s bad user input, a missing file, or a network failure, Python provides tools to handle these issues gracefully so your program doesn't crash unexpectedly.

## `try` and `except` Blocks

The `try` block lets you test a block of code for errors.
The `except` block lets you handle the error.

```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")
```

## Catching Specific Built-in Exceptions

It's best practice to catch specific exceptions rather than using a bare `except:`, which catches everything (including keyboard interrupts like Ctrl+C).

```python
try:
    with open("non_existent_file.txt", "r") as f:
        content = f.read()
except FileNotFoundError as e:
    print(f"Error: The file was not found. Details: {e}")
except Exception as e:
    # A fallback for catching any other uncaught errors
    print(f"An unexpected error occurred: {e}")
```

## The `else` and `finally` Blocks

*   **`else`**: Executes if the `try` block does *not* throw an error.
*   **`finally`**: Executes regardless of whether the `try` block succeeds or fails. It's often used for cleaning up resources.

```python
try:
    print("Trying to execute code...")
    # result = 10 / 0  # Uncomment to see the error branch
except ZeroDivisionError:
    print("An error occurred.")
else:
    print("Everything worked perfectly!")
finally:
    print("Cleanup operations happening here. This always runs.")
```

## Raising Exceptions

You can choose to throw an exception if a condition occurs using the `raise` keyword.

```python
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age is valid: {age}")

try:
    validate_age(-5)
except ValueError as e:
    print(f"Caught an exception: {e}")
```

## Creating Custom Exceptions

You can define your own exception classes by inheriting from Python's built-in `Exception` class.

```python
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError("You do not have enough money in your account.")
    return balance - amount

try:
    withdraw(100, 150)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")
```
