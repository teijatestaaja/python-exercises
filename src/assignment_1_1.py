def ask_amount():
    amount = input("How many do you wish to buy? ")
    return amount

def ask_price():
    price = input("What is the price in euros? ")
    return price

def ask_product(number):
    if number == 1:
        index = "first"
    else:
        index = "second"
    product = input("What is the " + index + " product you want to buy? ")
    return product

def count_total(amount_1, amount_2, price_1, price_2):
    total = int(amount_1) * (float(price_1)) + (int(amount_2) * float(price_2))
    return total

def welcome():
    print("Hello, welcome to the Python store!")

def goodbye():
    print("Thank you! Goodbye! See you soon again!")

def main():
    welcome()
    product_1 = ask_product(1)
    price_1 = ask_price()
    amount_1 = ask_amount()

    product_2 = ask_product(2)
    price_2 = ask_price()
    amount_2 = ask_amount()

    total = count_total(amount_1, amount_2, price_1, price_2)

    print("You are buying " + str(amount_1) + " pieces of " + str(product_1) + " and " + str(amount_2) + " pieces of " + str(product_2) + " from our store.")
    print("That will cost you " + str(total) + " euros in total.")
    
    goodbye()

main()