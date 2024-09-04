import random
import time

colors = {
    "Black": "\033[30m",
    "Red": "\033[31m",
    "Green": "\033[32m",
    "Yellow": "\033[33m",
    "Blue": "\033[34m",
    "Magenta": "\033[35m",
    "Cyan": "\033[36m",
    "White": "\033[37m",
    "Reset": "\033[0m"
}


def print_message(message, color):
    print(f"{colors[color]}{message}{colors['Reset']}")


def countdown():
    print_message("The game will start in...", "Yellow")
    for i in range(3, 0, -1):
        print(f"\r{colors['Blue']}{i}{colors['Reset']}", end=' ', flush=True)
        time.sleep(1)
    print_message("Go!", "Green")


def main():
    attempts_easy = 10
    attempts_medium = 5
    attempts_hard = 3

    print_message("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have a certain number of chances to guess the correct number.""", "Yellow")
    print()

    while True:
        countdown()

        computer = random.randint(1, 100)
        attempts = 0

        print_message("""Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)""", "Blue")

        try:
            choice_user = int(input("Enter your choice: "))
        except ValueError:
            print_message("ERROR! Please enter a valid number.", "Red")
            continue

        if choice_user == 1:
            chances = attempts_easy
            print_message("Great! You have selected the Easy difficulty level.", "Green")
        elif choice_user == 2:
            chances = attempts_medium
            print_message("Great! You have selected the Medium difficulty level.", "Green")
        elif choice_user == 3:
            chances = attempts_hard
            print_message("Great! You have selected the Hard difficulty level.", "Green")
        else:
            print_message("Incorrect number. Please select a valid option.", "Red")
            continue

        print_message("Let's start the game!", "Green")
        print_message("The computer is thinking...", "Yellow")
        for i in range(3, 0, -1):
            print(f"\r{colors['Blue']}{i}{colors['Reset']}", end=' ', flush=True)
            time.sleep(1)

        while True:
            try:
                guess_user = int(input("Enter your guess: "))
            except ValueError:
                print_message("ERROR! Please enter a valid number.", "Red")
                continue

            attempts += 1
            chances -= 1
            if guess_user > computer:
                print_message(f"Incorrect! The number is less than {guess_user}.", "Red")
            elif guess_user < computer:
                print_message(f"Incorrect! The number is greater than {guess_user}.", "Red")
            elif guess_user == computer:
                print_message(f"Congratulations! You guessed the correct number in {attempts} attempts.", "Green")
                break

            if chances == 0:
                print_message(f"Unfortunately, you lost! The number was {computer}.", "Red")
                break

            print_message(f"You only have {chances} more attempts.", "Red")

        restart = input("Would you like to play again? (Y/N): ").upper().strip()
        if restart == "N":
            print_message("Thanks for playing. I hope you come back soon.", "Blue")
            break


if __name__ == "__main__":
    main()
