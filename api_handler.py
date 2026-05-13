import requests

BASE_URL = "https://api.balldontlie.io/v1/"

def get_players():
    try:
        response = requests.get(f"{BASE_URL}/players?per_page=25")
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error fetching players : {e}")
        return []
    
def get_standings():
    try:
        response = requests.get(f"{BASE_URL}/standings?season=2025")
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error fetching standings: {e}")
        return []
    
    