# 🌌 Astronomy Photo of the Day (APOD) — Streamlit App

A simple **Streamlit web application** that fetches NASA's Astronomy Picture of the Day (APOD) using the NASA API and displays it interactively with title, date, description, and media (image or video).

## ✨ Features

* Fetches the **Astronomy Picture of the Day** from NASA's API.
* Supports **choosing a specific date** (APOD archive goes back to 1995-06-16).
* Displays either an **image** or **video**, depending on the media type.
* Shows the **title, date, and explanation** of the APOD.
* Built with Streamlit for a simple web interface.

## 📦 Requirements

* Python 3.8+
* A NASA API key (free from [api.nasa.gov](https://api.nasa.gov))

**Python libraries:**
* `streamlit`
* `requests`
* `python-dotenv`

Install them using:

```bash
pip install -r requirements.txt
```

## ⚙️ Setup

1. **Clone this repository**

```bash
git clone https://github.com/your-username/ASTRONOMY_PHOTO_OF_THE_DAY.git
cd ASTRONOMY_PHOTO_OF_THE_DAY
```

2. **Create a virtual environment (optional but recommended)**

```bash
python -m venv .venv
# On Windows
.venv\Scripts\activate
# On macOS/Linux
source .venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up your API key**

Create a `.env` file in the project root with:

```env
API_KEY=your_nasa_api_key_here
```

## 🚀 Usage

Run the Streamlit app:

```bash
streamlit run main.py
```

Then open `http://localhost:8501` in your browser. Pick any date (after 1995-06-16) to view that day's APOD.

## 📂 Project Structure

```
ASTRONOMY_PHOTO_OF_THE_DAY/
│
├── main.py           # Streamlit app
├── requirements.txt  # Dependencies
├── .gitignore        # Ignore venv, .env, cache
└── README.md         # Project documentation
```

## 🔑 Getting a NASA API Key

1. Visit [api.nasa.gov](https://api.nasa.gov)
2. Click "Generate API Key"
3. Fill out the simple form
4. Copy your API key to the `.env` file


## 💫 Acknowledgments

* NASA for providing the amazing APOD API
* Streamlit for the easy-to-use web framework
