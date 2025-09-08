import requests
import os
from dotenv import load_dotenv
import streamlit as st
from datetime import date

load_dotenv()

# NASA API
api_key = os.getenv("API_KEY")

#STREAMLIT UI
st.title("Astronomy photo of the day!")
chosen_date = st.date_input("Pick a date", value=date.today(), min_value=date(1995, 6, 16), max_value=date.today())

# DATA FETCH
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&date={chosen_date}"
response = requests.get(url)
data = response.json()

# Title and date
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