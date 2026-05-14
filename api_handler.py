import requests

# Base URL and API key
BASE_URL = "https://api.balldontlie.io/v1/"
API_KEY = "b9f3d1bd-aca9-4b50-97f3-aa45ec432d52"

# Headers to send with every request
HEADERS = {
    "Authorization": "b9f3d1bd-aca9-4b50-97f3-aa45ec432d52"
}


def get_players():
    try:
        response = requests.get(f"{BASE_URL}/players?per_page=25, headers=HEADERS")
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error fetching players : {e}")
        return []
    
def get_standings():
    try:
        response = requests.get(f"{BASE_URL}/standings?season=2025,headers=HEADERS")
        data = response.json()
        return data['data']
    except Exception as e:
        print(f"Error fetching standings: {e}")
        return []
    
    