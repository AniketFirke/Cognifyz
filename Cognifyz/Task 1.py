import random

def guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("Rules: You need to guess the correct number between 1 and 100.")

    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Let's begin!")

    # Simulated guesses for sandboxed environments
    simulated_guesses = [50, 75, 62, 68, 65, 63]  # Replace with actual logic or test cases
    guess_index = 0

    while guess_index < len(simulated_guesses):
        try:
            guess = simulated_guesses[guess_index]
            print(f"Simulated input: {guess}")
            guess_index += 1
            attempts += 1

            # Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

if _name_ == "_main_":
    guessing_game()