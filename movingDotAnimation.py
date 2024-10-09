import time

def moving_dot():
    width = 50
    for i in range(width):
        print(' ' * i + 'o', end='\r')  # Move 'o' horizontally
        time.sleep(0.05)
    print()  # New line when finished

moving_dot()
