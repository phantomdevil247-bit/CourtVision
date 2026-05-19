import requests

# Base URL and API key
BASE_URL = "https://api.balldontlie.io/v1/"
API_KEY = "e2ab2e47-842d-4410-ab13-9b137909cd20"

# Headers to send with every request
HEADERS = {
    "Authorization": API_KEY
}

def get_players():
    try:
        response = requests.get(f"{BASE_URL}players?per_page=100", headers=HEADERS)
        print(f"Status code: {response.status_code}")
        print(f"Response text: {response.text}")
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error fetching players : {e}")
        return []
    
def search_players(name):
    try:
        response = requests.get(f"{BASE_URL}players?search={name}&per_page=25", headers=HEADERS)
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

def get_player_games(player_id):
    try:
        response = requests.get(
            f"{BASE_URL}games",
            params={
                "seasons[]": 2024,
                "player_ids[]": player_id,
                "per_page": 5
            },
            headers=HEADERS
        )
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error fetching games: {e}")
        return []