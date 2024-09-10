import random

def guess_number_game():
    lower = 1
    upper = 100
    max_attempts = 10
    secret_number = random.randint(lower, upper)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between {lower} and {upper}.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < lower or guess > upper:
                print(f"Please enter a number within the range {lower_bound} to {upper_bound}.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've used all your attempts. The secret number was {secret_number}.")

guess_number_game()
