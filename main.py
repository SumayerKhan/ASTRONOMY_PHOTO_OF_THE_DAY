import requests
import os
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

# NASA API
api_key = os.getenv("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"

# DATA FETCH
response = requests.get(url)
data = response.json()

#STREAMLIT UI
st.title("Astronomy photo of the day!")
st.header(data['title'])
st.write(data['date'])

#PHOTO FETCH
img_url = data['url']

if data['media_type'] == 'image':
    st.image(image=img_url,caption=data['title'])
else:
    st.video(data=img_url)

# Description
st.markdown("### Description")
st.write(data['explanation'])