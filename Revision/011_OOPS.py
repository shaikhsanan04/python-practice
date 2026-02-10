# Defining a Class and Creating an Object

# class Car:

#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model

#     def display_carinfo(self):
#         print(f"{self.brand} {self.model}")
    
# car1 = Car("Mahindra","Thar")
# car1.display_carinfo()
    
# car2 = Car("Tata","Sienna")
# car2.display_carinfo()

# --------------------------------------------



# Encapsulation (Data Hiding)
# encapsulation prevents direct modification of attributes and allows controlled access using getter and setter methods

# class BankAccount:

#     def __init__(self, balance):
#         self.__balance = balance #private attribute

#     def get_balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount

# # using encapsulation
# account = BankAccount(10000)
# print(account.get_balance())
# account.deposit(4500)
# print(account.get_balance())
# account.deposit(55500)
# print(account.get_balance())

# --------------------------------------------------------------------

# Inheritance (Reusing Code)
# Inheritance allows a class (child) to inherit attributes and methods from another class (parent).

# class Animal:

#     def sound(self):
#         return "Animal Makes sound"

# class Dog(Animal):
#     def sound(self):
#         return "Bark"
    
# dog = Dog()
# dog2 = Animal()
# print(dog.sound())
# print(dog2.sound())




# Multiple Inheritance
# A class can inherit from multiple parent classes.

# class A:

#     def do_something_1(self):
#         return "something 1"

# class B:
#     def do_something_2(self):
#         return "something 2"

# class C(A, B):
#     def do_something_3(self):
#         return "something 3"
    
# c = C()
# print(c.do_something_3())
# print(c.do_something_2())
# print(c.do_something_1())

# Polymorphism (Same Method, Different Behavior)
# Polymorphism allows different classes to use the same method name.

# Method Overriding Example

# class Bird:

#     def fly(self):
#         return "birds fly"

# class Eagle(Bird):
#     def fly(self):
#         return "Eagles fly faster"
    

# bird = Bird()
# eagle = Eagle()

# print(bird.fly())
# print(eagle.fly())


# ----------------------------------------------------------------------------


# Abstraction (Hiding Implementation Details)
# Abstraction is used to define a method without implementing it in the base class. It is achieved using abstract base classes ( ABC module).

# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Square(Shape):

#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side * self.side
    
# square = Square(4)
# print(square.area())