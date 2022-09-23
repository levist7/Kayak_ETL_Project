import requests


url = "https://nominatim.openstreetmap.org/search?"
params = {
    'city': city 
    }

translation = requests.post(url, params=params)
translation.json()