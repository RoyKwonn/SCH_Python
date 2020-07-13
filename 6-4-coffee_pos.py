from transactions import *
import promotion
import starbuzz
import menu

items = ["DONUT", "LATTE", "FILTER", "MUFFIN"]
prices = [1.50, 2.20, 1.80, 1.20]
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
