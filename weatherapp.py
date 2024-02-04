import requests
import json
def get_weather(location):
    api_key = "564d5e65a7059ebdd106d7fc8b750827"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    complete_url = base_url + "?q=" + location + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        wind = data["wind"]
        weather_desc = data["weather"][0]

        print("Location: ", data["name"])
        print("Temperature: ", main["temp"], "K")
        print("Humidity: ", main["humidity"], "%")
        print("Weather Description: ", weather_desc["description"])
        print("Wind Speed: ", wind["speed"], "m/s")
    else:
        print("Location not found. Please try again.")

def main():
    location = input("Enter location (city or ZIP code): ")
    get_weather(location)

if __name__ == "__main__":
    main()