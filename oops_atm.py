class ATM:

    def __init__(self, bank, branch, location, balance):
        self.bank = bank
        self.branch = branch
        self.location = location
        self.balance = balance
        self.transactions = []
        self.name = ""
        self.aadhar = ""
        self.account_no = ""
        self.pin = ""

    def withdraw(self):
        amount = input("Enter Withdrawal Amount: ")

        if amount.isnumeric():
            amount = int(amount)

            if amount <= self.balance:
                self.balance -= amount
                self.transactions.append(f"Withdraw : Rs {amount}")
                print("Please Collect Your Cash")
                print("Available Balance :", self.balance)
            else:
                print("Insufficient Balance")
        else:
            print("Enter Numbers Only")

    def transfer(self):
        acc = input("Enter 10-Digit Account Number: ")

        if len(acc) == 10 and acc.isdigit():

            amount = input("Enter Transfer Amount: ")

            if amount.isnumeric():
                amount = int(amount)

                if amount <= self.balance:
                    self.balance -= amount
                    self.transactions.append(f"Transferred Rs {amount} to {acc}")
                    print("Money Transferred Successfully")
                else:
                    print("Insufficient Balance")
            else:
                print("Invalid Amount")
        else:
            print("Invalid Account Number")

    def balance_enquiry(self):
        print("Current Balance : Rs", self.balance)

    def registration(self):
        self.name = input("Enter Full Name : ")
        self.aadhar = input("Enter 12-Digit Aadhaar Number : ")

        if len(self.aadhar) == 12 and self.aadhar.isdigit():

            print("1. Savings Account")
            print("2. Current Account")

            choice = input("Choose Account Type : ")

            if choice == "1":
                print("Savings Account Selected")

            elif choice == "2":
                print("Current Account Selected")

            else:
                print("Invalid Choice")
                return

            self.account_no = input("Create 10-Digit Account Number : ")
            self.pin = input("Create 4-Digit ATM PIN : ")

            if len(self.account_no) == 10 and self.account_no.isdigit() and len(self.pin) == 4 and self.pin.isdigit():
                print("\nAccount Created Successfully")
                print("Account Holder :", self.name)
                print("Account Number :", self.account_no)
                print("ATM PIN :", self.pin)
            else:
                print("Invalid Account Number or PIN")

        else:
            print("Invalid Aadhaar Number")

    def mini_statement(self):
        if len(self.transactions) == 0:
            print("No Transactions Found")
        else:
            print("\n------ MINI STATEMENT ------")
            for i in self.transactions:
                print(i)

    def exit(self):
        print("Thank You for Using", self.bank, "ATM")
        print("Visit Again!")


# Object Creation
obj = ATM("XYZ BANK", "TADEPALLIGUDEM", "G3", 500000)

menu = """
1. Withdraw Cash
2. Money Transfer
3. Balance Enquiry
4. New Account Registration
5. Mini Statement
6. Exit
"""

print("=" * 35)
print("WELCOME TO", obj.bank)
print("=" * 35)
print("Branch   :", obj.branch)
print("Location :", obj.location)

while True:

    print(menu)

    choice = input("Enter Your Choice : ")

    if choice == "1":
        obj.withdraw()

    elif choice == "2":
        obj.transfer()

    elif choice == "3":
        obj.balance_enquiry()

    elif choice == "4":
        obj.registration()

    elif choice == "5":
        obj.mini_statement()

    elif choice == "6":
        obj.exit()
        break

    else:
        print("Invalid Choice")