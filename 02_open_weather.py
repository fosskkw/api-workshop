import os
import requests 
from dotenv import load_dotenv  # For loading environment variables from .env file

# Load the environment variables from the .env file at the root of the project.
# .env files are not tracked inside git (you need to explicitly specify that inside
# the .gitignore of your project) and let us store secrets like API keys without
# exposing them.
load_dotenv()

OPEN_WEATHER_API = "https://api.openweathermap.org/data/2.5"

def get_weather(city):
    """
    Fetches current weather data for the specified city
    """
    api_key = os.environ['OPEN_WEATHER_KEY']
    endpoint = f"{OPEN_WEATHER_API}/weather?appid={api_key}&q={city}"
    response = requests.get(endpoint)
    return response.json()

# Get weather data for Nashik
weather = get_weather("nashik")

# Print the weather description
print(weather['weather'][0]['description'])
