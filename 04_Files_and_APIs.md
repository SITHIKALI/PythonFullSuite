# Working With Python Programs

The Python REPL (Read-Eval-Print Loop) is an incredibly useful tool for quickly learning new Python concepts and testing your assumptions. However, it is not ideal for saving or sharing code. 

To ensure your code can be reused and shared, save it into project files. By doing this, you can run the code repeatedly and share it with others for collaboration or review.

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

To interact with APIs in Python, you commonly use the `requests` library, which provides a simple and intuitive way to send HTTP requests and handle responses. Here's a step-by-step guide:

---

## **Working with APIs in Python**

### 1. **Install the `requests` Library**
If you don't already have the `requests` library installed, you can install it using:
```bash
pip install requests
```

---

### 2. **Basic HTTP Requests**
The `requests` library supports various HTTP methods like `GET`, `POST`, `PUT`, and `DELETE`.

#### Example: Basic `GET` Request
```python
import requests

response = requests.get("https://api.example.com/data")
print(response.status_code)  # HTTP status code (e.g., 200 for success)
print(response.json())       # Parse response as JSON
```

---

### 3. **Sending Parameters in Requests**
You can include query parameters in your request using the `params` keyword.

#### Example:
```python
url = "https://api.example.com/search"
params = {"query": "python", "page": 1}

response = requests.get(url, params=params)
print(response.url)  # Full URL with query parameters
print(response.json())
```

---

### 4. **Making POST Requests**
To send data to an API, use the `POST` method with the `data` or `json` keyword.

#### Example:
```python
url = "https://api.example.com/create"
data = {"name": "John", "age": 30}

response = requests.post(url, json=data)  # Use 'json=' for JSON payloads
print(response.status_code)
print(response.json())
```

---

### 5. **Working with Headers**
Some APIs require additional headers for authentication, content type, etc.

#### Example:
```python
url = "https://api.example.com/protected"
headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}

response = requests.get(url, headers=headers)
print(response.status_code)
print(response.json())
```

---

### 6. **Error Handling**
Always handle errors gracefully to avoid crashes.

#### Example:
```python
try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx/5xx)
    print(response.json())
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
```

---

### 7. **Working with APIs that Require Authentication**
Many APIs require authentication through methods like API keys, OAuth tokens, or basic authentication.

#### Example: API Key
```python
url = "https://api.example.com/data"
headers = {"x-api-key": "YOUR_API_KEY"}

response = requests.get(url, headers=headers)
print(response.json())
```

---

### 8. **Interacting with JSON Responses**
API responses are often in JSON format. Use Python's dictionary methods to extract data.

#### Example:
```python
response = requests.get("https://api.example.com/data")
data = response.json()

for item in data["results"]:
    print(item["name"], item["value"])
```

---

### 9. **Rate Limiting**
Some APIs limit the number of requests you can make. Always check the API documentation for rate limits.

#### Example:
Respect rate limits by adding delays between requests:
```python
import time

for i in range(5):
    response = requests.get("https://api.example.com/data")
    print(response.json())
    time.sleep(1)  # Delay for 1 second
```

---

### 10. **API Documentation**
Always refer to the API's documentation for:
- Endpoints and their methods (`GET`, `POST`, etc.).
- Required headers and parameters.
- Authentication mechanisms.
- Rate limits and error codes.

---

# What Is an API?

An API (Application Programming Interface) is:

> A set of functions and procedures allowing the creation of applications that access the features or data of an operating system, application, or other service.

APIs provide a standardized way to access information across the web, enabling communication between clients and servers. Most modern APIs are **RESTful**, meaning they follow a common set of paradigms and practices.

---

## **Key Concepts**

### **Authentication**
- Some APIs require authentication to use their services.
- Authentication methods are beyond the scope of this guide, but many APIs are available for free and require no authentication.

---

### **Rate Limiting**
- Even if authentication isn’t required, APIs often implement **rate limiting** to prevent overloading their servers.
- For example:
  - The GitHub API allows **50 unauthenticated requests per hour per IP**.
  - The GitHub Search API allows **10 unauthenticated requests per hour**.

