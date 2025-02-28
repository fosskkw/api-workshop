import os
import random
import json
import requests
from dotenv import load_dotenv

# Load the environment variables from the .env file at the root of the project.
# .env files are not tracked inside git (you need to explicitly specify that inside
# the .gitignore of your project) and let us store secrets like API keys without
# exposing them. 
load_dotenv()

# API endpoint URLs for the services used in this application
OPEN_WEATHER_API = "https://api.openweathermap.org/data/2.5"
POKE_API = "https://pokeapi.co/api/v2"
GROQ_API = "https://api.groq.com/openai/v1"

# Dict of various weather conditions mapped to a Pokemon type.
TYPE_WEATHER_MAP = {
    "Thunderstorm": "Electric",
    "Drizzle": "Water",
    "Rain": "Water",
    "Snow": "Ice",
    "Mist": "Ghost",
    "Smoke": "Poison",
    "Haze": "Flying",
    "Dust": "Ground",
    "Fog": "Ghost",
    "Sand": "Ground",
    "Ash": "Rock",
    "Squall": "Flying",
    "Tornado": "Flying",
    "Clear": "Fire",
    "Clouds": "Normal",
}


def fetch_api_data(url, headers=None, json_data=None):
    """Generic function to fetch data from an API.
    
    Args:
        url (str): The API endpoint URL
        headers (dict, optional): HTTP headers to include in the request
        json_data (dict, optional): JSON data to send in POST requests
        
    Returns:
        dict or None: The JSON response data or None if the request failed
    """
    try:
        if json_data:
            response = requests.post(url, headers=headers, json=json_data)
        else:
            response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"API request failed: {e}")
        return None
    except json.JSONDecodeError:
        print("Invalid JSON response received.")
        return None


def get_weather(city):
    """Fetches and returns the current weather data of `city` from Open Weather API
    
    Args:
        city (str): Name of the city to get weather data for
        
    Returns:
        dict or None: Weather data for the specified city or None if request failed
    """
    url = f"{OPEN_WEATHER_API}/weather?appid={os.environ['OPEN_WEATHER_KEY']}&q={city}"
    return fetch_api_data(url)


def get_pokemon(pokemon_type):
    """Fetches and returns a random Pokemon of `type` from PokeAPI
    
    Args:
        pokemon_type (str): The type of Pokemon to fetch (e.g., "Water", "Fire")
        
    Returns:
        dict or None: Information about a random Pokemon of the specified type
                     or None if the request failed or no Pokemon of that type exists
    """
    url = f"{POKE_API}/type/{pokemon_type.lower()}"  # PokeAPI requires lowercase type names
    data = fetch_api_data(url)
    if data and data.get("pokemon"):
        # Select a random Pokemon from the list of Pokemon of the specified type
        pokemon_idx = random.randint(0, len(data["pokemon"]) - 1)
        return data["pokemon"][pokemon_idx]["pokemon"]
    return None


def get_description(city, weather, pokemon):
    """Returns a short description on why you should take the given `pokemon` with you in the given `city` in given `weather`
    
    Args:
        city (str): Name of the city
        weather (dict): Weather data from OpenWeather API
        pokemon (dict): Pokemon data from PokeAPI
        
    Returns:
        dict or None: Response from Groq API containing the generated description
                     or None if the request failed
    """
    
    url = f"{GROQ_API}/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['GROQ_KEY']}",
    }
    
    # System prompt that instructs the LLM how to format the response
    system_prompt = """
Write a short and fun paragraph on why the given pokemon would be the best choice to take to the given city with the given weather conditions. 
Keep it short and crisp.

Format should be: 
City: <name_of_city>
Weather: <description_of_weather>
Pokemon: <name_of_pokemon> (<type_of_pokemon>)

<your_paragraph>"""

    # The parameters `weather` and `pokemon` are of type `dict`. To send them to
    # the Groq API, we need to convert them into strings. The `json.dumps` method
    # converts any given Pythonic JSON object to string. 
    weather_str = json.dumps(weather)
    pokemon_str = json.dumps(pokemon)
    
    # The data that has to be sent to the Groq API
    json_data = {
        "model": "llama-3.1-8b-instant",  # Specifies which LLM to use, check out Groq's documentation for all the available models
        "messages": [
            {
                "role": "system", 
                "content": system_prompt
            },
            {
                "role": "user", 
                "content": f"city:{city},weather:{weather_str},pokemon={pokemon_str}",
            },
        ],
    }
    return fetch_api_data(url, headers, json_data)


def main():
    """Main function that orchestrates the program flow"""
    city = input("❓ Enter your city name: ")
    weather = get_weather(city)

    # Check if we successfully got weather data
    if not weather or "weather" not in weather or not weather["weather"]:
        print("Could not retrieve weather data.")
        return

    # Extract the main weather condition and map it to a Pokemon type
    weather_type = weather["weather"][0]["main"]
    pokemon_type = TYPE_WEATHER_MAP.get(weather_type)

    if not pokemon_type:
        print(f"No Pokemon type mapping for weather: {weather_type}")
        return

    # Get a random Pokemon of the mapped type
    pokemon = get_pokemon(pokemon_type)

    if not pokemon:
        print("Could not retrieve Pokemon data.")
        return

    # Generate a description of why this Pokemon is suitable for the current weather
    description_data = get_description(city, weather, pokemon)

    # Extract and print the generated description from the LLM response
    if description_data and "choices" in description_data and description_data["choices"]:
        print(description_data["choices"][0]["message"]["content"])
    else:
        print("Could not retrieve description.")

if __name__ == "__main__":
    main()
