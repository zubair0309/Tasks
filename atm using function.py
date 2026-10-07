import random
print("WELCOME TO  SBI ATM")
print("please enter your debit card")
print("choose the required options")
options=''' 

1: QUICK CASH,
2: TRANSFER,
3: BALANCE INQ;
4: REGISTRATION;
5: PIN GENERATION;
6: MINI statement;
7: EXIT;

'''
balance=100000000000000
transaction=[]
def quick_cash():
    global balance
    cash=input("enter the amount")
    if cash.isnumeric():
        cash=int(cash)
        if cash<=balance:
           print("please collect the cash")
           transaction.append(cash)
           balance-=cash
        else:
            print("amount excedes the current balance")
    else:
        ("enter the numerics")
    
def transfer():
    acc=input("enter the account number")
    print("account number should contain 10 digits")
    if len(acc)==10:
        amount=input("enter the amount")
        print(f"amount is successfully transfered to{acc}")
    else:
        print("enter the correct account number")

def balanceenq():
    print(f"balance{balance}")

def registration():
    name=print(input("enter your full name : "))
    aadhar=int(input("enter your aadharno : "))
    accountno=0
    while True:
        choice=input("enter 1 for current account or 2 for saveings account")
        if choice=="1":
            accountno=random.randint(1000000000 , 5000000000)
            print(f"{accountno}")
            break
        elif choice=="2":
            accountno=random.randint(6000000000 , 9000000000)
            print(f"{accountno}")
            break

def pingeneration():
    pin=random.randint(1000,9999)
    print(pin)
def ministatement():
   if len(transaction)>0:
      for i in transaction:
        print(i)
   else:
       print("no transctions")
       
def exit():
    print("thank you visit again")
    
print(options)
while True:
    choice=int(input("enter the options"))
    if choice==1:
        quick_cash()
    elif choice==2:
        transfer()
    elif choice==3:
        balanceenq()
    elif choice==4:
        registration()
    elif choice==5:
        pingeneration()
    elif choice==6:
         ministatement()   
    elif choice==7:
        exit()
        break    
           
    else:
        print("invalid option")
    
    
            
    


