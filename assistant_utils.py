import requests
import os

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# Mock function to simulate retrieving latest movies
def get_latest_movies(title=None, month=None):
    base_url = "http://www.omdapi.com"

    # build parameters dictionary for the API call
    params = {
        "apikey": OMDB_API_KEY,
        "t": title,
        "y": year,
    }

    try:
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data["Response"] == "True":
                return data
            else:
                return f"No results found for {title} ({year})"
        else:
            return f"Error: {response.status_code}"
        
    except Exception as e:
        return f"Error: {e}"
    