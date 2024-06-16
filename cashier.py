class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        # Prompting to ask the user to enter a combination of coins 
        # Initialize the different coins followed by asking the user to enter each amount in the prompt
        print("Please insert coins.")
        larges = int(input("How many larges?: "))
        halfs = int(input("How many halfs?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))
        
        # The total variable is used to add all the combinations of coins as well as multiplying the coins based on their specific amount then returning the total 
        total = larges * 1 + halfs * 0.5 + quarters * 0.25 + nickels * 0.05
        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
         # if the users coins are equal or more than the cost, the user will recieve change back based on the different of the two. Otherwise it will return false if the user doesn't have enough the pay
        if coins >= cost:
            change = coins - cost
            print(f"Here is ${change:.2f} in change.")
            return True
        else:
            print("Sorry, that's not enoguh money. Money refunded. ")
            return False
