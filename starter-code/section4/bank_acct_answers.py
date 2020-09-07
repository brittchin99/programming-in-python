#PROJECT: Bank Account
#INSTRUCTIONS - create a bank account class that allows users to log in or create a bank account.
#once the user logs in, they can get their account info, balance, deposit money, or withdraw money

#Note: this project currently uses a hardcoded login (because I didn't want to work with files)
#Ideally, you should store user info in an external file or database

#import for password hashing
import hashlib, binascii, os

class BankAccount():

    acct_id = 1000

    #temporary "database"
    accounts = []

    def __init__(self, firstName, lastName, email, password):
        '''creates a new instance of a bank account when a new account is created
        balance should be set to $0, id should be set to the next available id'''
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        #store password as hashed (hashPassword(password))
        self.password = hashPassword(password)
        self.balance = 0
        self.id = BankAccount.acct_id
        BankAccount.acct_id += 1
        BankAccount.accounts.append({"email": self.email, "user": self})

    def getAccountInfo(self):
        '''displays all user info'''
        print("Name: {} {}".format(self.firstName, self.lastName))
        print("Email:", self.email)
        print("Account ID:", self.id)
        print("Current balance: ${}".format(self.balance))
        
    def getBalance(self):
        ''''''
        print("Available Balance: ${}".format(self.balance))
        
    def deposit(self):
        '''deposits money into the user's account'''
        amount = float(input("Enter amount to be deposited: $")) 
        self.balance += amount 
        print("Amount Deposited: ${}".format(amount))
        print("Your new balance is ${}".format(self.balance))

    def withdraw(self):
        '''withdraws money from the user's account, should check if the balance is enough to withdraw'''
        amount = float(input("Enter amount to be withdrawn: $")) 
        if self.balance >= amount:
            self.balance -= amount
            print("Amount Withdrawn: ${}".format(amount))
            print("Your new balance is ${}".format(self.balance))
        else: 
            print("Insufficient balance.")

#---DO NOT TOUCH THIS CODE---
#hashing for passwords
def hashPassword(password):
        '''Hash a password for storing.'''
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), 
                                    salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')
 
def verifyPassword(stored_password, provided_password):
    '''Verify a stored password against one provided by user'''
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512', 
                                  provided_password.encode('utf-8'), 
                                  salt.encode('ascii'), 
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
#----------------------------

def main():
    #---DO NOT TOUCH THIS CODE---

    #Sample accounts to test login
    sample1 = BankAccount("Lexa", "Clarke", "lclarke@gmail.com", "commander123")
    sample2 = BankAccount("Harry", "Potter", "hpotter@gmail.com", "leviosa")
    sample3 = BankAccount("Karen", "Smith", "momager@gmail.com", "ilovemy3kids")

    for account in BankAccount.accounts:
        user = account["user"]
        if (user.firstName == "Lexa"):
            user.balance = 150.0
        elif (user.firstName == "Harry"):
            user.balance = 30.0
        else:
            user.balance = 10.0
##        account["user"].getAccountInfo()

    #{firstName: "Lexa", lastName: "Clarke", email: "lclarke@gmail.com", password: "commander123", id: 1000}
    #{firstName: "Harry", lastName: "Potter", email: "hpotter@gmail.com", password: "leviosa", id: 1001}
    #{firstName: "Karen", lastName: "Smith", email: "momager@gmail.com", password: "ilovemy3kids", id: 1002}

    #----------------------------
    
    loggedIn = False
    done = False

    #for simplicity, assume the user will always enter a number
    while not done:
        print("Welcome to the Deposit & Withdrawal Machine.")
        print("MENU")
        print("1. Log in\n2. Create account\n3. Quit")
        answer = input("What would you like to do? Please enter the option number: ")
        answer = int(answer)

        if (answer == 1): #log in
            #ask for login info
            email = input("Please enter the email associated with your account: ")
            password = input("Please enter your password: ")
            user = {}
            for account in BankAccount.accounts: #find user object in "database"
                if account["email"] == email:
                    user = account["user"]

            if (user == {}): #user was not found in the "database"
                print("Invalid login credentials.")
                
            else:
                #verify if password is correct -- stored password is hashed - must be checked with verifyPassword()
                stored_password = user.password

                if (verifyPassword(stored_password, password)):
                    print("Sucessfully logged in.")
                    loggedIn = True

        elif(answer == 2): #create the user's account
            firstName = input("Please enter your first name: ")
            lastName = input("Please enter your last name: ")
            email = input("Please enter an email for your account: ")
            password = input("Please enter your password: ")
            user = BankAccount(firstName, lastName, email, password)
            print("Account created successfully.")
            loggedIn = True
            
        elif(answer == 3): #quit
            print("Thank you for using the Deposit & Withdrawal Machine. Goodbye!")
            done = True

        else:
            print("Invalid option.")

        while loggedIn:
            print()
            print("MENU")
            print("1. Get Account Info\n2. Get Balance\n3. Make a deposit\n4. Make a withdrawal\n5. Log out")
            answer = input("What would you like to do? Please enter the option number: ")
            answer = int(answer)

            if(answer == 1): #get account info
                user.getAccountInfo()

            elif(answer == 2): #get balance
                user.getBalance()
                
            elif(answer == 3): #deposit
                user.deposit()
                
            elif(answer == 4): #withdraw
                user.withdraw()
                
            elif(answer == 5): #log out

                #store user info in the "database" -- this won't actually save
                for account in BankAccount.accounts:
                    if account["email"] == email:
                        account["user"] = user

                #log out user and exit the program
                print("Thank you for using the Deposit & Withdrawal Machine. Goodbye!")
                loggedIn = False
                done = True

            else:
                print("Invalid option.")

        print()
    
        
if __name__ == "__main__":
    main()
