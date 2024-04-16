"""
Clone of weather app pulling from OpenWeather APIs
"""
import requests


def main():
    api_key = open("api_key.txt", "r").read()

    location = input("Location: ")

    result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=imperial&appid={api_key}')
    #print (result.json())

    temperature=result.json()['main']['temp']
    description = result.json()['weather'][0]['description']

    print(description)


#Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting up script")
    main()


