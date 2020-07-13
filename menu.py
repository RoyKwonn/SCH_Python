def menu_list(itm):
    option = 1
    for choice in itm:
        print(str(option) + ". " + choice)
        option = option + 1
    print(str(option) + ". Quit")
    return option
