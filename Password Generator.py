import random

Lower_Case_Letter = "abcdefghigklmnopqrstuvwxyz"
Upper_Case_Letter = Lower_Case_Letter.upper()
Numbers = "1234567890"
Symbols = "!@#$%^&*()_+=-[]{};:,<.>/?"
Characters = Lower_Case_Letter + Upper_Case_Letter + Numbers + Symbols

while 1:
    Password_Length = input("Please enter the password length that you would like \n= ")
    Password_Quantity = input("Please enter thr number of password that you would need \n= ")
    for x in range(0, int(Password_Quantity)):
        Password = ""
        for i in range(0, int(Password_Length)):
            password_Char = random.choice(Characters)

            Password = Password + password_Char

        print(f"Here is your password {x} :", Password)
