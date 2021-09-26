import pdb
from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()

country1 = Country("Austria", False)
country_repository.save(country1)
country2 = Country("Switzerland", False)
country_repository.save(country2)
country3 = Country("New Zealand", True)
country_repository.save(country3)
country4 = Country("South Africa", False)
country_repository.save(country4)
country5 = Country("The Netherlands", True)
country_repository.save(country5)
country_repository.select_all()

city1 = City("Vienna", country1, False)
city_repository.save(city1)
city2 = City("Bern", country2, False)
city_repository.save(city2)
city_repository.select_all()

country_repository.delete_all()


print(country_repository.select_all()[0].id)
print(city_repository.select_all()[0].id)

pdb.set_trace()