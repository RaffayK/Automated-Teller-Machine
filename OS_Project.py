from datetime import date
import threading
import time

today = date.today()
lock = threading.Lock()


class CardHolder:
    def __init__(self, cardNumber, pin, firstName, lastName, balance):
        self.cardNumber = cardNumber
        self.pin = pin
        self.firstName = firstName
        self.lastName = lastName
        self.balance = balance

    # Getters
    def get_cardNumber(self):
        return self.cardNumber

    def get_pin(self):
        return self.pin

    def get_firstName(self):
        return self.firstName

    def get_lastName(self):
        return self.lastName

    def get_balance(self):
        return self.balance

    # Setters
    def set_cardNumber(self, newVal):
        self.cardNumber = newVal

    def set_pin(self, newVal):
        self.pin = newVal

    def set_firstName(self, newVal):
        self.firstName = newVal

    def set_lastName(self, newVal):
        self.lastName = newVal

    def set_balance(self, newVal):
        self.balance = newVal

    # Print function
    def print_out(self):
        print("Card Number: ", self.cardNumber)
        print("PIN: ", self.pin)
        print("First Name: ", self.firstName)
        print("Last Name: ", self.lastName)
        print("Balance: ", self.balance)


# Function for printing the menu
def print_menu():
    print("        *********           ")
    print("    *THE RFM BANK MENU*     ")
    print("        *********           ")
    print("* Please choose one of the following options:")
    print("****************")
    print("* 1. Deposit ")
    print("* 2. Withdraw ")
    print("* 3. Fund Transfer")
    print("* 4. Inquire Balance")
    print("* 5. Mini Statement")
    print("* 6. Account Details")
    print("* 7. Change PIN")
    print("* 8. Pay Bill")
    print("* 9. Exit")
    print("****************")


def deposit(cardHolder):
    try:
        print("        *********")
        deposit = float(input("* Enter the amount you want to deposit (in Rps): "))
        cardHolder.set_balance(cardHolder.get_balance() + deposit)
        print("* Your new balance is:", cardHolder.get_balance())
        print("* Date:", today)
        print("        *********")
    except ValueError:
        print("* Invalid input. Amount must be a number.")


def withdraw(cardHolder):
    try:
        print("        *********")
        withdraw = float(input("* Enter the amount you want to withdraw (in Rps): "))
        if cardHolder.get_balance() < withdraw:
            print("* Sorry, insufficient balance")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("* Successfully withdrawn")
        print("        *********")
    except ValueError:
        print("* Invalid input. Amount must be a number.")


def Funds_Transfer(cardHolder):
    recipient_name = input("* Enter the name or phone number of the recipient: ")
    try:
        withdraw = float(input("* Enter the amount to send (in Rps): "))
        if cardHolder.get_balance() < withdraw:
            print("* Sorry, insufficient balance")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - withdraw)
            print("        *********")
            print("* Name:", recipient_name)
            print("* Amount sent:", withdraw)
            print("* Status: Successfully sent")
            print("* Date:", today)
            print("* Amount remaining:", cardHolder.get_balance())
            print("        *********")
    except ValueError:
        print("* Invalid input. Amount must be a number.")


def Balance_Inquiry(cardHolder):
    print("        *********")
    print("* Name:", cardHolder.get_firstName(), cardHolder.get_lastName())
    print("* Your current balance in the account is:", cardHolder.get_balance())
    print("* Date:", today)
    print("        *********")


import random
from datetime import datetime, timedelta

today = datetime.today().date()

# Rest of the code...

def mini_statement(cardHolder, today):
    print("        *********")
    print("* Name:", cardHolder.get_firstName(), cardHolder.get_lastName())
    print("* Mini Statement:")
    # Generate random dates for transactions
    transaction_dates = [today - timedelta(days=random.randint(1, 30)) for _ in range(5)]

    for i in range(5):
        transaction_amount = random.randint(10, 1000)
        transaction_type = random.choice(["Deposit", "Withdraw"])
        transaction_date = transaction_dates[i]

        print("* Transaction {}: {} ${} on {}".format(i + 1, transaction_type, transaction_amount, transaction_date))

    print("        *********")


def account_Details(cardHolder):
    print("        *********")
    print("* Debit Card No:", cardHolder.get_cardNumber())
    print("* Name:", cardHolder.get_firstName(), cardHolder.get_lastName())
    print("* Total Amount:", cardHolder.get_balance())
    print("* Date:", today)
    print("        *********")


def change_pin(cardHolder):
    new_pin = input("* Enter your new PIN: ")
    cardHolder.set_pin(new_pin)
    print("* PIN successfully changed!")


def pay_bill(cardHolder):
    try:
        print("        *********")
        bill_amount = float(input("* Enter the bill amount to pay (in Rps): "))
        if cardHolder.get_balance() < bill_amount:
            print("* Sorry, insufficient balance")
        else:
            cardHolder.set_balance(cardHolder.get_balance() - bill_amount)
            print("* Bill payment successful")
            print("* Bill amount:", bill_amount)
            print("* Date:", today)
            print("* Amount remaining:", cardHolder.get_balance())
        print("        *********")
    except ValueError:
        print("* Invalid input. Amount must be a number.")


if __name__ == "__main__":
    current_user = None
    list_of_cardHolders = [
        CardHolder("3181070575", 7058, "Furqan", "Zaka ud din", 5000),
        CardHolder("3333333333", 1103, "Raffay", "Afridi", 10000),
        CardHolder("3343297802", 6892, "Maleeha", "Waqar", 600),
        CardHolder("3452145129", 3971, "Muhammad", "Ali", 1200)
    ]

    print("       *********           ")
    print("* Welcome to THE RFM BANK!!")
    print("       *********           ")

    print("* Please insert your card...")
    time.sleep(2)
    print("Please wait while your card is being processed!")
    time.sleep(5)

    while True:
        card_number = input("* Please enter your debit card number: ")
        pin = int(input("* Please enter your PIN: "))

        for cardHolder in list_of_cardHolders:
            if cardHolder.get_cardNumber() == card_number and cardHolder.get_pin() == pin:
                current_user = cardHolder
                break

        if current_user is None:
            print("* Card number or PIN not recognized. Please try again.")
        else:
            print("************************")
            print("* Welcome, {} {}!".format(current_user.get_firstName(), current_user.get_lastName()))
            print("************************")
            break

    while True:
        print_menu()
        option = input("* Enter your choice (1-9): ")

        if option == "1":
            deposit(current_user)
        elif option == "2":
            withdraw(current_user)
        elif option == "3":
            Funds_Transfer(current_user)
        elif option == "4":
            Balance_Inquiry(current_user)
        elif option == "5":
            mini_statement(current_user, today)
        elif option == "6":
            account_Details(current_user)
        elif option == "7":
            change_pin(current_user)
        elif option == "8":
            pay_bill(current_user)
        elif option == "9":
            print("        *********")
            print(" *Thank you for using THE RFM BANK!")
            print("        *********")
            break
        else:
            print("* Invalid option. Please choose a valid option (1-9).")