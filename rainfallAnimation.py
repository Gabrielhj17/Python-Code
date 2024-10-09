import random
import time

def rainfall_animation():
    width = 40
    height = 10
    for _ in range(50):
        raindrop_pos = random.randint(0, width - 1)
        for i in range(height):
            screen = [' ' * width for _ in range(height)]
            screen[i] = screen[i][:raindrop_pos] + '|' + screen[i][raindrop_pos+1:]
            print("\n".join(screen))
            print("\n" + "-" * width)
            time.sleep(0.1)
            print("\033c", end="")

rainfall_animation()
