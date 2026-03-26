import random

def guessing_game():
    while True:
        number = random.randint(1, 10)
        attempts = 0
        max_attempts = 5

        print("\nWelcome to Guessing Game 🎯")
        print("Guess a number between 1 and 10")
        print("You have 5 attempts")

        while attempts < max_attempts:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess == number:
                print("Correct! 🎉")
                print("Attempts used:", attempts)
                break

            elif guess < number:
                print("Too low ⬇️")

            else:
                print("Too high ⬆️")

        else:
            print("Game Over ❌")
            print("The number was:", number)

        # Replay option
        choice = input("Play again? (yes/no): ")

        if choice.lower() != "yes":
            print("Thanks for playing! 👋")
            break


guessing_game()