import random
# This will be used to generate the computer's choice in the game.

# This function prints the art logo for the game when called
def print_logo():
    print("""
    ######                                                                                                                   
    #     #  ####   ####  #    #    #####    ##   #####  ###### #####      ####   ####  #  ####   ####   ####  #####   ####  
    #     # #    # #    # #   #     #    #  #  #  #    # #      #    #    #      #    # # #      #      #    # #    # #     
    #     # #    # #      ######    #    # #    # #      #####  #    #    #  ### #    # # ####   ####   #    # #####   ####  
    #     # #    # #      #    #    #    # ###### #      #      #####      #    # #    # # #      #      #    # #   #      #
    #     # #    # #    # #    #    #    # #    # #    # #      #   #      #    # #    # # #      #      #    # #    # #    #
     #####   ####   ####  #    #     #####  #    #  ####  ###### #    #      ####   ####  #  ####   ####   ####  #    #  ####
    """)

# This function displays the rules of the game and waits for the user to press enter before returning to the main menu.
def show_rules():
    print("""
    Rules:
    - Rock crushes Scissors
    - Scissors cuts Paper
    - Paper covers Rock
    """)
    input("Press enter to continue")
    main_menu()

# This function displays the main menu, prints the logo, and handles user input for menu choices
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
        choice = input('Choose between 1 - 4: ')
        if choice == '1':
            play_game()
            can_continue = True
        elif choice == '2':
            show_rules()            
            can_continue = True
        elif choice == '3':
            reset_scores()
            main_menu()
            can_continue = True
        elif choice == '4':
            exit()
        else:
            print('Incorrect option chosen. Please try again.')

# This function prompts the user for their choice, validates the input, and returns the full word rock paper or sciessors
def get_user_choice():
    user_input = input("Enter your choice (rock(r), paper(p), scissors(s)): ").lower()
    while user_input not in ['rock', 'paper', 'scissors', 'r', 'p', 's']:
        print("Invalid choice. Please try again.")
        user_input = input("Enter your choice (rock(r), paper(p), scissors(s)): ").lower()
    if user_input == 'r':
        return 'rock'
    elif user_input == 'p':
        return 'paper'
    elif user_input == 's':
        return 'scissors'
    else:
        return user_input

# This function randomly selects and returns the computer's choice using the crandom computer choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# This function compares the user's choice with the computer's choice and returns the result of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# This function resets both the user's and computer's scores to zero
def reset_scores():
    print("Word")
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    print("Scores have been reset.")

# This function contains the main game loop, handling multiple rounds of the game until the user chooses to stop playing
def play_game():
    global user_score, computer_score
    print("Welcome to Rock-Paper-Scissors!")
    user_name = input("Enter your name: ")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"{user_name} chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        print(f"Scores - {user_name}: {user_score}, Computer: {computer_score}")
        continue_playing = input("Do you want to play again? (y/n): ").lower()
        if continue_playing != 'y':
            break
    main_menu()

# These global variables keep track of the scores for the user and computer
user_score = 0
computer_score = 0

if __name__ == "__main__":
    main_menu()
