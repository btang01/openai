import requests
import os

OMDB_API_KEY = os.getenv("OMDB_API_KEY")

# Mock function to simulate retrieving latest movies
def get_latest_movies(title=None, year=None):
    base_url = "http://www.omdbapi.com"

    # build parameters dictionary for the API call
    params = {
        "apikey": OMDB_API_KEY,
        "t": title,
        "y": year,
        "plot": "short"
    }

    try:
        # Make the API call to OMDb
        response = requests.get(base_url, params=params)
        if response.status_code == 200:
            data = response.json()
            if data["Response"] == "True":
                return data  # Return movie data if successful
            else:
                return f"No results found for '{title}' ({year})"
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Error: {e}"


def interact_with_movie_agent_assistant(assistant_id, title=None, year=None):
    """Interact with OMDb API and print movie details."""
    try:
        movie_data = get_latest_movies(Title, Year)
        if isinstance(movie_data, dict):
            print(f"\nTitle: {movie_data.get('Title')}")
            print(f"Year: {movie_data.get('Year')}")
            print(f"Director: {movie_data.get('Director')}")
            print(f"Plot: {movie_data.get('Plot')}\n")
        else:
            print(movie_data)
    except Exception as e:
        print(f"Error during interaction: {e}")


if __name__ == "__main__":
    # Test the OMDb API by asking for a movie title and optional year
    title = input("Enter the movie title: ").strip()
    year = input("Enter the movie year (optional): ").strip()

    # Call the API and print the result
    movie_data = get_latest_movies(title, year)
    
    # Print relevant movie information including the plot
    if isinstance(movie_data, dict):
        print(f"\nTitle: {movie_data.get('Title')}")
        print(f"Year: {movie_data.get('Year')}")
        print(f"Director: {movie_data.get('Director')}")
        print(f"Plot: {movie_data.get('Plot')}\n")
    else:
        print(movie_data)