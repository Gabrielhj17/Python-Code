import random

number = int(random.randint(1, 20))

def guessLoop(number, guesses=0):
    guess = int(input("Guess a number between 1 and 20: "))
    guesses += 1  # Increment guesses each time a guess is made
    
    if guess == number:
        print(f"Congratulations! You guessed the correct number. It took you {guesses} guesses.")
    elif guess < number:
        print("Too low! Try again.")
        guessLoop(number, guesses)
    else:
        print("Too high! Try again.")
        guessLoop(number, guesses)  
    
guessLoop(number)
