#my car
class Car:
    def __init__(self, color, brand, shape):
        self.color=color
        self.brand=brand
        self.shape=shape

        def describe(self):
            return f'the color of this{self.color}and the brand is {self.brand}the shape is{self.shape}'

my_car = Car('red', 'BMW' , 'wagon')
car1 = Car ('green' , 'Audi' , 'sedan')
print(my_car.describe())
print(car1.describe())

#Create a class called Student with attributes name and age.
#Add a method introduce that prints: "Hello, my name is [name] and I am [age] years old."
#Create an object of Student and call the introduce method

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

        def introduce(self):
            return f'Hello, my name is {self.name} and i am {self.age} years old.'

f_intro=Student('maina',50)
print(f_intro.introduce())

#Define a class Calculator with methods add, subtract, multiply, and divide that perform 
#the respective operations on two numbers.
#Create an object of Calculator and use it to perform some calculations.

class Calculator:
    def __init__(self,add,subtract,multiply,divide):
        self.add=add
        self.subtract=subtract
        self.multiply=multiply
        self.divide=divide

        def add(self,a,b):
            return a+b
        
        def subtract(self,a,b):
            return a-b
        
        def multiply(self,a,b):
            return a*b
        
        def divide(self,a,b):
            return a/b
        
x=float(input('enter number: '))
y=float(input('enter number: '))
numbers= Calculator(x,y)
print(numbers.divide())
print(numbers.subtract())
print(numbers.add())
print(numbers.multiply())


#Create a class Animal with attributes species and sound.Add a method make_sound that prints:
#"The [species] goes [sound]!",Instantiate objects for different animals and call make_sound.

class Animal:
    def __init__(self,species,sound):
        self.sound=sound

    def make_sound(self):
        return f'The {self.species} goes {self.sound}!'
    
dog=Animal('dog','woof')
cow=Animal('cow','moo')
cat=Animal('cat','meow')

print(dog.make_sound())
print(cat.make_sound())
print(cow.make_sound())

#Create a class Book with attributes like title, author, and year.
#Add a method that returns a description of the book.
#Create an object of Book and print out the description.

class Book:
    def __init__(self,title, author,year):
        self.title=title
        self.author=author
        self.year=year

    def describe(self):
        return f'the book{self.title} on cold war by{self.author} was published on{self.year}.'
    
book1=Book('Art of war','Maina',2040)
print(book1.describe())

#Define a class BankAccount with attributes owner and balance (set balance to 0 by default).
#Add methods deposit and withdraw to modify the balance and a method get_balance to display the balance.
#Ensure that the withdraw method does not allow the balance to go negative.

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance +=amount
            return f'{amount}deposited your balance is {self.balance}'
        else:
            return f'deposit amount cannot be less than 0'
        
    def withdraw(self,amount):
        if amount>self.balance:
            return f'hello{self.owner} insufficient balance to withdraw{amount}'
        else:
            self.balance=amount
            return f'hello {self.owner} {amount} withdrawed and the new balance is {self.balance}'
        
    def get_balance(self):
        return f'hello {self.owner} your current balance is {self.balance}'
    
person1=BankAccount('maina')
person1.deposit(40000)
person1.withdraw(10000)
print(person1.get_balance())


#Define a class Rectangle with attributes width and height.Add methods area and perimeter to calculate
#the area and perimeter of the rectangle.
#Instantiate a few rectangle objects and print their area and perimeter.


#Create a class Employee with attributes name and salary.Add a method give_raise that increases the salary
#by a given percentage.Instantiate an employee, give them a raise, and display their new salary.

class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def give_raise(self,percentage):
        self.salary+=self.salary*(percentage/100)
        return self.salary
    
employee1=Employee('maina',100000)
employee1.give_raise(30)
print(f'{employee1.name} new salary is {employee1.salary}')


#Create a base class Vehicle with attributes brand and model.
#Create two subclasses Car and Motorcycle that inherit from Vehicle and add unique methods to each
#subclass (e.g., honk for Car and rev_engine for Motorcycle).
#Instantiate both subclasses and call their methods.

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)
        self.brand=brand

class Car(Vehicle):
    def honk(self):
        return f'{self.brand} the car honks'
    
class motorcycle(Vehicle):
    def rev_engine(self):
        return f'the motorcycle vrooms'
    
Vehicle1=Car('toyota','v8')
print(Vehicle1.honk())