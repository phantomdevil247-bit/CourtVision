import requests

# Base URL and API key
BASE_URL = "https://api.balldontlie.io/v1/"
API_KEY = "1de2bd8e-123a-4cfc-afe8-3e5aaed799de"

# Headers to send with every request
HEADERS = {
    "Authorization": API_KEY
}

def get_players():
    try:
        response = requests.get(f"{BASE_URL}/players?per_page=100", headers=HEADERS)
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error fetching players : {e}")
        return []
    
def search_players(name):
    try:
        response = requests.get(f"{BASE_URL}players?search={name}&per_page=25, headers=HEADERS")
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error searching players: {e}")
        return []
    
def get_standings():
    try:
        response = requests.get(f"{BASE_URL}/standings?season=2025",headers=HEADERS)
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error fetching standings: {e}")
        return []
    
    