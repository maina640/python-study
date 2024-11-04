#Write a program which gets a phone number from a form input or terminal. Validates 
#the phone number by checking if it starts with +254.. or 07.. or 7… or 254.. or 01... or
#1.. Convert the number to start with +254… 
#e.g if a user enters “0712345678”, the program should display “+254712345678”
#e.g if a user enters “0112345678”, the program should display “+254112345678”
#e.g if a user enters “712345678”, the program should display “+254712345678”
phone_number=str(input('enter phone_number: '))
phone_number = phone_number.strip()

if phone_number.startswith("+254") or phone_number.startswith("07") or phone_number.startswith("7") or phone_number.startswith("254") or phone_number.startswith("01") or phone_number.startswith("1"):
    # If the phone number starts with "07" or "7", remove the leading "0" or "7"
    if phone_number.startswith("07") or phone_number.startswith("7"):
      phone_number = phone_number[1:]
    # If the phone number starts with "01" or "1", remove the leading "0" or "1"
    if phone_number.startswith("01") or phone_number.startswith("1"):
      phone_number = phone_number[1:]
    # If the phone number starts with "254", remove the leading "254"
    if phone_number.startswith("254"):
      phone_number = phone_number[3:]
    # Add the "+254" prefix to the phone number
    phone_number = "+254" + phone_number
    print(phone_number)
else:
    print(None)

# Get the phone number from the user
phone_number = input("Enter phone number: ")

# Format the phone number
formatted_phone_number = format_phone_number(phone_number)

# Display the formatted phone number
if formatted_phone_number:
  print("Formatted phone number:", formatted_phone_number)
else:
  print("Invalid phone number.")