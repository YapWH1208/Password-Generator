import random
from tkinter import *

class Password_Generator:
    def __init__(self):
        # Main Screen
        window = Tk()
        window.title("Password Generator")

        # Labels
        Title_Label = Label(window, text="Welcome to the Password Generator")
        Title_Label.grid(row=0, sticky=N, pady=10, padx=150)

        Password_Length_Label = Label(window, text="Password Length:")
        Password_Length_Label.grid(row=1, sticky=W, padx=15)

        # Entry
        self.Pass_Length = IntVar()
        Password_Length_Entry = Entry(window, textvariable=self.Pass_Length)
        Password_Length_Entry.grid(row=1, sticky=E, padx=15)

        # Button
        Get_Password_Button = Button(window, text="Get Password", command=self.password)
        Get_Password_Button.grid(row=3, sticky=S)

        # Dummy Label
        Label(window).grid(row=4)
        Label(window).grid(row=10)

        # Result
        Result_Label = Label(window, text="Your Results:")
        Result_Label.grid(row=6, sticky=S)

        self.Result = StringVar()
        Result_Text = Entry(window, textvariable=self.Result, width=150)
        Result_Text.grid(row=7, ipady=10, padx=15)

        window.mainloop()

    def password(self):

        Lower_Case_Letter = "abcdefghigklmnopqrstuvwxyz"
        Upper_Case_Letter = Lower_Case_Letter.upper()
        Numbers = "1234567890"
        Symbols = "!@#$%^&*()_+=-[]{};:,<.>/?"
        Characters = Lower_Case_Letter + Upper_Case_Letter + Numbers + Symbols

        Password = ""
        for i in range(0, int(self.Pass_Length.get())):
            password_Char = random.choice(Characters)

            Password = Password + password_Char

        self.Result.set(Password)

Password_Generator()
