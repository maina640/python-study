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