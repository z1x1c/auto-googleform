from datetime import datetime
from time import sleep

def is_time():
    now = datetime.now()

    # Check if it is Monday
    is_monday = now.weekday() == 0

    # Check if it is between 12:30-12:40 
    is_in_timeframe = now.hour == 12 and now.minute <= 40 and now.minute >= 30

    if is_monday and is_in_timeframe:
        return True
    else:
        return False

def form_is_open():
    pass

def fill_form():
    pass

def submit_form():
    pass

def run():
    print("Starting...")

    while not(is_time()) and not():
        sleep(3)
        print("Not time yet...", flush = True)
    while not(form_is_open()):
        sleep(3)
        print("Checking if form open...", flush = True)

    fill_form()
    submit_form()

def main():
    run()

if __name__ == "__main__":
    main()
