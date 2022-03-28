class Atm:
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pin = pinNumber
   
    def check_balance(self):
        print("Your balance is 100 rupees")

    def depositAmount(self, amount):
        new_amount=0+amount   
        print("You have deposited "+str(amount)+" in your bank. Your current balance is "+str(new_amount))

    def withdrawlMoney(self,amount):
        new_amount=0-amount
        print("You have withdrawl"+str(amount)+"from your bank. Your current balance is"+str(new_amount))

def main():
    Card_number = input("Insert your card number: ")
    pin_number  = input("Enter your pin number: ")

    new_user =  Atm(Card_number ,pin_number)

    print("Choose your activity ")
    print("1. Cash Withdrawl 2. Balance Inquiry")
    activity = int(input("Enter activity number : "))
        
    if (activity == 1):
        amount = int(input("Enter the amount: "))
        new_user.withdrawlMoney(amount)
       
    elif (activity == 2):
       new_user.check_balance()
    else:
        print("Enter a valid number")


if __name__ == "__main__":
    main()