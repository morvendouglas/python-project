import unittest
from models.city import City
from models.country import Country

class TestCountry(unittest.TestCase):
    
    def setUp(self):
        self.country = Country("France", False)

    def test_country_has_a_name(self):
        self.assertEqual("France", self.country.name)
       
    def test_country_has_a_mark_as_visited(self):
        self.assertEqual(False, self.country.visited)
    

