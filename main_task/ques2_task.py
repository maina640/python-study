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