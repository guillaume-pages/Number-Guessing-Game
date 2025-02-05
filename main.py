import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have a limited number of chances to guess the correct number.")
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

def get_replay_choice():
    while True:
        choice = input('If you want to play another game, write "again" or if you want to stop, write "exit": ').lower()
        if choice in ['again', 'exit']:
            return choice
        print("Invalid input. Please type 'again' or 'exit'.")

def game(number_to_guess, number_of_attempts):
    current_try = 1
    while current_try <= number_of_attempts:
        user_input = input(f"Attempt {current_try}/{number_of_attempts}. Enter your guess: ")
        if user_input.lower() == "exit":
            exit()
        
        try:
            user_guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        if user_guess == number_to_guess:
            print(f"\n🎉 Congratulations! You guessed the correct number in {current_try} attempt(s).")
            break
        elif user_guess < number_to_guess:
            print(f"The number is greater than {user_guess}.")
        else:
            print(f"The number is less than {user_guess}.")
        
        current_try += 1
    
    else:
        print("\n❌ Sorry, you failed to guess the number within the allowed attempts.")
        print(f"The correct number was {number_to_guess}.")
    
    replay = get_replay_choice()
    if replay == "again":
        main()
    elif replay == "exit":
        exit()

def start_game(difficulty):
    number_to_guess = random.randint(1, 100)
    attempts = {
        1: 10,
        2: 5,
        3: 3
    }
    print("\nThe game starts now!")
    print('If during the game you want to stop, type "exit".')
    game(number_to_guess, attempts[difficulty])

def main():
    while True:
        welcome_message()
        try:
            difficulty = int(input("\nChoose a difficulty (1, 2, or 3): "))
            if difficulty in [1, 2, 3]:
                start_game(difficulty)
            else:
                print("Invalid choice. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2, or 3).")

if __name__ == '__main__':
    main()
