# Mini program of demo bank

class Apna_Bank: # initialize bank class 
    def __init__(self, Name, Balance):
        self.Name = Name
        self.Balance = Balance

    def deposit_amount(self, amount): # method for deposit amount 
        self.amount = amount
        if self.amount <= 0:
            return ("Amount should be +v value")
        else:
            print(f"Deposit {self.Balance} successful!")
            self.Balance += self.amount
            

    def withdrawal_amount(self, amount): # method for withdrawal amount
            self.amount = amount
            if self.amount <= 0:
                return ("Amount should be +v value")
            else:
                print(f"Withdrawal {self.Balance} successful!")
                self.Balance -= self.amount
                

    def display_details(self): # display details of user 
            print("Name of Account Holder:", self.Name)
            print("Account Balance:", self.Balance)

user1 = Apna_Bank("Pappu", 1000) # object of bank class for user 1

user1.display_details() # get details of user 

user1.deposit_amount(1000) # add amount in balance 
user1.display_details()

user1.withdrawal_amount(2000) # withdrawal amount in balance 
user1.display_details()