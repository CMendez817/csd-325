#Cameron Mendez
#07/06/2025
#Module 9.2
#Futurama API


import requests

# Test connection to Futurama Characters API
url = "https://futurama-api.fly.dev/api/v2/characters"
response = requests.get(url)
print("Connection to Futurama Characters API status code:", response.status_code)

# Print raw JSON text
print("\nRaw JSON Response:")
print(response.text[:1000])

# Format and display character info
if response.status_code == 200:
    characters = response.json()
    print("\n-- Futurama Character Info --\n")
    for char in characters[:5]:
        name = char['name']
        full_name = f"{name['first']} {name.get('middle', '')} {name['last']}".strip()
        species = char.get('species', 'Unknown')
        age = char.get('age', 'Unknown')
        planet = char.get('planet', 'Unknown')

        print(f"Name: {full_name}")
        print(f"Species: {species}")
        print(f"Age: {age}")
        print(f"Planet: {planet}\n")
else:
    print("Failed to fetch character data.")

input("Press Enter to exit...")
