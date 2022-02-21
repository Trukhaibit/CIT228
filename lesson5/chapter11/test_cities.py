import unittest
from city_functions import cityName

class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self, city, country):
        city_name = cityName(city,country)
        self.assertEqual(city_name, "Santiago, Chile")
    def test_city_country_population(self, city, country, population):
        city_name = cityName(city,country,population)
        self.assertEqual(city_name, "Santiago, Chile - Population 5000000")
santiagoChile= CityCountryTestCase()
santiagoChile.test_city_country("santiago","chile",)
santiagoChile.test_city_country_population("santiago","chile","")
santiagoChile.test_city_country_population("santiago","chile","5000000")