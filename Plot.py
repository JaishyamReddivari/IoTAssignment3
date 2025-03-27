import pandas as pd
import matplotlib.pyplot as plt
import requests
from datetime import datetime, time

CHANNEL_ID = "2894243"
READ_API_KEY = "KGWKRBBT23VFYLZP"
FIELDS = {
    1: {"label": "Temperature (°C)", "color": "red"},
    2: {"label": "Humidity (%)", "color": "blue"},
    3: {"label": "CO₂ (ppm)", "color": "green"}
}

# Define today's 2 PM to 7 PM UTC window
today = datetime.utcnow().date()
start = pd.Timestamp(datetime.combine(today, time(14, 0)), tz='UTC')
end = pd.Timestamp(datetime.combine(today, time(19, 0)), tz='UTC')

# Set up plot
plt.figure(figsize=(12, 6))

# Fetch and plot each field
for field, meta in FIELDS.items():
    url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/fields/{field}.json"
    params = {
        "api_key": READ_API_KEY,
        "results": 1000
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data["feeds"])
    df["created_at"] = pd.to_datetime(df["created_at"], utc=True)
    df[meta["label"]] = pd.to_numeric(df[f"field{field}"], errors="coerce")
    df = df[(df["created_at"] >= start) & (df["created_at"] <= end)]

    plt.plot(df["created_at"], df[meta["label"]], label=meta["label"], color=meta["color"], marker='o')

# Final plot styling
plt.title("Environmental Data (2 PM – 7 PM UTC Today)")
plt.xlabel("Time")
plt.ylabel("Sensor Values")
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
