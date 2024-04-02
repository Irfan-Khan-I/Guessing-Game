import random

def play_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize the number of guesses
    num_guesses = 0
    
    print("Welcome to the Guessing Game!")
    print("I've picked a number between 1 and 100. Can you guess it?")
    
    while True:
        # Get the player's guess
        guess = int(input("Enter your guess (between 1 and 100): "))
        num_guesses += 1
        
        # Check if the guess is correct
        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {num_guesses} guesses!")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

# Start the game
play_game()
