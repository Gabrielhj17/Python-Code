import random

def scramble_word(word):
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def word_scramble_game():
    words = ["python", "javascript", "computer", "keyboard", "function"]
    target_word = random.choice(words)
    scrambled_word = scramble_word(target_word)

    print(f"Scrambled word: {scrambled_word}")
    
    while True:
        guess = input("Guess the original word: ").lower()
        if guess == target_word:
            print("Correct!")
            break
        else:
            print("Wrong guess, try again!")

word_scramble_game()
