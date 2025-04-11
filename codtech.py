import requests
import matplotlib.pyplot as plt
import seaborn as sns

# ---- API Setup ----
API_KEY = "815694f311be20313e0c8d3b62929071"
CITY = "Hyderabad"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

# ---- Fetch Data ----
response = requests.get(URL)
data = response.json()
print(data)

# ---- Extract Temp and Time ----
dates = []
temps = []

for entry in data['list']:
    dates.append(entry['dt_txt'])            # Time
    temps.append(entry['main']['temp'])      # Temp in °C

# ---- Plot using Seaborn ----
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, marker='o', color='green')
plt.title(f"5-Day Weather Forecast for {CITY}", fontsize=14)
plt.xlabel("Date & Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.savefig("weather_dashboard.png")   # Save image
plt.show()
