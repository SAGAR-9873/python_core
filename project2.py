import random
def play_game():
    number = random.randint(1, 100)
    guesses = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            guesses += 1

            if guess > number:
                print("Lower number please")
            elif guess < number:
                print("Higher number please")
            else:
                print(f"Correct! You guessed the number in {guesses} attempts.")
                break

        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    play_game()
