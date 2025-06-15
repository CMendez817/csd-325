#Cameron Mendez
#Module 4.2
#06/14/2025

#Revisions made to sitka_highs.py

import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

# Function to read temperature data (highs or lows) from the CSV file
def get_weather_data(temp_type='high'):
    filename = filename = 'sitka_weather_2018_simple.csv'
    dates, temps = [], []

    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)

        for row in reader:
            try:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                if temp_type == 'high':
                    temp = int(row[5])  # High temperature
                elif temp_type == 'low':
                    temp = int(row[6])  # Low temperature
                else:
                    raise ValueError("Invalid temperature type.")
            except ValueError:
                # Skip missing or invalid data
                continue
            else:
                dates.append(current_date)
                temps.append(temp)

    return dates, temps

# Function to display the graph
def plot_temperatures(dates, temps, temp_type='high'):
    fig, ax = plt.subplots()

    # Choose color and title based on type
    if temp_type == 'high':
        ax.plot(dates, temps, c='red')
        title = "Daily High Temperatures - 2018"
        ylabel = "High Temp (F)"
    else:
        ax.plot(dates, temps, c='blue')
        title = "Daily Low Temperatures - 2018"
        ylabel = "Low Temp (F)"

    # Format the plot
    plt.title(title, fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel(ylabel, fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    # Show the graph
    plt.show()

# Display a simple menu with instructions
def display_menu():
    print("\nWeather Data Viewer")
    print("Choose an option:")
    print("1. View High Temperatures")
    print("2. View Low Temperatures")
    print("3. Exit")

# Main loop
while True:
    display_menu()
    choice = input("Enter your choice (1, 2, or 3): ").strip()

    if choice == '1':
        # Show high temperatures
        dates, highs = get_weather_data(temp_type='high')
        plot_temperatures(dates, highs, temp_type='high')
    elif choice == '2':
        # Show low temperatures
        dates, lows = get_weather_data(temp_type='low')
        plot_temperatures(dates, lows, temp_type='low')
    elif choice == '3':
        # Exit the program
        print("Exiting the Weather Data Viewer. Goodbye!")
        sys.exit()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
 