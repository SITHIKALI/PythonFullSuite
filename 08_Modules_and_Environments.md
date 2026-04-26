# Modules and Environments

As your Python projects grow, keeping all your code in a single file becomes unmanageable. Furthermore, learning how to manage dependencies is a crucial skill for any developer.

## Modules

A module is simply a file containing Python definitions and statements. The file name is the module name with the suffix `.py` appended.

### Standard Library Imports
Python comes with a "batteries-included" standard library.
```python
import math
import random
from datetime import datetime

print(math.pi)
print(random.randint(1, 10))
print(datetime.now())
```

### Creating Your Own Modules
If you have a file `my_math.py`:
```python
# my_math.py
def add(a, b):
    return a + b
```

You can use it in another file:
```python
# main.py
import my_math

result = my_math.add(5, 10)
```

## Virtual Environments (`venv`)

A virtual environment is a self-contained directory tree that contains a Python installation for a particular version of Python, plus a number of additional packages.

**Why use them?** To avoid dependency conflicts. Project A might need version 1.0 of a library, while Project B needs version 2.0. By using virtual environments, you keep their dependencies isolated.

### Creating and Activating a Virtual Environment
1. **Create**:
   ```bash
   python3 -m venv myenv
   ```
2. **Activate (Mac/Linux)**:
   ```bash
   source myenv/bin/activate
   ```
3. **Activate (Windows)**:
   ```cmd
   myenv\Scripts\activate
   ```
   *Once activated, your terminal prompt will usually be prefixed with `(myenv)`.*

4. **Deactivate**:
   ```bash
   deactivate
   ```

## Managing Dependencies with `pip`

`pip` is the package installer for Python. 

### Installing Packages
```bash
pip install requests
```

### Requirements Files
It's standard practice to track your project's dependencies in a `requirements.txt` file.

**Generating the file**:
```bash
pip freeze > requirements.txt
```

**Installing from the file** (useful when setting up a project on a new machine):
```bash
pip install -r requirements.txt
```
