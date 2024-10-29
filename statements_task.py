#Take three inputs from a user, separately. Print the largest of the numbers.
num1=40
num2=67
num3=89
largest=max(num1=num2+num3)
print(f'the largest number is {largest}')

#conditional statement
if num1>num2 and num1>num3:
    largest=num1
elif num2>num1 and num2>num3:
    largest=num2
else:
    largest=num3
print(f'the largest number is{largest}')


#Take as input from a user the temperature if the temperature is above 30°C display
#“The temperature is too high”,if the temperature is above 15 display “Normal temperature” 
# otherwise display “Cold temperature”
temp=int(input('enter_your_temp: '))
if temp>30:
    print('The temperature is too high')
elif temp>15:
    print('Normal temperature')
else:
    print('cold temparature')


#Write a Python program that checks if a variable x is between 10 and 20 (inclusive)
#and if another variable y is greater than 100. If both conditions are true, print 
# "Conditions met", otherwise print "Conditions not met"
X=int(input('enter X: '))
if X>10 and X<20:
    print('inclusive')
else:
    print('not_inclusive')
Y=int(input('enter Y: '))
if Y>100:
    print('inclusive')


#Write a Python program that checks if a variable student_score is greater than 90.
#If true, check if the attendance is greater than 80. If both conditions are true,
#print "Excellent student", otherwise print "Good score, but attendance needs improvement"
student_score=78
attendance=89
if student_score>90 and attendance>80:
    print('Excellent student')
else:
    print('Good score, but attendance needs improvement')


#Write a program that:
#Takes a transaction amount and account type ("Standard" or "Premium") as input.
#If the account type is "Standard":
#Check if the amount is above 500:
#If it is, print "Transaction exceeds the limit for Standard accounts."
#If not, print "Transaction approved."
#If the account type is "Premium":
#Check if the amount is above 1,000:
#If it is, print "Transaction exceeds the limit for Premium accounts."
#If not, print "Transaction approved."
#standard<500
#premium>1000
transaction_amount=float(input('enter your transaction amount:'))
account_type=input(input('Is account_type premium/standard:')).strip()
if account_type=='standard':
    if transaction_amount>500:
        print('Transaction exceeds the limit for Standard accounts.')
    else:
        print('Transaction approved')
elif account_type=='premium':
    if transaction_amount>1000:
        print('Transaction exceeds the limit for Premium accounts.')
    else:
        print('Transaction approved.')
else:
    print('non')











