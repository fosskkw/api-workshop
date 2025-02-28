import requests

# Define the base URL for the PokeAPI
POKE_API = "https://pokeapi.co/api/v2"

# Construct the endpoint URL to get data about Pikachu
endpoint = f"{POKE_API}/pokemon/pikachu"

# Send a GET request to the API
response = requests.get(endpoint)

# Print the response data
print(response.text)

# You can get the response JSON as a Python object using `json()` of `response`
# json_dict = response.json()
