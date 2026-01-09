"""
Challenge: Real-Time Weather Logger (API + CSV)

Build a python CLI tool that fetches real-time weather data for a given city and logs it to a CSV file for daily tracking

Your program should:
1. Ask the user for a city name.
2. Fetch weather data using the OpenWeatherMap API
3. Store the following in a CSV file ('weather_log.csv'):
    - Date (auto-filled as today's date)
    - City
    - Temperature (in °C)
    - Weather condition (e.g., Clear, Rain)
4. Present duplicate entries for the same city on the same day.
5. Allow users to:
    - Add new weather log
    - View all logs
    - Show average, highest, lowest temperatures, and most frequent condition

Bonus:
- Format the output like a table
-  Handle API failures and invalid city names gracefully
"""

import os
import csv
from datetime import datetime
import requests
from collections import Counter

FILENAME = "weather_log.csv"
API_KEY = "GET THE KEY"

# Create CSV file if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Date", "City", "Temperature (°C)", "Condition"])


def log_weather():
    city = input("Enter your city name: ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    date = datetime.now().strftime("%Y-%m-%d")

    # Check for duplicate entry
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Date"] == date and row["City"].lower() == city.lower():
                print("Weather entry for this city already exists today.")
                return

    try:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )
        response = requests.get(url, timeout=10)
        data = response.json()

        if response.status_code != 200:
            print(f"API Error: {data.get('message', 'Unknown error')}")
            return

        temp = data["main"]["temp"]
        condition = data["weather"][0]["main"]

        with open(FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([date, city.title(), temp, condition])

        print(f"Logged: {temp}°C, {condition} in {city.title()} on {date}")

    except requests.exceptions.RequestException:
        print("Network error. Please try again later.")
    except KeyError:
        print("Unexpected API response.")


def view_logs():
    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = list(csv.reader(f))

        if len(reader) <= 1:
            print("No entries found.")
            return

        print("\nDate       | City        | Temp (°C) | Condition")
        print("-" * 50)

        for row in reader[1:]:
            print(f"{row[0]:<10} | {row[1]:<11} | {row[2]:<9} | {row[3]}")


def show_stats():
    temps = []
    conditions = []

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            try:
                temps.append(float(row["Temperature"]))
                conditions.append(row["Condition"])
            except ValueError:
                continue

    if not temps:
        print("No data available for statistics.")
        return

    print("\nWeather Statistics:")
    print(f"Average Temperature: {sum(temps) / len(temps):.2f} °C")
    print(f"Highest Temperature: {max(temps)} °C")
    print(f"Lowest Temperature: {min(temps)} °C")
    print(f"Most Frequent Condition: {Counter(conditions).most_common(1)[0][0]}")



def main():
    while True:
        print("\nReal-Time Weather Logger")
        print("1. Add Weather Log")
        print("2. View Logs")
        print("3. View Statistics")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        match choice:
            case "1":
                log_weather()
            case "2":
                view_logs()
            case "3":
                show_stats()
            case "4":
                print("Goodbye 👋")
                break
            case _:
                print("Invalid choice.")


if __name__ == "__main__":
    main()
