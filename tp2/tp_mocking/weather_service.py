import requests
import json
from datetime import datetime

class WeatherService:
    def __init__(self, api_key='441f54eb9b8819b3a05d1674294bb055'):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_temperature(self, city):
        """Récupère la température d'une ville via une API"""
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        try:
            response = requests.get(self.base_url, params=params)
            if response.status_code == 200:
                data = response.json()
                return data['main']['temp']
            else:
                return None
        except requests.exceptions.RequestException:
            return None

    def save_weather_report(self, city, filename="weather_log.json"):
        """Récupère la météo et la sauvegarde dans un fichier"""
        # 1. Récupérer la température
        temp = self.get_temperature(city)
        if temp is None:
            return False
        # 2. Créer le rapport
        report = {
            'city': city,
            'temperature': temp,
            'timestamp': datetime.now().isoformat()
        }
        # 3. Sauvegarder dans le fichier
        try:
            # Lire le fichier existant
            with open(filename, 'r') as f:
                reports = json.load(f)
        except FileNotFoundError:
            reports = []
        reports.append(report)
        with open(filename, 'w') as f:
            json.dump(reports, f)
        return True

def get_temperature(city):
    service = WeatherService()
    return service.get_temperature(city)

def save_weather_report(city, filename="weather_log.json"):
    service = WeatherService()
    return service.save_weather_report(city, filename) 