#Cameron Mendez
#Revised 06/08/25
#Weather App 


#Tools to complete search requests
import requests
import re

#Define OpenWeather API key and base URL
API_KEY = '906b6939735602a519447e37a839d229'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'


#Function to validate zip code using RegEx
def is_valid_zip(zip_code):
    return bool(re.match(r'^\d{5}$', zip_code))#Validate with 5 digit Zip only


#Function to fetch weather data w/ the OpenWeather API
def get_weather(zip_code):
    #Construct the API URL with the zip code and API key
    url = f'{BASE_URL}?zip={zip_code},us&appid={API_KEY}&units=imperial'  #units=imperial for Fahrenheit
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        if data.get('cod') == 200:
            #Extract needed data
            city = data['name']
            weather = data['weather'][0]['description']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind_speed = data['wind']['speed']

            #Display the weather data
            print(f"\nWeather in {city}:")
            print(f"Temperature: {temp}°F")
            print(f"Condition: {weather}")
            print(f"Humidity: {humidity}%")
            print(f"Wind Speed: {wind_speed} mph")
        else:
            print("Error: Could not fetch weather data.")
    else:
        print(f"Failed to retrieve data. HTTP Status code: {response.status_code}")


#Main program loop
def main():
    while True:
        #Get user zip code
        zip_code = input("Please enter your 5-digit zip code: ").strip()

        #Validate zip code
        if not is_valid_zip(zip_code):
            print("Invalid zip code. Please enter a valid 5-digit zip code.")
            continue

        #Get and display weather data
        get_weather(zip_code)

        #Ask if the user wants to check another area
        repeat = input("\nWould you like to check another zip code? (y/n): ").strip().lower()
        if repeat != 'y':
            print("Goodbye!")
            break

if __name__ == '__main__':
    main()

# Keep the program window open when opened in folder
input("\nPress Enter to exit...")