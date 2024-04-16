"""
Clone of weather app pulling info from OpenWeather APIs
"""
import requests

def main():
    #pulls api key from text file for my OpenWeather account
    api_key = open("api_key.txt", "r").read()

    #input and while loop ensures F or C is entered for units (input validation) to pull for from API request, non case sensitive
    print('What units would you like the temperature in? Enter: F (fahrenheit) or C (celsius)?')
    units = ""
    units = input("").capitalize()

    while len(units) != 1 or (units != "F" and units != "C"):
        print('Lets try again...What units would you like the temperature in? Enter: F (fahrenheit) or C (celsius)?')
        units= input().upper()

    #ensures proper terminology is used when put into api request
    unitCodeConversion=""
    if units == "F":
        unitCodeConversion="imperial"
    else:
        unitCodeConversion= "metric"

    #api request to pull requested information into large JSON format
    while True:
        # input for location request and input validation
        location = input("Location: ")

        result = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={location}&units={unitCodeConversion}&appid={api_key}')

        if result.json()['cod']== '404':
            print("Invalid Location")
            continue
        break

    #print (result.json()) #shows format on how to extract data from .json format
    #location details
    lon=result.json()['coord']['lon']
    lat = result.json()['coord']['lat']

    #description details
    description = result.json()['weather'][0]['description']

    #general weather details
    temperature = result.json()['main']['temp']
    real_feel_temp= result.json()['main']['feels_like']
    humidity_level = result.json()['main']['humidity']

    #final output format below (easily modifiable)
    print(f'{location.capitalize()} located at {lon} longitude and {lat} latitude has temperatures of {temperature:.0f}{units} with a real feel temperature of {real_feel_temp:.0f}{units}')
    print(f'Presenting with {description} and humidity at {humidity_level}%')

if __name__ == '__main__':
    main()


