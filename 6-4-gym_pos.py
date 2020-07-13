from transactions import *
import promotion
import starbuzz
import menu

items = ["WORKOUT", "WEIGHTS", "BIKES"]
prices = [35.0, 10.0, 8.0]
running = True

while running:
    opt = menu.menu_list(items)
    choice = int(input("Choose an option : "))
    if choice == opt:
        running = False
    else:
        credit_card = input("Credit card number : ")
        price = promotion.discount(prices[choice - 1])
        if input("Starbuzz card? ") == "Y":
            price = starbuzz.discount(price)
        save_transaction(price, credit_card, items[choice-1])
