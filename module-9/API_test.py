#Cameron Mendez
#07/06/2025
#Module 9.2a

import requests

#Test Google connection
try:
    response = requests.get('http://www.google.com')
    print("Google Test - Status Code:", response.status_code)
except Exception as e:
    print("Google connection failed:", e)

#Test the astronaut API
try:
    astro_response = requests.get("http://api.open-notify.org/astros.json")
    print("Astronaut API Status Code:", astro_response.status_code)

    if astro_response.status_code == 200:
        astronauts = astro_response.json()['people']
        print("\n-- Current Astronauts in Space --")
        for person in astronauts:
            print(f"Name: {person['name']}, Craft: {person['craft']}")
    else:
        print("Could not fetch astronaut data.")
except Exception as e:
    print("Astronaut API failed:", e)



input("Press Enter to exit...")