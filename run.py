import random

# Print Logo
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

# Show Rules
def show_rules():
    print("""
    Rules:
    - Rock crushes Scissors
    - Scissors cuts Paper
    - Paper covers Rock
    """)
    input("Press enter to continue")
    main_menu()

# Main Menu
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

# Get User's Choice
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

# Get Computer's Choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Determine Winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return "You win!"
    else:
        return "Computer wins!"

# Reset Scores
def reset_scores():
    print("Word")
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    print("Scores have been reset.")

# Play Game
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

# Initialize Scores
user_score = 0
computer_score = 0

if __name__ == "__main__":
    main_menu()
