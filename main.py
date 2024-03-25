from datetime import datetime
from time import sleep
import pytz

# Settings
url = ""
timezone = "Pacific/Auckland"
timestamps = ""

def get_timezone_adjusted_timestamp(timezone_str, timestamp_str) -> datetime:
    try:
        timestamp = datetime.fromisoformat(timestamp_str)
        target_timezone = pytz.timezone(timezone_str)
        tz_aware_timestamp = timestamp.replace(tzinfo=pytz.utc).astimezone(target_timezone)

        return tz_aware_timestamp
    except Exception as e:
        print(f"Error converting timestamp to local time ({timezone})")

def fill_form():
    pass

def submit_form():
    pass

def is_time(offset_minute = 0):
    now = datetime.now()

    # Check if it is Thursday
    is_thursday = now.weekday() == 3

    # Check if it is 12:30PM
    is_1230_pm = now.hour == 12 and now.minute == 30

    # Check if it is within 10min after specified time
    is_in_10min = now.hour == 12 and now.minute <= 40 and now.minute >= 30

    if is_thursday and is_in_10min:
        return True
    else:
        return False

# Could use ML to predict form open time period
def within_speculated_timeframe():
    pass

def form_is_open():
    pass

def run():
    print("Starting...")

    while not(is_time()) and not():
        print("Not time yet...", flush = True)
        sleep(5)
    while not(form_is_open()):
        print("Checking if form open...", flush = True)
        sleep(5)

    fill_form()
    submit_form()

def main():
    run()

if __name__ == "__main__":
    main()
