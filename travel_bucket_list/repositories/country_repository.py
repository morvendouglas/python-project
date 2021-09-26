from db.run_sql import run_sql
from models.city import City
from models.country import Country
import repositories.city_repository as city_repository

def save(country):
    sql = "INSERT INTO countries (country_name, visited) VALUES (%s, %s) RETURNING *"
    values = [country.name, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country

def select_all():
    countries = []
    sql = "SELECT * FROM countries"
    results = run_sql(sql)
    for item in results:
        country = Country(item['country_name'], item['visited'], item['id'])
        countries.append(country)
    return countries

def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        country = Country(result['country_name'], result['visited'], result['id'])
    return country

def delete_all():
    sql = "DELETE FROM countries"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(country):
    sql = "UPDATE countries SET (country_name, visited) = (%s, %s) WHERE id = %s"
    values = [country.name, country.visited, country.id]
    run_sql(sql, values)

def cities(country):
    cities = []
    sql = "SELECT * FROM cities WHERE country_id = %s"
    values = [country.id]
    results = run_sql(sql, values)
    for item in results:
        city = City(item['city_name'], item['country_id'], item['visited'], item['id'])
        cities.append(city)
    return cities