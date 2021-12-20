from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import country_repository
from repositories import city_repository
from models.country import Country
from models.city import City
import pdb

travel_blueprint = Blueprint("travel", __name__)

# countries

# index pages
@travel_blueprint.route("/")
def countries():
    countries = country_repository.select_all()
    return render_template("/index.html", countries = countries)

# new country
@travel_blueprint.route("/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("/new.html", countries = countries)

# post to db
@travel_blueprint.route("/",  methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    visited = request.form['visited']
    country = Country (country_name, visited)
    country_repository.save(country)
    return redirect('/')

# show country
@travel_blueprint.route("/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('/show.html', country = country)

# edit country
@travel_blueprint.route("/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('/edit.html', country = country)

# update country
@travel_blueprint.route("/<id>", methods=['POST'])
def update_country(id):
    name = request.form['country_name']
    visited = request.form['visited']
    country = Country(name, visited, id)
    country_repository.update(country)
    return redirect('/')

# delete country
@travel_blueprint.route("/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/')

# _________________________________________________

# all cities to to one country

# index of cities
@travel_blueprint.route("/countries/<country_id>/cities")
def cities(country_id):
    country = country_repository.select(country_id)
    cities = country_repository.cities(country)
    # pdb.set_trace()
    return render_template("/cities/index.html", country = country, cities = cities)

# new city
@travel_blueprint.route("/countries/<country_id>/cities/new", methods=['GET'])
def new_city(country_id):
    country = country_repository.select(country_id)
    cities = country_repository.cities(country)
    return render_template("/cities/new.html", country = country, cities = cities)

# post to db
@travel_blueprint.route("/countries/<country_id>/cities",  methods=['POST'])
def create_city(country_id):
    city_name = request.form['city_name']
    country = country_repository.select(country_id)
    visited = request.form['visited']
    city = City(city_name, country, visited)
    city_repository.save(city)
    return redirect(f"/countries/{country_id}/cities")

 # show city
@travel_blueprint.route("/countries/<country_id>/cities/<id>", methods=['GET'])
def show_city(country_id, id):
    country = country_repository.select(country_id)
    city = city_repository.select(id)
    return render_template('/cities/show.html', city = city, country = country)

# edit city
@travel_blueprint.route("/countries/<country_id>/cities/<id>/edit", methods=['GET'])
def edit_city(country_id, id):
    country = country_repository.select(country_id)
    city = city_repository.select(id)
    return render_template('/cities/edit.html', city = city, country = country)

# update city
@travel_blueprint.route("/countries/<country_id>/cities/<id>", methods=['POST'])
def update_city(country_id, id):
    name = request.form['city_name']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, visited, id)
    city_repository.update(city)
    return redirect(f'/countries/{country_id}/cities')

# delete city
@travel_blueprint.route("/countries/<country_id>/cities/<id>/delete", methods=['POST'])
def delete_city(country_id, id):
    city_repository.delete(id)
    return redirect(f"/countries/{country_id}/cities")

































