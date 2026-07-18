import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city_name):

    api_key = os.getenv("WEATHER_API_KEY")

    if not api_key:
        print("Error: Openweather key is not found in env variables")
        return 
    
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q":city_name,
        "appid":api_key,
        "units":"metric"
    }
    try:
        response = requests.get(url, params=params ,timeout=5)

        response.raise_for_status()


        data = response.json()

        return  data

    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 401:
            print("Error: Invalid API Key. Please verify your .env configuration.")
        elif response.status_code == 404:
            print(f"Error: City '{city_name}' not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.RequestException as err:
        print(f"An unexpected error occurred: {err}")

