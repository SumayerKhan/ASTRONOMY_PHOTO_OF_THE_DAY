import requests
import os
from dotenv import load_dotenv

load_dotenv()

# NASA API
api_key = os.getenv("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# DATA FETCH
response = requests.get(url)
data = response.json()
