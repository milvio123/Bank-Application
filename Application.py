Names = []
accountnumber = []
balance = []
names = 0
accountnumbers = 0
balances = 0
userentered = 0

def gettingname(Name):
    return Name
    
def gettingaccountnumber(AccountNumber):
    return AccountNumber
    
def gettingbalance(Balance):
    return Balance
    

    
def ifentered(userenter):
    numbtimes = 0
    if userenter == "P":
        while numbtimes < 5:
            name = gettingname(input("Please enter a name: "))
            Names.append(name)
            AN = gettingaccountnumber(input("Please enter an account number: "))
            accountnumber.append(AN)
            bal = gettingbalance(input("Please enter a balance: "))
            balance.append(bal)
            numbtimes+=1
    
    elif userenter == "S":
        accounttosearch = input("Please enter the account number to search: ")
        if int(accounttosearch)>5:
            print("The account number not found!")
        else:
            print("Name is: " + Names[int(accounttosearch)-1] + " and the balance is: " + str(balance[int(accounttosearch)-1]))
    
            
    elif userenter == "E":
        print("Thank you for using the program.")
        print("Bye")
    
    elif userenter == "D":
        accounttodep = input("Please enter the account number to add deposit: ")
        amounttodep = input("Please enter the amount to be deposited: ")
        balance[int(accounttodep)-1] = int(balance[int(accounttodep)-1]) + int(amounttodep)

    elif userenter == "W":
        accounttowith = input("Please enter the account number to withdraw: ")
        amounttowith = input("Please enter the amount to be withdraw: ")
        if int(amounttowith) > int(balance[int(accounttowith)-1]):
            print("ERROR: Not enough balance")
        else:
            balance[int(accounttowith)-1] = int(balance[int(accounttowith)-1]) - int(amounttowith)

    else:
        print("Invalid choice. Please try again!")


    
    
while userentered != "E":
    print("**** MENU OPTIONS ****")
    print("Type P to populate accounts")
    print("Type S to search for account")
    print("Type D to deposit Amount")
    print("Type W to withdraw Amount")
    print("Type E to exit")
    userentered = input("Please enter your choice: ")
    ifentered(userentered)

    
    
        
