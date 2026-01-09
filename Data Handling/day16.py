"""
Sample data:
Date, City, Temperature, Condition
2025-06-11, Delhi, 36.5, Clear
2025-06-12, Delhi, 37.8, Sunny
2025-06-13, Delhi, 38.0, Sunny
2025-06-14, Delhi, 34.2, Rain
2025-06-15, Delhi, 35.0, Clouds
2025-06-16, Delhi, 33.4, Rain
2025-06-17, Delhi, 34.7, Clear

Plot graphs from this data


"""

import csv
from collections import defaultdict
import matplotlib.pyplot as plt

FILENAME = "weather_log.csv"


def visualize_weather():
    dates = []
    temps = []
    conditions = defaultdict(int)

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                temp = float(
                    row.get("Temperature")
                    or row.get("Temperature (°C)")
                )

                dates.append(row["Date"])
                temps.append(temp)
                conditions[row["Condition"]] += 1

            except (ValueError, KeyError, TypeError):
                continue

    if not dates or not temps:
        print("No valid temperature data available.")
        return

    # 📈 Temperature over time
    plt.figure(figsize=(10, 7))
    plt.plot(dates, temps, marker='o')
    plt.title("Temperature Over Time")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # 📊 Weather condition frequency
    plt.figure(figsize=(7, 5))
    plt.bar(conditions.keys(), conditions.values())
    plt.xlabel("Condition")
    plt.ylabel("Days")
    plt.title("Weather Conditions Frequency")
    plt.tight_layout()
    plt.show()


visualize_weather()

