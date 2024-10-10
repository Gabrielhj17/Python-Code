import string, time, random

letters = string.ascii_letters + " "
target = "Hello World"
result = ""

for letter in target:
    while True:
        I = random.choice(letters)
        print(result + I)
        if I == letter:
            result += I
            break
        time.sleep(0.01)
