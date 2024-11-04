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