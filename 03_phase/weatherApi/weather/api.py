import os
import requests
from dotenv import load_dotenv

load_dotenv()

def get_weather(city_name):

    api_key = os.getenv("WEATHER_API_KEY")
    
