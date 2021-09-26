import unittest
from models.city import City
from models.country import Country

class TestCity(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("Italy", ["Rome", "Naples"], True)
        self.city1 = City("Rome", self.country, True)
        self.city2 = City("Naples", self.country, True)

    def test_city_has_a_name(self):
        self.assertEqual("Rome", self.city1.name)
        
    def test_city_has_country(self):
        self.assertEqual("Italy", self.city1.country.name)
       
    def test_city_has_a_mark_as_visited(self):
        self.assertEqual(True, self.city1.visited)
