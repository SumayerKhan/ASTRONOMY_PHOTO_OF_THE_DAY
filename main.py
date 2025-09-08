import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

response = requests.get(url)
data = response.json()
img_data = requests.get(data['url']).content
with open('image.jpg', 'wb') as im:
    im.write(img_data)