import random, string

def guessing_game():
    letters = string.ascii_lowercase
    target_letter = random.choice(letters)
    attempts = 0

    while True:
        guess = input("Guess a letter: ").lower()
        attempts += 1
        if guess == target_letter:
            print(f"Correct! It took you {attempts} attempts.")
            break
        else:
            print("Wrong guess, try again!")

guessing_game()
