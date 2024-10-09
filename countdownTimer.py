import time

def countdown_timer(seconds):
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        time_format = f'{mins:02}:{secs:02}'
        print(f'\rTime left: {time_format}', end='', flush=True)
        time.sleep(1)
        seconds -= 1

    print("\nTime's up!")

countdown_time = int(input("Enter the time in seconds for the countdown: "))
countdown_timer(countdown_time)
