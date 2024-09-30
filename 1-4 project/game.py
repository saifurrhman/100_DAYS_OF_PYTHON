import random

def get_difficulty_level():
    print("Choose a difficulty level:")
    print("1. Easy (1-10, unlimited attempts)")
    print("2. Medium (1-50, 10 attempts)")
    print("3. Hard (1-100, 5 attempts)")
    
    while True:
        choice = input("Enter the number corresponding to the difficulty level: ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

def play_game(level):
    if level == 1:
        number_to_guess = random.randint(1, 10)
        attempts = float('inf')  # Unlimited attempts
    elif level == 2:
        number_to_guess = random.randint(1, 50)
        attempts = 10
    else:
        number_to_guess = random.randint(1, 100)
        attempts = 5

    print(f"You have {attempts} attempts to guess the number.")

    while attempts > 0:
        guess = input(f"Enter your guess (between {1 if level == 1 else 1} and {10 if level == 1 else 100}): ")
        
        # Validate input
        if not guess.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(guess)

        if (level == 1 and not (1 <= guess <= 10)) or \
           (level == 2 and not (1 <= guess <= 50)) or \
           (level == 3 and not (1 <= guess <= 100)):
            print(f"Please guess a number within the range!")
            continue

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You've guessed the number.")
            return

        attempts -= 1
        if attempts > 0:
            print(f"You have {attempts} attempts left.")
        else:
            print(f"Game Over! The correct number was {number_to_guess}.")

def main():
    while True:
        difficulty_level = get_difficulty_level()
        play_game(difficulty_level)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

if __name__ == "__main__":
    main()
