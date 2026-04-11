import requests as rq
import pandas as pd

url = "https://archive-api.open-meteo.com/v1/archive?latitude=33.57&longitude=-7.59&start_date=2015-01-01&end_date=2024-01-01&hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,windspeed_10m"

url2 = "https://archive-api.open-meteo.com/v1/archive?latitude=34.02&longitude=-6.83&start_date=2015-01-01&end_date=2024-01-01&hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,windspeed_10m"


#? Casa weather data
response = rq.get(url)
data = response.json()

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "humidity": data["hourly"]["relativehumidity_2m"],
    "precipitation": data["hourly"]["precipitation"],
    "cloudcover": data["hourly"]["cloudcover"],
    "windspeed": data["hourly"]["windspeed_10m"]
})

df.to_csv("casa_weather.csv", index=False)


#? Rabat weather data

response = rq.get(url2)

df = pd.DataFrame({
    "time": data["hourly"]["time"],
    "temperature": data["hourly"]["temperature_2m"],
    "humidity": data["hourly"]["relativehumidity_2m"],
    "precipitation": data["hourly"]["precipitation"],
    "cloudcover": data["hourly"]["cloudcover"],
    "windspeed": data["hourly"]["windspeed_10m"]
})

df.to_csv("rabat_weather.csv", index=False)




