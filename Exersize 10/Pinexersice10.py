print("Welcome to The Bank of Darren")

attempts = 3   #<-- Variable is attempts
UserPin = 1234 # <-- Variable is UserPin

while attempts != 0:  # <--saying whilst 3 is not equal (!=) to 0
    Pin = int(input("Please Enter 4 digit Pin: "))  #<-- Saying is the Pin is e
    if Pin != UserPin:  #<-- If Pin is not equal to User Pin
        attempts -= 1 #<-- if false subtracy 1
        print ("Incorrect pin number", attempts, "attempts left") # <-- What it will print
    else:
        UserChoice = input("d: Deposit or w: Withdraw: ")  # <-- Asking for you to input d or w when you run
        if UserChoice == "d":     #<-- Saying if user choice is d
            UserDeposit = input("Enter Amount: ")  #<-- Asking you to input a amount when run
            print(UserDeposit, "£ deposited successfully") #<-- once inputted will display messsage
        if UserChoice == "w":               #<-- Saying if user choice is d
            UserWithdraw = input("Enter amount to withdraw: ")      #<-- Asking you to input a amount when run
            print(UserWithdraw, "£ Withdrawn successfully")          #<-- once inputted will display messsage
    UserExit = input("Would you like to continue Y/N: ")     #<-- saying if to input a prompt
    if UserExit == "n":
        print("Thank you for being a Bank of Darren Customer")         #<-- exit message
        break
    else:
        continue         