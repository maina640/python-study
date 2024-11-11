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
    