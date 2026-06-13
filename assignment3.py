# 1 (class named Student with attributes)
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course
st = Student("Anshu", 20, "AIML")
print("Name:", st.name)
print("Age:", st.age)
print("Course:", st.course)

# 2 (class named Car with attributes)
class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
car1 = Car("toyota", "fortuner", 4700000)
car2 = Car("mahindra", "scorpio", 2000000)
print("brand:",car1.brand,car2.brand)
print("model:",car1.model,car2.model)
print("price:",car1.price,car2.price)
print(car1.brand,car1.model,car1.price)
print(car2.brand,car2.model,car2.price)

# 3 ( class named Employee)


class Employee:
    def __init__(self,employee_id, name, salary):
        self.employee_id = employee_id
        self.name =name
        self.salary = salary
Employee = Employee(23, "aakash", 50000)
print("employee_id:",Employee.employee_id)
print("name:",Employee.name)
print("salary:",Employee.salary)


#4  (class named Rectangle)

class Rectangle:
    def __init__(self,length, width):
       self.length= length
       self.width = width
    def area(self):
        return self.length*self.width
rect = Rectangle(10, 5)
print("Area of Rectangle:", rect.area())

# 5 (class named Circle with an attribute radius)

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return self.radius*self.radius*3.14
circle = Circle(10)
print("area of circle:",circle.area())      

# 6  ( class named BankAccount)


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Balance after withdrawal:", self.balance)
        else:
            print("Insufficient Balance")
acc = BankAccount("Anshu", 10000)
acc.deposit(5000)
acc.withdraw(3000)

# 7 ( class named Animal with a method sound)

class Animal:
    def __init__(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("bark")
d = Dog()
d.sound()           

# 8  (class named Person with attributes)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Roll Number:", self.roll_number)
s = Student("Anshu", 20, 210)
s.display()

# 9(class named Calculator with methods)


class Calculator:
    def add(self, a, b):
        print("Addition:", a + b)
    def subtract(self, a, b):
        print("Subtraction:", a - b)
    def multiply(self, a, b):
        print("Multiplication:", a * b)
    def divide(self, a, b):
        if b != 0:
            print("Division:", a / b)
        else:
            print("Cannot divide by zero")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
c = Calculator()
c.add(num1, num2)
c.subtract(num1, num2)
c.multiply(num1, num2)
c.divide(num1, num2)


# 10  ( class named LibraryBook with attributes)

class LibraryBook:
    def __init__(self, book_name, author, price):
        self.book_name = book_name
        self.author = author
        self.price = price
    def display_book_info(self):
        print("Book Name:", self.book_name)
        print("Author:", self.author)
        print("Price:", self.price)
        print("---------------------")
book1 = LibraryBook("Python Basics", "abc", 450)
book2 = LibraryBook("Data Structures", "def", 550)
book3 = LibraryBook("Machine Learning", "ghi", 750)
book1.display_book_info()
book2.display_book_info()
book3.display_book_info() 