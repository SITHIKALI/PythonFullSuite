# Object-Oriented Programming (OOP) in Python

Object-Oriented Programming is a paradigm that organizes software design around data, or objects, rather than functions and logic. An object can be defined as a data field that has unique attributes and behavior.

## Classes and Objects

A **class** is a blueprint for creating objects. An **object** is an instance of a class.

```python
class Dog:
    # The __init__ method initializes the object's attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # A method is a function defined inside a class
    def bark(self):
        return f"{self.name} says woof!"

# Creating an instance (object) of the Dog class
my_dog = Dog("Rex", 3)

print(my_dog.name)  # Output: Rex
print(my_dog.bark())  # Output: Rex says woof!
```

## Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

*   **Parent class** is the class being inherited from, also called base class.
*   **Child class** is the class that inherits from another class, also called derived class.

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

# Dog inherits from Animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

my_dog = Dog("Buddy")
print(my_dog.eat())  # Output: Buddy is eating. (Inherited method)
print(my_dog.bark()) # Output: Buddy says woof!
```

## Magic (Dunder) Methods

Magic methods in Python are the special methods that start and end with double underscores (`__`). They are also called dunder methods. They are used to implement operator overloading and built-in Python behaviors.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Controls how the object is printed
    def __str__(self):
        return f"{self.make} {self.model}"

my_car = Car("Toyota", "Corolla")
print(my_car)  # Output: Toyota Corolla (Calls the __str__ method)
```
