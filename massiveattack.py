import requests
import os
import time
from colorama import Fore

while True:
    try:
        response = requests.get("https://timeapi.io/api/Time/current/zone?timeZone=Europe/Amsterdam")
        data = response.json()
        year = data["year"]
        month = data["month"]
        day = data["day"]
        hour = data["hour"]
        minute = data["minute"]
        seconds = data["seconds"]


        time.sleep(0.9)
        os.system("cls")
        print(Fore.GREEN, year, "/", month, "/", day, "   ", hour, ":", minute, ":", seconds)
    except Exception as e:
        print("Error occured: ", e)
        with open('logreport_massiveattack.txt', 'w') as f:
            f.write(str(e))
