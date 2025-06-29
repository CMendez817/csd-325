#Cameron Mendez
#Module 7.2
#06/28/2025

# city_functions.py

def city_country(city, country, population=None, language=None):
    """Return a formatted string with city, country, optional population, and optional language."""
    result = f"{city.title()}, {country.title()}"
    
    if population:
        result += f" - population {population}"
    
    if language:
        result += f", {language.title()}"
    
    return result

# Function calls with population
print(city_country("santiago", "chile"))
print(city_country("tokyo", "japan", 14000000))
print(city_country("paris", "france", 2148000, "french"))

# Keep the window open after running
input("\nPress Enter to exit...")