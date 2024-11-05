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
