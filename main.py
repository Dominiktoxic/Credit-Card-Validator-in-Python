from tkinter import *
from tkinter import messagebox

# Credit Card Validator

# Steps
# (1) Remove any "-" or " "
# (2) Sum all digits in odd places from right to left
# (3) Double every second digit from right to left
# (4) Sum the values from steps 2 and 3
# (5) Check if the sum is divisible by 10, if so, the Credit Card Number is valid

class Validator:

    def __init__(self, card):
        self.card = card

    def verify(self):
        self.card = self.card.replace("-", "")
        self.card = self.card.replace(" ", "")

        odd = 0
        self.card = self.card[::-1]

        for digit in self.card[::2]:
            odd += int(digit)

        even = 0
        for digit in self.card[1::2]:
            digit = int(digit)
            digit *= 2
            if digit >= 10:
                even = digit % 10 + 1
            else:
                even += digit

        if (odd + even) % 10 == 0:
            return True
        else:
            return False

app = Tk()

MAX_WIDTH = 400
MAX_HEIGHT = 210

app.maxsize(MAX_WIDTH, MAX_HEIGHT)
app.minsize(MAX_WIDTH, MAX_HEIGHT)

app.title("Credit Card Validator")

programTitle = Label(app, text="Credit Card\nValidator", font=("Arial Black", 20))
programTitle.pack()

entry = Entry(app, font=("Arial Bold", 15))
entry.place(x=90, y=100)

def instantiateValidator():
    card = entry.get()
    validator = Validator(card)
    try:
        credit_card_number = validator.verify()
        if credit_card_number:
            messagebox.showinfo("Credit Card Validator", f"'{card}' is valid!")
        else:
            messagebox.showinfo("Credit Card Validator", f"'{card}' is invalid!")
    except ValueError:
        print(card, "is an invalid credit card number.")

submit = Button(app, text="Submit", font=("Arial Bold", 12), command=instantiateValidator)
submit.place(x=171, y=150)

app.mainloop()