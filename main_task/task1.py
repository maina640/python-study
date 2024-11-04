from datetime import datetime
#Write a program that prompts the user to enter the base and height of a triangle
#and returns its area.
base=int(input('enter the base: '))
height=int(input('enter the height: '))
area=base*height
print(area)

#Prompt the user for a number either on a form input or the terminal. Depending on
#whether the number is even or odd, display  either “odd” or “even” to the user.
numeral=int(input('enter numeral: '))
if numeral%2==0:
    print('even')
else:
    print('odd')
    
#If the number is a multiple of 4, print out “divisible by 4”.
if numeral%4==0:
    print('divisible by 4')
else:
    print('not divisible')

#Write a program which gets a phone number from a form input or terminal. Validates 
#the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or
#1.. Convert the number to start with +254… 
#e.g if a user enters “0712345678”, the program should display “+254712345678”
#e.g if a user enters “0112345678”, the program should display “+254112345678”
#e.g if a user enters “712345678”, the program should display “+254712345678”
phone_number=str(input('enter phone_number: '))
phone_number = phone_number.strip()

if phone_number.startswith("+254") or phone_number.startswith("07") or phone_number.startswith("7") or phone_number.startswith("254") or phone_number.startswith("01") or phone_number.startswith("1"):
    # If the phone number starts with "07" or "7", remove the leading "0" or "7"
    if phone_number.startswith("07") or phone_number.startswith("7"):
      phone_number = phone_number[1:]
    # If the phone number starts with "01" or "1", remove the leading "0" or "1"
    if phone_number.startswith("01") or phone_number.startswith("1"):
      phone_number = phone_number[1:]
    # If the phone number starts with "254", remove the leading "254"
    if phone_number.startswith("254"):
      phone_number = phone_number[3:]
    # Add the "+254" prefix to the phone number
    phone_number = "+254" + phone_number
    print(phone_number)
else:
    print(None)

# Get the phone number from the user
phone_number = input("Enter phone number: ")

# Format the phone number
formatted_phone_number = format_phone_number(phone_number)

# Display the formatted phone number
if formatted_phone_number:
  print("Formatted phone number:", formatted_phone_number)
else:
  print("Invalid phone number.")

#Write a program which accepts email as form input or from terminal. Validate the email
#by checking if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.
email=str(input('enter your email: '))
if email.index('@')>0 and email.index('@')<email.index('.'):
    print('valid email')
else:
    print('invalid email')





#Implement a program that takes 3 users  inputs from the terminal or the Browser, and stores
#them in three variables. Return the largest of the three. Do this without using the the 
#inbuilt max () function!
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
# Find the largest number
largest_number=find_largest(num1, num2, num3)

# Print the largest number
print("The largest number is:", largest_number)



#Write a program that lets the user input a password. Give them only 4 attempts to check
#the passwords entered against “admin@123”. If the password is correct access is granted.
#After you show them a message , the account is blocked.
attempts=4
correct_password='admin@123'
for m in range(attempts):
    password=input('enter password:')
    if password==correct_password:
        display='Access granted'
    else:
        display='Incorrect password'
print(display)

#Write that prompts the user to input student marks. The input should be between 0 and 100.
#then output the correct grade: 
#A > 79 , B - 60 to 79, C  > 49 to 59, D - 40 to 49, E - less 40
marks=float(input('enter your: '))
if marks > 79:
    print('A')
elif marks >= 60 and marks <= 79:
    print('B')
elif marks >= 49 and marks <= 59:
    print('C')
elif marks >= 40 and marks <= 49:
    print('D')
else:
    print('E')



#Write a program that takes as input the speed of a car e.g 80. If the speed is less than 70,
#it should print “Ok”. Otherwise, for every 5 km/s above the speed limit (70), it should 
#give the driver one demerit point and print the total number of demerit points.
#For example, if the speed is 80, it should print: “Points: 2”. If the driver gets more
#than 12 points, the function should print: “License suspended”.
def check_speed(speed):
  demerit_points = 0
if 'speed'< 70:
    print("Ok")
else:
    demerit_points = ('speed' - 70) // 5
    if demerit_points > 12:
      print("License suspended")
    else:
      print(f"Points: {demerit_points}")


#Write a program called stars. It should prompt the user for a number, and it should print the number of stars till the number entered.
#Example If rows is 5, it should print the following:
#*
#**
#***
#****
#*****.....
def stars():
    
  rows = int(input("Enter the number of rows: "))
  for i in range(1, rows + 1):
    print("*" * i)

stars()

#Write a program that calculates the total stock in a company from the array/list below if we know that the
#stock is the last digit in every array/list.
#prods = [[‘omo’,’30kshs’,’300’], [‘milk’,’50kshs’,’200’],[‘bread’,’45kshs’,’359’], [‘coffee’,’5kshs’,’79’]]
products = [['omo', '30kshs', '300'], ['milk', '50kshs', '200'], ['bread', '45kshs', '359'], ['coffee', '5kshs', '79']]
total_stock = 0

for product in products:
  stock = int(product[-1][-1])  # Extract the last digit of the last element
  total_stock += stock

print(f"Total stock: {total_stock}")


#Write a program that takes the date of birth of a person and the program outputs the age in terms of years,
#months,days TODAY.
dob=input('enter day of birth yyyy-mm-dd:')
dob_split=dob.split('_')
print(dob_split)
today=datetime.now()
#t_month=
today_month=today.month
today_year=today.year
today_day=today.day
print(today_day)

years=today_year-int(dob.split[0])
months=today.month-int(dob.split[1])
days=today_day-int(dob.split[2])
print(type(today))
#age=today_dob


#Write a program that prints the largest of 4 inputs taken in from a user. Assume that the user would not enter
#any two numbers which are the same.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
num4 = float(input("Enter the fourth number: "))

# Find the largest number
largest = num1
if num2 > largest:
  largest = num2
if num3 > largest:
  largest = num3
if num4 > largest:
  largest = num4

# Print the largest number
print("The largest number is:", largest)

#Write a program that takes the email and password as input from a user and checks if they are equal to 
#“admin@mail.com” and password is “Admin@123” , if so then print  “Login is Successful” and if not print 
#“Invalid username or password”. ONLY accept 3 tries after which it notifies you that you have been blocked.

correct_password='admin@123'
max_attempts=4
attempts=0
while attempts<max_attempts:
    password=input('enter your password: ')
    if password==correct_password:
        display='access granted'
        break
    else:
        attempts+=1
        print(f'incorrect password you have{\
            attempts}attempts remaining')

if attempts==max_attempts:
    display='account blocked'

#Write a program that takes input of 2 values and adds them. The program should only accept numbers and floats 
#only or otherwise display an error “invalid character entered” and take the user to re-enter the inputs .
while True:
    try: 
        input1=float(input('enter the first number: '))
        input2=float(input('enter the first number: '))

        result=input1+input2
        print(result):






