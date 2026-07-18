import argparse
from weather.formatter import display_weather
from weather.api import get_weather



def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--city")
    args =parser.parse_args()


    data = get_weather(args.city)

    if data:
        display_weather(data)

    


if __name__ == "__main__":
    main()
    