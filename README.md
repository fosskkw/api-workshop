# A Practical Guide to APIs

This repository contains the materials and code for the workshop "A Practical Guide to APIs" conducted at KKWIEER, Nashik on February 28, 2025, as part of the Tech Horizon event.

## Workshop Overview

This workshop demonstrates practical API usage by building a fun Python application that recommends the perfect Pokemon to take with you based on the current weather conditions in your city. The app combines data from three different APIs to create a personalized Pokemon recommendation with a creative explanation.

## APIs Used

1. **OpenWeather API** - Retrieves current weather conditions for a specified city
2. **PokeAPI** - Fetches Pokemon data based on weather-appropriate types
3. **Groq API** - Uses LLM (Large Language Model) to generate creative descriptions

## Prerequisites

- Python 3.8 or higher
- API keys for:
  - [OpenWeather API](https://openweathermap.org/api) (free tier available)
  - [Groq API](https://console.groq.com/keys) (requires registration)
- Internet connection to access the APIs

## Setup Instructions

### Option 1: Using `uv` (Recommended)

[`uv`](https://github.com/astral-sh/uv) is a fast Python package installer and resolver.

1. [Install `uv`](https://docs.astral.sh/uv/getting-started/installation/)

2. Clone the repository:
   ```bash
   git clone https://github.com/fosskkw/api-workshop.git
   cd api-workshop
   ```

3. Create a virtual environment and install dependencies:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   uv sync
   ```

### Option 2: Using Standard venv and pip

1. Clone the repository:
   ```bash
   git clone https://github.com/fosskkw/api-workshop.git
   cd api-workshop
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the root directory with your API keys:
   ```
   OPEN_WEATHER_KEY=your_openweather_api_key
   GROQ_KEY=your_groq_api_key
   ```

## Tutorial Progression

The workshop follows a step-by-step approach to building the final application:

1. **01_pokeapi.py** - Introduces making API requests with the free, no-auth PokeAPI
   ```bash
   uv python 01_pokeapi.py
   # OR
   python 01_pokeapi.py
   ```

2. **02_open_weather.py** - Demonstrates API key authentication with OpenWeather API
   ```bash
   uv python 02_open_weather.py
   # OR
   python 02_open_weather.py
   ```

3. **03_groq_api.py** - Shows how to work with a more complex API (Groq LLM)
   ```bash
   uv python 03_groq_api.py
   # OR
   python 03_groq_api.py
   ```

4. **04_main.py** - Combines all three APIs into a cohesive application
   ```bash
   uv python 04_main.py
   # OR
   python 04_main.py
   ```

## Main Application

Run the main application:
```bash
uv python 04_main.py
# OR
python 04_main.py
```

When prompted, enter the name of a city to receive a weather-appropriate Pokemon recommendation with a creative description of why that Pokemon is perfect for your current conditions.

## How It Works

1. The application takes a city name as input
2. It fetches the current weather conditions using the OpenWeather API
3. Based on the weather condition, it maps to an appropriate Pokemon type
4. It randomly selects a Pokemon of that type using the PokeAPI
5. It uses Groq's LLM API to generate a creative description explaining why this Pokemon is perfect for your journey

## Example Output

```
❓ Enter your city name: Nashik

City: Nashik
Weather: Clear
Pokemon: Charizard (Fire)

When exploring Nashik under clear skies, Charizard is your ideal companion! As the sun beams down on this historic city, Charizard's fire abilities are at their peak strength. The clear weather enhances this Fire-type's natural powers, perfect for soaring above Nashik's famous vineyards and temples. While you visit Panchavati or trek through the nearby Western Ghats, Charizard's powerful wings provide convenient transportation and its flame offers warmth during cool evenings after hot days. In Nashik's clear weather, there's simply no better Pokemon partner than the majestic Charizard!
```

## Workshop Materials

If you attended the "A Practical Guide to APIs" workshop at KKWIEER on February 28, 2025, you can use this repository to revisit the concepts covered and continue experimenting with the code.

## Additional Resources

- [OpenWeather API Documentation](https://openweathermap.org/api)
- [PokeAPI Documentation](https://pokeapi.co/docs/v2)
- [Groq API Documentation](https://console.groq.com/docs/quickstart)
- [Python Requests Library Documentation](https://requests.readthedocs.io/)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
