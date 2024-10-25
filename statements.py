if 20>40:
    print('20 is greater')
else:
    print('20 is less than')

    #declare a variable marks then check if the marks is
    #above 50 print pass otherwise print fail
    marks=50
    if marks>20:
        print('pass')
    else:
        print('fail')
    
#average_marks = 70
average_marks = 70
if (average_marks > 50) and (average_marks < 100):
     print('pass')
else:
    print('fail')

    #if elif or else
    #if 90>=100 (A)
    #if 80>=90 (B)
    #if 70>=80 (C)
    #if 60>=70 (D)
    #if 50>=60 (E)
    #any below 50 (fail)
marks=int(input('enter marks: '))
if marks>=90 and marks <=100:
    print('A')
elif marks>=80 and marks<90:
    print('B')
elif marks>=70 and marks<80:
    print('C')
elif marks>=60 and marks <70:
    print('D')
elif marks>=50 and marks<60:
    print('E')
else:
    print('fail') 

#write a program that takes age from input
#if age is 60 or above print(older)
#if age is 18 and above print(adult)
#otherwise print (minor)
age=int(input('enter age: '))
if age>=60:
    print('older')
elif age>=18 and age<60:
    print('adult')
else:
    print('minor')


#nested (if)statements
#you give 100 discount on purchase above 1000
#you give 200 discount on purchase above 6000
#no discount

purchase=int(input('enter purchase:'))
if purchase>1000:
    print('100 discount')
    if purchase>6000:
        print('200 discount')
else:
    print('no discount')

#write a program that takes users age as input
#if the age is 18 and above, print (eligible)
#if not above 18 print (too young)

age=int(input('enter age:'))
if age>=18:
    license=input("do you have a license yes/no:").lower().strip()
    if license=='yes':
        print('you are eligible')
    else:
        print('you are not eligible')
else:
    print('you are too young for driving')


#write aloan that:
#takes the user's credit score and annual income as input
#if the credit score is above 700, check if the income is above 50000;
#If both conditions are met, print "Loan approved."
#If only the credit score is high, print "Income requirement not met."
#If the credit score is below 700, print "Credit score too low."
credit_score=int(input('enter credit score '))
annual_income=float(input('enter annual income '))
if credit_score>700:
    if annual_income>=50000:
        print('loan approved')
    else:
        print('income requirement not met')
else:
    print('credit score too low')
    




    
