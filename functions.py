# a funcion to calculate the area of a triangle
def triangle_area():
    base=70
    height=67
    area=(base*height)/2
    print(area)
triangle_area()


#create a function that calculate area of a rectangle
def area_of_rectangle():
    length=56
    width=89
    area=(length*width)
    print(area)
area_of_rectangle()
def area_of_rectangle(len,width):
    area=(length*width)
    return(area)

#area of triangle using parameters and arguments
def area_triangle(base,height):
    area_tri=(base*height)*0.5
    print(area_tri)
area_triangle(20,50)


#Write a program that prints the largest of 4 inputs 
#taken in from a user. Assume that the user would not 
#enter any two numbers which are the same.

num1=int(input('enter number: '))
num2=int(input('enter number: '))
num3=int(input('enter number: '))
num4=int(input('enter number: '))

def check_largest(num1,num2,num3,num4):
    if num1>num2 and num1>num3 and num1>num4:
        result=f'{num1} is the largest'
    elif num2>num1 and num2>num3 and num2>num4:
        result=f'{num2} is the largest'
    elif num3>num1 and num3>num2 and num3>num4:
        result=f'{num3} is the largest'
    else:
        result=f'{num4} is the largest'
    return result

number1=int(input('enter number 1'))
number2=int(input('enter number 2'))
number3=int(input('enter number 3'))
number4=int(input('enter number 4'))

x=check_largest(number1,number2,number3,number4)