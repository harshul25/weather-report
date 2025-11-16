import requests
import pandas as pd
from dagster import asset

@asset
def daily_weather():
    """Fetch today's weather from Open-Meteo and return a dataframe."""
    url = (
        "https://api.open-meteo.com/v1/forecast?"
        "latitude=43.45&longitude=-80.49&hourly=temperature_2m"
    )  

    response = requests.get(url)
    data = response.json()

    hours = data["hourly"]["time"]
    temps = data["hourly"]["temperature_2m"]

    df = pd.DataFrame({"time": hours, "temperature": temps})
    df.to_csv("weather_today.csv", index=False)

    return df
