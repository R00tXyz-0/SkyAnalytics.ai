import requests
import pandas as pd

url_C = "https://archive-api.open-meteo.com/v1/archive?latitude=33.57&longitude=-7.59&start_date=2015-01-01&end_date=2024-01-01&hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,windspeed_10m"

url_R = "https://archive-api.open-meteo.com/v1/archive?latitude=34.02&longitude=-6.83&start_date=2015-01-01&end_date=2024-01-01&hourly=temperature_2m,relativehumidity_2m,precipitation,cloudcover,windspeed_10m"


response_C = requests.get(url_C)
data_C = response_C.json()

df_C = pd.DataFrame({
    "time": data_C["hourly"]["time"],
    "temperature": data_C["hourly"]["temperature_2m"],
    "humidity": data_C["hourly"]["relativehumidity_2m"],
    "precipitation": data_C["hourly"]["precipitation"],
    "cloudcover": data_C["hourly"]["cloudcover"],
    "windspeed": data_C["hourly"]["windspeed_10m"]
})

df_C.to_csv("casa_weather.csv", index=False)


response_R = requests.get(url_R)
data_R = response_R.json()

df_R = pd.DataFrame({
    "time": data_R["hourly"]["time"],
    "temperature": data_R["hourly"]["temperature_2m"],
    "humidity": data_R["hourly"]["relativehumidity_2m"],
    "precipitation": data_R["hourly"]["precipitation"],
    "cloudcover": data_R["hourly"]["cloudcover"],
    "windspeed": data_R["hourly"]["windspeed_10m"]
})

df_R.to_csv("rabat_weather.csv", index=False)
