#Write a python program that takes from a user 5 inputs (maths, eng, swa, sci, sos). 
#Create a function that calculates the total marks another the average marks ,then a
#functions that finds the grade according to the table below. 
#Use the value from total to get the average and average to find the grade.
#A > 79 , B - 60 to 79, C -  59 to 49, D - 40 to 49, E - less 40
maths=float(input('enter maths marks: '))
english=float(input('enter english marks: '))
kiswahili=float(input('enter kiswahili marks: '))
science=float(input('enter science marks: '))
social=float(input('enter social marks: '))

def total_mark(maths,english,kiswahili,science,social):
    sum=maths+english+kiswahili+science+social
    return sum
total_marks=total_mark(maths,english,kiswahili,science,social)
print(total_marks)

#calculate average
def calculate_average(total):
    average=total / 5
    return average

avg=calculate_average(total_marks)

def find_grade(b):
    if b>79:
        grade='A'
    elif 60<= b <= 79:
        grade='B'
    elif 49 <= b <= 59:
        grade='C'
    elif 40 <= b <= 40:
        grade='D'
    else:
        grade='E'
    return grade

print(find_grade)