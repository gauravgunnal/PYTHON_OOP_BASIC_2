'''Q1'''
'''Abstraction in object-oriented programming (OOP) is the process of simplifying complex systems by breaking them down into smaller, 
more manageable parts. It focuses on capturing the essential features and behavior of an object while hiding unnecessary details. 
Abstraction allows us to create abstract classes or interfaces that provide a blueprint or contract for derived classes to implement.
In Python, abstraction can be achieved through abstract classes and interfaces. An abstract class is a class that cannot be instantiated and 
serves as a blueprint for derived classes. It can contain both abstract and concrete methods. An abstract method is a method without an 
implementation in the abstract class, which must be implemented by any concrete subclass that inherits from it.
Here's an example to illustrate abstraction using an abstract class in Python:'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# Creating an object of the Rectangle class
rectangle = Rectangle(5, 3)

# Accessing the overridden methods
print(rectangle.area())      # Output: 15
print(rectangle.perimeter()) # Output: 16

'''Q2'''
'''Abstraction and encapsulation are two important concepts in object-oriented programming (OOP), but they serve different purposes and 
have distinct meanings:
Abstraction:
Abstraction focuses on capturing the essential features and behavior of an object while hiding unnecessary details.
It is the process of simplifying complex systems by breaking them down into smaller, more manageable parts.
Abstraction allows you to create abstract classes or interfaces that provide a blueprint or contract for derived classes to implement.
It promotes modularity, information hiding, and code reusability.'''
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Creating objects of the derived classes
rectangle = Rectangle(5, 3)
circle = Circle(4)

# Accessing the overridden methods
print(rectangle.area())      # Output: 15
print(rectangle.perimeter()) # Output: 16
print(circle.area())         # Output: 50.24
print(circle.perimeter())    # Output: 25.12

'''Encapsulation:
Encapsulation is the process of bundling data (attributes) and methods (functions) together within a class, hiding the internal 
implementation details from the outside world.It involves encapsulating the data and methods related to an object into a single entity, 
allowing the object to control the access to its internal state.Encapsulation provides data integrity and security, preventing direct access 
to the internal data and allowing controlled interaction with the object through well-defined interfaces.
It promotes information hiding, code organization, and code maintenance.
Example in Python:'''
class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Encapsulated attribute
        self._balance = balance  # Encapsulated attribute

    def get_account_number(self):
        return self._account_number

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount


# Creating an object of the BankAccount class
account = BankAccount("123456789", 1000)

# Accessing the encapsulated attributes using getter methods
print(account.get_account_number())  # Output: 123456789
print(account.get_balance())  # Output: 1000

# Modifying the encapsulated attributes using appropriate methods
account.deposit(500)
account.withdraw(200)

# Accessing the modified attributes
print(account.get_balance())  # Output: 1300

'''Q3'''
'''The abc module in Python stands for "Abstract Base Classes." It provides mechanisms for defining abstract base classes (ABCs) in Python.
 Abstract base classes are classes that cannot be instantiated directly and serve as a blueprint for derived classes. They define a common 
 interface that derived classes must adhere to.
The abc module is used to create abstract base classes and abstract methods. Here are the main purposes and features of the abc module:
Defining Abstract Base Classes (ABCs):
The abc module provides the ABC class, which is used as a base class for defining abstract base classes. When a class inherits from ABC,
 it becomes an abstract base class, and instances of that class cannot be created directly. The ABC class itself uses metaclasses to enforce 
 this behavior.
Declaring Abstract Methods:
Abstract methods are methods that have no implementation in the abstract base class but must be implemented by any concrete (derived) 
class that inherits from the abstract base class. The abc module provides the abstractmethod decorator, which is used to declare abstract 
methods. Abstract methods are meant to be overridden by derived classes to provide specific implementations.
Enforcing Interface Compliance:
By defining abstract base classes and abstract methods, the abc module helps enforce a common interface that derived classes must adhere to. 
It ensures that derived classes implement the required methods, providing a way to define shared behavior and promote code consistency.
Checking Class Hierarchy:
The abc module provides various utility functions, such as isinstance() and issubclass(), that allow you to check if an object or class is 
an instance or subclass of an abstract base class. This enables runtime checking and validation of class hierarchies and helps ensure proper 
inheritance.
The abc module is commonly used when implementing abstract base classes and defining interfaces in Python. It promotes code organization,
 modularity, and reusability by providing a way to define common behavior across multiple classes and ensuring that derived classes conform 
 to a specific interface.
Here's a simple example that demonstrates the usage of the abc module to define an abstract base class with an abstract method:'''

'''Q4'''
'''Data abstraction can be achieved in Python through the use of classes, access modifiers, and getter/setter methods. 
Here are the steps to achieve data abstraction:
Define a Class:
Start by defining a class that represents the abstraction you want to create. The class will encapsulate the data and 
behavior related to the abstraction.
Use Access Modifiers:
In Python, access modifiers are conventions that indicate the intended visibility of attributes and methods. By convention, attributes 
and methods that are intended to be private are prefixed with an underscore (_). This indicates that they should not be accessed 
directly from outside the class.
Define Getter and Setter Methods:
To provide controlled access to the encapsulated data, define getter and setter methods within the class. These methods 
allow external code to retrieve and modify the data in a controlled manner.
The getter methods are used to retrieve the values of the encapsulated attributes, while the setter methods are used 
to modify the attribute values. Within these methods, you can apply additional logic or validation to ensure the integrity of the data.
Access the Data through Methods:
Encourage the use of getter and setter methods to access and modify the data within the class. This promotes data encapsulation 
and ensures that any necessary logic or validation is consistently applied.
By following these steps, you can achieve data abstraction in Python. Here's an example to illustrate the process:
'''
class BankAccount:
    def __init__(self):
        self._balance = 0  # Encapsulated attribute

    def get_balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount


# Creating an object of the BankAccount class
account = BankAccount()

# Accessing the encapsulated attribute using the getter method
print(account.get_balance())  # Output: 0

# Modifying the encapsulated attribute using the setter method
account.deposit(100)
account.withdraw(50)

# Accessing the modified attribute
print(account.get_balance())  # Output: 50
'''By encapsulating the data and providing controlled access through methods, we achieve data abstraction. This hides the internal 
implementation details of the class and allows users of the class to work with the abstraction without needing to know how the data 
is stored or manipulated internally.'''

'''Q5'''
'''No, we cannot create an instance of an abstract class in Python. Abstract classes are designed to be incomplete and serve as blueprints 
for derived classes. They are meant to be subclassed, and their abstract methods need to be implemented by the derived classes.
Attempting to create an instance of an abstract class directly will result in a TypeError being raised. Python enforces this behavior 
to prevent the creation of objects that do not fully define the required behavior specified by the abstract class.
Here's an example to illustrate the inability to instantiate an abstract class:'''
from abc import ABC, abstractmethod

class AbstractClass(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

# Attempting to create an instance of the abstract class
# obj = AbstractClass()  # Raises TypeError
'''To utilize an abstract class, you need to create a derived class that inherits from the abstract class and implements all the abstract 
methods defined in the base class. The derived class becomes a concrete class and can be instantiated.'''