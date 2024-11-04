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
