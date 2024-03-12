from datetime import datetime
import pytz

# Settings
url = ""
timezone = "Pacific/Auckland"
timestamps = {}

# Retrive link at specific date and time
def get_timezone_adjusted_timestamp(timezone, timestamp) -> datetime:
    tz = pytz.timezone(timezone)
    tz_now = datetime.now(tz)

    return tz_now

# Form autofill script
def fill_form():
    pass

def submit_form():
    pass

def main():
    print("Running script", flush = True)
    submit_form()

if __name__ == "__main__":
    main()
