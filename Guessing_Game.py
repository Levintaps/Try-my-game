import random
import os
import sys

def guess_game():

    number_to_guess = random.randint(1, 10)
    attempts = 5

    print("Welcome to the Guessing Game!")
    print("Guess the number between 1 and 10.")
    print(f"You have {attempts} attempts to guess the correct number.\n")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))

            if guess == number_to_guess:
                print(f"Congratulations! You've guessed the number {number_to_guess} correctly!")
                return
            elif guess < number_to_guess:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Sorry! You've used all your attempts. The correct number was {number_to_guess}.")
    print("Your computer will shut down now.")

    # time.sleep(5)
    # os.system("shutdown /s /t 1")  # Restart command for Windows
    # os.system("shutdown /r /t 1")  # Shutdown command for Windows
    # os.system("sudo shutdown -r now")  # Restart command for Linux/macOS
    # os.system("sudo shutdown -h now")  # Shutdown command for Linux/macOS

if __name__ == "__main__":
    guess_game()
