from .api import get_weather

def display_weather(response):
    if response is None:
        return

    name = response["name"]
    temperature = response["main"]["temp"]
    humidity = response["main"]["humidity"]
    feels_like = response["main"]["feels_like"]
    condition = response['weather'][0]["description"]
    wind_speed =response["wind"]["speed"]


    print("="*50)

    print("Weather Report ")

    print("="*50)

    print(f"{'📍 City':<18}: {name}")
    print(f"{'🌡 Temperature':<18}: {temperature}°C")
    print(f"{'🤗 Feels Like':<18}: {feels_like}°C")
    print(f"{'💧 Humidity':<18}: {humidity}%")
    print(f"{'☁ Condition':<18}: {condition.title()}")
    print(f"{'🌬 Wind Speed':<18}: {wind_speed} m/s")

    
