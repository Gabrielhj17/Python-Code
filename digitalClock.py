import time

def digital_clock():
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(f"\rCurrent Time: {current_time}", end='', flush=True)
        time.sleep(1)

digital_clock()
