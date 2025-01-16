import requests

API_KEY = 'your_openweathermap_api_key'  # Replace with your API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        response = requests.get(BASE_URL, params={
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        })
        response.raise_for_status()
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = data['main']['temp']
        print(f"The weather in {city} is {weather} with a temperature of {temperature}°C.")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")

if __name__ == "__main__":
    city = input("Enter the city name: ")
    get_weather(city)
