import unittest
from unittest.mock import patch, Mock, mock_open
from weather_service import get_temperature, save_weather_report, WeatherService
import requests

class TestWeather(unittest.TestCase):
    def setUp(self):
        """Fixture : prépare les données avant chaque test"""
        self.sample_weather_data = {'main': {'temp': 25.5}}
        self.test_city = "Paris"

    @patch('weather_service.requests.get')
    def test_get_temperature_success(self, mock_get):
        """Test avec données de la fixture"""
        fake_response = Mock()
        fake_response.status_code = 200
        fake_response.json.return_value = self.sample_weather_data
        mock_get.return_value = fake_response
        result = get_temperature(self.test_city)
        self.assertEqual(result, 25.5)
        mock_get.assert_called_once_with(
            'http://api.openweathermap.org/data/2.5/weather',
            params={
                'q': self.test_city,
                'appid': '441f54eb9b8819b3a05d1674294bb055',
                'units': 'metric'
            }
        )

    @patch('weather_service.requests.get')
    def test_get_temperature_city_not_found(self, mock_get):
        """Test quand la ville n'existe pas"""
        fake_response = Mock()
        fake_response.status_code = 404
        mock_get.return_value = fake_response
        result = get_temperature("VilleInexistante")
        self.assertIsNone(result)
        mock_get.assert_called_once()

    @patch('weather_service.requests.get')
    def test_get_temperature_network_error(self, mock_get):
        """Test quand il y a une erreur réseau"""
        mock_get.side_effect = requests.exceptions.RequestException()
        # On attend que la fonction gère l'exception (à modifier dans weather_service.py)
        result = get_temperature("Paris")
        self.assertIsNone(result)

    @patch('weather_service.requests.get')
    def test_multiple_cities(self, mock_get):
        """Test plusieurs villes avec une seule méthode"""
        cities_and_temps = [
            ("Paris", 25.0),
            ("Londres", 18.5),
            ("Tokyo", 30.2)
        ]
        for city, expected_temp in cities_and_temps:
            fake_response = Mock()
            fake_response.status_code = 200
            fake_response.json.return_value = {'main': {'temp': expected_temp}}
            mock_get.return_value = fake_response
            with self.subTest(city=city):
                result = get_temperature(city)
                self.assertEqual(result, expected_temp)

class TestWeatherReport(unittest.TestCase):
    def setUp(self):
        self.city = "Paris"
        self.filename = "weather_log.json"

    @patch('weather_service.datetime')
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch.object(WeatherService, 'get_temperature')
    def test_save_weather_report_success(self, mock_get_temp, mock_file, mock_datetime):
        """Test sauvegarde rapport météo - EXERCICE PRINCIPAL"""
        mock_get_temp.return_value = 20.5
        mock_datetime.now.return_value.isoformat.return_value = "2024-01-01T12:00:00"
        result = save_weather_report(self.city, self.filename)
        self.assertTrue(result)
        mock_get_temp.assert_called_with(self.city)
        # Vérifie que le fichier a été ouvert en lecture puis en écriture
        mock_file.assert_any_call(self.filename, 'r')
        mock_file.assert_any_call(self.filename, 'w')

    @patch.object(WeatherService, 'get_temperature')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_weather_report_failure(self, mock_file, mock_get_temp):
        """Test sauvegarde échouée si get_temperature retourne None"""
        mock_get_temp.return_value = None
        result = save_weather_report("VilleInexistante", "weather_log.json")
        self.assertFalse(result)
        mock_get_temp.assert_called_with("VilleInexistante")
        mock_file.assert_not_called()

class TestWeatherService(unittest.TestCase):
    def setUp(self):
        self.service = WeatherService()
        self.city = "Paris"
        self.filename = "weather_log.json"

    @patch('weather_service.requests.get')
    def test_get_temperature_success(self, mock_get):
        fake_response = Mock()
        fake_response.status_code = 200
        fake_response.json.return_value = {'main': {'temp': 22.2}}
        mock_get.return_value = fake_response
        temp = self.service.get_temperature(self.city)
        self.assertEqual(temp, 22.2)

    @patch('weather_service.requests.get')
    def test_get_temperature_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException()
        temp = self.service.get_temperature(self.city)
        self.assertIsNone(temp)

    @patch('weather_service.datetime')
    @patch('builtins.open', new_callable=mock_open, read_data='[]')
    @patch.object(WeatherService, 'get_temperature')
    def test_save_weather_report_success(self, mock_get_temp, mock_file, mock_datetime):
        mock_get_temp.return_value = 19.5
        mock_datetime.now.return_value.isoformat.return_value = "2024-01-01T12:00:00"
        result = self.service.save_weather_report(self.city, self.filename)
        self.assertTrue(result)
        mock_get_temp.assert_called_with(self.city)
        mock_file.assert_any_call(self.filename, 'r')
        mock_file.assert_any_call(self.filename, 'w')

    @patch.object(WeatherService, 'get_temperature')
    @patch('builtins.open', new_callable=mock_open)
    def test_save_weather_report_failure(self, mock_file, mock_get_temp):
        mock_get_temp.return_value = None
        result = self.service.save_weather_report("VilleInexistante", self.filename)
        self.assertFalse(result)
        mock_get_temp.assert_called_with("VilleInexistante")
        mock_file.assert_not_called()

if __name__ == '__main__':
    unittest.main() 