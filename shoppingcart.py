def shopping_cart():
    responses = {}
    total = 0
    active = True
    while active:
        name = input('Welcome to Yosef\'s store! What is your name? ')
        opening = input(f'Hello {name}! Would you like to "add"/"delete" an item or "view shopping cart"? Enter "quit" to complete your visit. ')


        if opening.title() == 'Add' or 'Add' in opening.title():
            add_items = input('What would you like to add? ')
            if add_items:
                price_items = float(input(f'Looks like you chose to add {add_items}. Please enter the price: $'))
                if price_items:
                    responses[add_items] = price_items
                    print(f'You have successfully added {add_items} to your shopping cart!')
                    while True:
                        retry = input('Would you like to add another item? ')
                        if retry.title() == 'Yes' or retry.title() == 'Y':
                            add_items = input('What would you like to add? ')
                            if add_items:
                                price_items = float(input(f'Looks like you chose to add {add_items}. Please enter the price: $'))
                                if price_items:
                                    responses[add_items] = price_items
                                    print(f'You have successfully added {add_items} to your shopping cart!')
                        elif retry.title() == 'No' or retry.title() == 'N':
                            break
                        else:
                            print('That is not a correct ansnwer. Please input "Yes" or No"')



        elif opening.title() == 'Delete' or 'Delete' in opening.title():
            delete_items = input(f'What item would you like to remove? ')
            if delete_items.title():
                del responses[delete_items]
                print(f'You have successfully removed {delete_items} to your shopping cart!')
                

        elif opening.title() == 'View Shopping Cart' or 'View' in opening.title():
            print('\n----------Shopping Cart----------')
            for key, value in responses.items():
                total += value
                print (f"\t{key.title()}   x   ${value}")
            print('--------------Total--------------')
            print(f'Your total for today is: {total}\n')

        elif opening.title() == 'Quit':
            active = False 



    print(f'\n------{name.title()}\'s Shopping Cart------')
    for key, value in responses.items():
        print (f"\t{key.title()}   x   ${value}")
    print('--------------Total--------------')
    print(f'Your total for today is: {total}\n')
            


shopping_cart()