from datetime import datetime

# Settings
url = ""
timezone = ""
timestamps = {}

# Retrive link at specific date and time
def get_timezone_adjusted_timestamp(timezone, timestamp) -> datetime:
    pass

# Form autofill script
def fill_form():
    pass

def submit_form():
    timestamp = get_timezone_adjusted_timestamp(timezone, timestamps)
    # Ex: {"Thursday": "12:30PM", "Friday": "12:30PM"}
    now = datetime.now()

def main():
    print("Running script", flush = True)
    submit_form()

if __name__ == "__main__":
    main()
