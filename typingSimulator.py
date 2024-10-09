import time, random

def type_slowly(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(random.uniform(0.05, 0.2))  # Random typing delay
    print()  # For a new line after typing is complete

message = "Hello, this is a typing simulation"
type_slowly(message)
