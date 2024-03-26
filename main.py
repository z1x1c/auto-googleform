from datetime import datetime
from time import sleep
import requests

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

def form_is_open(url):
    try:
        response = requests.get(url)
        # Check if form accessible
        if response.status_code == 200:
            if "This form is no longer accepting responses" in response.text:
                return False
            else:
                return True
        else:
            print(f"Form returned status code {response.status_code}.")
            return False
    except Exception as e:
        print(f"An error occurred: {e}")
        raise e

def fill_form():
    email = "python@email.com"
    first_name = "John"
    last_name = "Doe"
    player_level = "Intermediate"
    is_member = "Yes"
    will_pay = "Yes"
    
    value = {
            "entry.emailAddress": email,
            "entry.559352220": first_name,
            "entry.1846655546": last_name,
            "entry.877086558": player_level,
            "entry.1459019614": is_member,
            "entry.861646923": will_pay,
            "pageHistory": "0,1",
            }
    
    return value


def submit_form(url, data):
    user_agent = {'Referer':'none','User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}

    session = requests.Session()

    try:
        res = session.post(url, data = data)
        if res.status_code != 200:
            raise Exception(f"Error {res.status_code}")
        return True
    except Exception as e:
        print(f"Error: {e}")
        raise e

def run():
    url = input("Enter form url: ").replace("viewform", "formResponse")

    print("Starting...")

    # while not(is_time()) and not():
    #     sleep(3)
    #     print("Not time yet...", flush = True)
    # while not(form_is_open(url)):
    #     sleep(3)
    #     print("Checking if form open...", flush = True)

    form_data = fill_form()
    submit_form(url, form_data)

if __name__ == "__main__":
    run()
