import unittest
from restaurant import Restaurant

class RestaurantTestCase(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        super().__init__(methodName)
    def setUp(self):
        self.restaurant_name = "Arby's"
        self.cuisine_type = "American"
        self.number_served = 5
    def test_set_number_served(self):
        Restaurant.set_number_served()
        self.assertEqual(self.number_served, 10)
    def test_increment_number_served(self):
        Restaurant.increment_number_served()
        self.assertEqual(self.number_served, 10)
restaurant = RestaurantTestCase()
print("type 10.")
restaurant.test_set_number_served()
print("current number is 5, type 5.")
restaurant.test_increment_number_served()