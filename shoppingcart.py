def addresses():
    responses = {}
    active = True
    while active:
        name = input('Welcome to Yosef\'s store! What is your name? ')
        opening = input(f'Hello {name}! Would you like to "add"/"delete" an item or "view shopping cart"? Enter "quit" to complete your visit. ')


        if opening.title() == "Add" or "Add" in opening.title():
            add_items = input('What would you like to add? ')
            if add_items:
                cost_items = input(f'Looks like you chose the {add_items}. Please enter the price: ')
                if cost_items

        elif opening.title() == "Delete" or "Delete" in opening.title():
            delete_items = input('What item would you like to delete? ')

        elif opening.title() == 'View Shopping Cart' or "View" in opening.title():
            for key, value in responses.items():
                print (f"{key.title()}'s address is {value}.")

        elif opening.title() == 'Quit':
            active = False 
            print(responses)
            for key, value in responses.items():
                print (f"{key.title()}'s address is {value}.")


addresses()