import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    print("What would you like? (small/ medium/ large): ")
    # User input for sandwich size choice, convert to lowercase
    choice = input().strip().lower()
    
    order_ingredients = recipes[choice]["ingredients"]
    # Check if resources are sufficient
    if sandwich_maker_instance.check_resources(order_ingredients):
        cost = recipes[choice]["cost"]
        print(f"Order cost is: ${cost:.2f}")
        coins = cashier_instance.process_coins()

        # Process transaction and make sandwich if successful    
        if cashier_instance.transaction_result(coins, cost):
            sandwich_maker_instance.make_sandwich(choice, order_ingredients)
            print(f"{choice.capitalize()} sandwich is ready. Bon appetit!")
    else:
        print("Sorry, there aren't enough resources to make the sandwich.")

if __name__ == "__main__":
    main()
