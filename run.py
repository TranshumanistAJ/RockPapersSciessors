def print_logo():
    print("""

 ######                                                                                                                   
 #     #  ####   ####  #    #    #####    ##   #####  ###### #####      ####   ####  #  ####   ####   ####  #####   ####  
 #     # #    # #    # #   #     #    #  #  #  #    # #      #    #    #      #    # # #      #      #    # #    # #      
 ######  #    # #      ####      #    # #    # #    # #####  #    #     ####  #      #  ####   ####  #    # #    #  ####  
 #   #   #    # #      #  #      #####  ###### #####  #      #####          # #      #      #      # #    # #####       # 
 #    #  #    # #    # #   #     #      #    # #      #      #   #     #    # #    # # #    # #    # #    # #   #  #    # 
 #     #  ####   ####  #    #    #      #    # #      ###### #    #     ####   ####  #  ####   ####   ####  #    #  ####  
                                                                                                                          

    """)


def main_menu():
    print_logo()
    print('Please select from one of the following options')
    print('-----------')
    print('1. Play the game')
    print('2. View the rules')
    print('3. Reset the scores')
    print('4. Exit')
    print('-----------')
    can_continue = False

    while not can_continue:
        choice = input('choose between 1 - 3 \n')
        if choice == '1':
            print('option 1 pressed')
            can_continue = True
        elif choice == '2':
            print('option 2 pressed')
            can_continue = True
        elif choice == '3':
            print('option 3 pressed')
            can_continue = True
        elif choice == '4':
            exit()
        else:
            print('incorrect option chosen')

main_menu()