---

### **Free APIs**
- Free APIs are publicly available and don’t require payment, but they may lack guaranteed uptime or maintenance.
- If a free API becomes unavailable, you can explore alternatives in the [public-apis repository](https://github.com/public-apis/public-apis).

---

# Working with APIs

APIs (Application Programming Interfaces) allow you to interact with servers and services over the web by sending requests and receiving responses. This section provides an introduction to the basic concepts of working with APIs.

---

## **Requests and Responses**

APIs work on the **request-response cycle**:
- You send a **request** to the server.
- The server responds with:
  - An **HTTP Status Code** (indicating success or failure).
  - Optionally, **data** in a specific format (e.g., JSON).

---

## **HTTP Methods**

HTTP methods (or verbs) specify the type of operation you want to perform:
- **GET**: Retrieve a resource from the server.
- **POST**: Create a new resource on the server with the data you provide.
- **PUT**: Edit or update an existing resource.
- **DELETE**: Remove a resource from the server.

---

## **Headers, Body, and Parameters**

You can include extra information in your requests:
- **Headers**: Metadata about the request (e.g., authentication tokens, content type).
- **Body**: Data to send with the request (e.g., for POST or PUT).
- **URL Parameters**: Key-value pairs added to the URL.  
  Example:  
  `https://example.com?var1=foo&var2=bar`

---

## **Response Types**

API responses are typically returned in various formats, with **JSON** being the most common.

### Example JSON Response:
```json
[
    {
        "name": "New York",
        "pop": 8550405
    },
    {
        "name": "Los Angeles",
        "pop": 3971883
    },
    {
        "name": "Chicago",
        "pop": 2720546
    },
    {
        "name": "Houston",
        "pop": 2296224
    },
    {
        "name": "Philadelphia",
        "pop": 1567442
    }
]
```

JSON is widely used because it is easy to read, write, and generate in various programming languages.

---

## **HTTP Status Codes**

HTTP Status Codes indicate whether your request was successful or why it failed. Here are the common categories:

| **Category** | **Description**                     | **Examples**                                      |
|--------------|-------------------------------------|--------------------------------------------------|
| **1xx**      | Informational                      | Rarely used.                                    |
| **2xx**      | Success                            | `200 OK`: Standard success response.            |
|              |                                     | `201 CREATED`: Resource created successfully.   |
| **3xx**      | Redirection                        | `301 Moved Permanently`: Resource moved to a new URL. |
| **4xx**      | Client Error                       | `404 Not Found`: Resource not found.            |
| **5xx**      | Server Error                       | `500 Internal Server Error`: Server encountered an issue. |

---

## **Fun Fact: I'm a Teapot (HTTP Status Code 418)**

HTTP Status Code `418` was introduced as an April Fool’s joke in 1998, known as the **Hyper Text Coffee Pot Control Protocol (HTCPCP)**. It signifies:  
> "I’m a Teapot."  

You can "brew" coffee by sending the `BREW` command to servers supporting this protocol. 🫖

---

## **Authentication**

Some APIs require authentication to use their services. While authentication methods are beyond the scope of this section, you can explore the following resources for more information:
- [Zapier - Authentication Part 1](https://zapier.com) and [Part 2](https://zapier.com) by Brian Cooksey.
- [Requests Library Authentication Documentation](https://docs.python-requests.org/en/master/user/authentication/).

---

## **Rate Limiting**

APIs often enforce **rate limits** to prevent overloading servers. 
- Example: The GitHub API allows:
  - **50 unauthenticated requests per hour per IP** for general requests.
  - **10 unauthenticated requests per hour** for their Search API.

For more free APIs to explore, check out the [public-apis repository](https://github.com/public-apis/public-apis).

---

# Using the `requests` Library

The `requests` library is an external Python library designed to simplify working with HTTP requests. It was developed by Kenneth Reitz and is often described as "HTTP for humans." It has become one of the most popular Python libraries thanks to its ease of use.

---

## **Installing the `requests` Library**

If you haven’t installed the `requests` library yet, you can do so using `pip`:
```bash
python -m pip install requests
```

---

## **Our First Request Using `requests`**

Let’s make a request to the [Shibe API](http://shibe.online) to get a random dog picture.

**File: `shibe.py`**
```python
# Import the requests library
import requests

# Define the API URL
api_url = "http://shibe.online/api/shibes?count=1"

# Make a GET request to the API
response = requests.get(api_url)

# Check the response status code
print(f"Response status code is: {response.status_code}")

# Parse the response as JSON
response_json = response.json()

# Print the resulting list of URLs
print(response_json)
```

**Run the script:**
```bash
(env) $ python shibe.py
Response status code is: 200
['https://cdn.shibe.online/shibes/28d7c372ea7defdb315ef845285d4ac3906ccea4.jpg']
```

---

## **Dealing with Errors**

HTTP status codes are a good indicator of whether your request was successful.

### Example: Handling a 404 Error
```python
# Make a request to a non-existent endpoint
bad_response = requests.get("http://shibe.online/api/german-shepards")

# Print the status code
print(f"Bad Response Status Code is: {bad_response.status_code}")
```

**Output:**
```bash
Bad Response Status Code is: 404
```

---

## **Passing Parameters**

You can pass query parameters to the API using the `params` argument.

### Example: Requesting Multiple Dog Pictures
```python
# Base API URL
api_url = "http://shibe.online/api/shibes"

# Define query parameters
params = {
   "count": 10  # Request 10 dog pictures
}

# Make the GET request with parameters
api_response = requests.get(api_url, params=params)

# Print the status code
print(f"Shibe API Response Status Code is: {api_response.status_code}")

# Parse the response as JSON
json_data = api_response.json()

# Print the list of image URLs
print("Here is a list of URLs for dog pictures:")
for url in json_data:
    print(f"\t {url}")
```

**Run the script:**
```bash
(env) $ python shibe.py
Shibe API Response Status Code is: 200
Here is a list of URLs for dog pictures:
     https://cdn.shibe.online/shibes/dfb2af0b2ac1f057750da32f0ea0e154afc160cf.jpg
     https://cdn.shibe.online/shibes/4989daad2c805ec62b0fb09a80280ba2262f1b08.jpg
     ...
```

---

## **More About `requests`**

To dive deeper into the `requests` library, check out the [quick start documentation](https://docs.python-requests.org/en/latest/user/quickstart/).

---

# Practice: Bringing It All Together

Let’s review the concepts we covered today by building a program that interacts with the GitHub API to retrieve the top repositories sorted by the number of stars.

---

## **Objective**

Create a program, `day_one.py`, that:
1. Fetches repositories with more than 50,000 stars, filtered by specific programming languages.
2. Sorts repositories by the number of stars in descending order.
3. Handles errors gracefully and allows customization of search parameters.

---

## **Setup**

1. Install the `requests` library if you haven’t already:
   ```bash
   python -m pip install requests
   ```

2. Create a file named `day_one.py`.

---

## **Step 1: Making the Initial Request**

Start by creating a function to make a `GET` request to the GitHub search API. Use the `if __name__ == "__main__"` block to ensure the program runs only when executed directly.

**Code Example:**
```python
import requests

def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    response = requests.get(gh_api_repo_search_url)
    print(f"Response status code is: {response.status_code}")

if __name__ == "__main__":
    repos_with_most_stars()
```

---

## **Step 2: Adding Query Parameters**

Add a query string to search for repositories with more than 50,000 stars. Update the request to include this query using the `params` argument.

**Code Example:**
```python
def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    params = {
        "q": "stars:>50000"
    }
    response = requests.get(gh_api_repo_search_url, params=params)
    print(f"Response status code is: {response.status_code}")
    print(f"Response data: {response.json()}")
```

---

## **Step 3: Parsing the Response**

Parse the JSON response to extract useful information like repository name, stars, and programming language. Loop through the `items` list in the response.

**Code Example:**
```python
def repos_with_most_stars():
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    params = {
        "q": "stars:>50000"
    }
    response = requests.get(gh_api_repo_search_url, params=params)
    response_json = response.json()

    for repo in response_json.get("items", []):
        print(f"{repo['name']} - Stars: {repo['stargazers_count']} - Language: {repo['language']}")
```

---

## **Step 4: Creating a Query Builder**

To allow filtering by languages, create a helper function to dynamically construct the query string.

**Code Example:**
```python
def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars}"
    for language in languages:
        query += f"+language:{language}"
    return query
```

---

## **Step 5: Integrating the Query Builder**

Update the `repos_with_most_stars` function to use the `create_query` function. Pass in a list of languages to filter the results.

**Code Example:**
```python
def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)
    params = {
        "q": query,
        "sort": sort,
        "order": order
    }

    response = requests.get(gh_api_repo_search_url, params=params)
    response_json = response.json()

    for repo in response_json.get("items", []):
        print(f"{repo['name']} - Stars: {repo['stargazers_count']} - Language: {repo['language']}")

if __name__ == "__main__":
    repos_with_most_stars(["python", "javascript", "ruby"])
```

---

## **Step 6: Adding Error Handling**

Handle common errors such as hitting the API rate limit (`403`) or bad responses (any status code other than `200`).

**Code Example:**
```python
def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)
    params = {
        "q": query,
        "sort": sort,
        "order": order
    }

    response = requests.get(gh_api_repo_search_url, params=params)

    if response.status_code == 403:
        raise Exception("Rate limit exceeded. Try again later.")
    elif response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    response_json = response.json()

    for repo in response_json.get("items", []):
        print(f"{repo['name']} - Stars: {repo['stargazers_count']} - Language: {repo['language']}")

if __name__ == "__main__":
    repos_with_most_stars(["python", "javascript", "ruby"])
```

---

## **Final Code**

The final code includes:
1. Dynamic query building.
2. Sorting and ordering options as keyword arguments.
3. Error handling for common API issues.

**Final Code:**
```python
import requests

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars}"
    for language in languages:
        query += f"+language:{language}"
    return query

def repos_with_most_stars(languages, sort="stars", order="desc"):
    gh_api_repo_search_url = "https://api.github.com/search/repositories"
    query = create_query(languages)
    params = {
        "q": query,
        "sort": sort,
        "order": order
    }

    response = requests.get(gh_api_repo_search_url, params=params)

    if response.status_code == 403:
        raise Exception("Rate limit exceeded. Try again later.")
    elif response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    response_json = response.json()

    for repo in response_json.get("items", []):
        print(f"{repo['name']} - Stars: {repo['stargazers_count']} - Language: {repo['language']}")

if __name__ == "__main__":
    repos_with_most_stars(["python", "javascript", "ruby"])
```

---

## **Key Takeaways**
- Use the `requests` library to interact with APIs.
- Dynamically construct query strings to filter API results.
- Handle errors gracefully to avoid crashes.
- Use default keyword arguments for flexibility.

---

# Wrapping Up

Today, we've taken a whirlwind tour of the Python programming language, covering everything from basic syntax to working with libraries, APIs, and handling errors.

---

## **What’s Next?**

During **Day 2**, we’ll put this knowledge into practice by writing real programs. Be ready to apply what you’ve learned to solve more complex problems and build useful tools.

---

## **Source Control**

To make the most of your Python projects, it’s highly recommended to use **source control**. Here’s why and how:

### Why Use Source Control?
- **Track Changes**: Source control tools like Git let you track every change you make to your project.
- **Commit Often**: Commit early and often to keep a history of your progress.
- **Collaboration**: GitHub makes it easy to collaborate with others on projects.

### Getting Started with GitHub
- If you’re new to Git or GitHub, check out the [Git In-depth Frontend Masters class](https://frontendmasters.com/) for a comprehensive introduction.
- For Python projects, use a proper `.gitignore` file to exclude unnecessary files (e.g., virtual environments, compiled files, etc.). GitHub provides a [Python `.gitignore` template](https://github.com/github/gitignore/blob/main/Python.gitignore) that you can use.

---
