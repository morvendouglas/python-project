from models.city import City
from models.country import Country
import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()

country1 = Country("Austria", False)
country_repository.save(country1)
country_repository.select_all()


city1 = City("Vienna", country1, False)
city_repository.save(city1)
city_repository.select_all()

