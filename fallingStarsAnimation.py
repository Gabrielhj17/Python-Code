import random
import time

def falling_stars():
    width = 50
    for _ in range(30):
        star_position = random.randint(0, width)
        print(' ' * star_position + '*')
        time.sleep(0.1)

falling_stars()
