def shopping_cart():
    responses = {}
    active = True
    while active:
        name = input('Welcome to Yosef\'s store! What is your name? ')
        opening = input(f'Hello {name}! Would you like to "add"/"delete" an item or "view shopping cart"? Enter "quit" to complete your visit. ')


        if opening.title() == 'Add' or 'Add' in opening.title():
            add_items = input('What would you like to add? ')
            if add_items:
                price_items = float(input(f'Looks like you chose to add {add_items}. Please enter the price: $'))
                if price_items:
                    # add item to dictionary
                    print(f'You have successfully added {add_items} to your shopping cart!')
                    retry = input('Would you like to add another item?')
                    if retry.title() == 'No' or retry.title() == 'N':
                        active = False
                responses[add_items] = price_items


        elif opening.title() == 'Delete' or 'Delete' in opening.title():
            delete_items = input(f'Are you sure you would like to remove {add_items} from your shopping cart? ')
            if delete_items:
                # delete item from dictionary
                del responses[add_items]
                print(f'You have successfully removed {delete_items} to your shopping cart!')
                

        elif opening.title() == 'View Shopping Cart' or 'View' in opening.title():
            # show final shopping cart
            print('----------Shopping Cart----------')
            for key, value in responses.items():
                print (f"\t{key.title()}   x   {value}")
            print('--------------Total--------------')
        elif opening.title() == 'Quit':
            active = False 


    for key, value in responses.items():
        print (f"{key.title()}'s address is {value}.")


shopping_cart()