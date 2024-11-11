#Write a program that takes input of someone's basic salary and benefits, adds them to find
#the gross salary then uses  the gross salary to find the NHIF.
basic_salary=float(input('enter basic salary:'))
benefits=float(input('enter benefits: '))
def calculate_gross_salary(basic_salary,benefits):
    sum=basic_salary+benefits
    return sum
gross_salary=calculate_gross_salary(basic_salary,benefits)
print(gross_salary)

#Employee's Monthly Gross Salary(Kshs)	Monthly NHIF Contribution (Kshs)
#5,999	150
#6,000 - 7,999	300
#8,000 - 11,999	400
#12,000 - 14,999	500
#15,000 - 19,999	600
#20,000 - 24,999	750
#25,000 - 29,999	850
#30,000 - 34,999	900
#35,000 - 39,999	950
#40,000 - 44,999	1,000
#45,000 - 49,999	1,100
#50,000 - 59,999	1,200
#60,000 - 69,999	1,300
#70,000 - 79,999	1,400
#80,000 - 89,999	1,500
#90,000 - 99,999	1,600
#100,000 and above	1,700

def find_NHIF_using_gross_sal(gs):
    if gs <5999:
        give=150
    elif gs > 6000 and gs<8000:
        give=300
    elif gs >8000 and gs <11999:
        give=400
    elif gs >12000 and gs <15000:
        give=500
    elif gs >15000 and gs <19999:
        give=600
    elif gs >20000 and gs <25000:
        give=750
    elif gs >25000 and gs <30000:
        give=850
    elif gs >30000 and gs <35000:
        give=900
    elif gs >35000 and gs <40000:
        give=950
    elif gs >40000 and gs <45000:
        give=1000
    elif gs>45000 and gs<50000:
        give=1100
    elif gs>50000 and gs<60000:
        give=1200
    elif gs>60000 and gs<70000:
        give=1300
    elif gs>70000 and gs<80000:
        give=1400
    elif gs>80000 and gs<90000:
        give=1500
    elif gs>90000 and gs<100000:
        give=1600
    else:
        give=1700
    return give

NHIF=find_NHIF_using_gross_sal(gross_salary)
print(NHIF)
