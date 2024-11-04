#Write a program which accepts email as form input or from terminal. Validate the email
#by checking if it's a valid email. 
#Hint: Check if it contains an “@” symbol and “.” symbol.
email=str(input('enter your email: '))
if email.index('@')>0 and email.index('@')<email.index('.'):
    print('valid email')
else:
    print('invalid email')