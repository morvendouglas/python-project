from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import country_repository
from repositories import city_repository
from models.country import Country
from models.city import City

travel_blueprint = Blueprint("travel", __name__)

# where im going / travel bucket list

# index pages
@travel_blueprint.route("/where-im-going")
def countries():
    countries = country_repository.select_all()
    return render_template("where-im-going/index.html", countries = countries)

# new destination
@travel_blueprint.route("/where-im-going/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    return render_template("where-im-going/new.html", countries = countries)

# post to db
@travel_blueprint.route("/where-im-going",  methods=['POST'])
def create_country():
    country_name = request.form['country_name']
    visited = request.form['visited']
    country = Country (country_name, visited)
    country_repository.save(country)
    return redirect('/where-im-going')

# show
@travel_blueprint.route("/where-im-going/<id>", methods=['GET'])
def show_country(id):
    country = country_repository.select(id)
    return render_template('where-im-going/show.html', country = country)

# edit 
@travel_blueprint.route("/where-im-going/<id>/edit", methods=['GET'])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('where-im-going/edit.html', country = country)

# update 
@travel_blueprint.route("/where-im-going/<id>", methods=['POST'])
def update_country(id):
    name = request.form['country_name']
    visited = request.form['visited']
    country = Country(name, visited, id)
    country_repository.update(country)
    return redirect('/where-im-going')

# delete
@travel_blueprint.route("/where-im-going/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/where-im-going')



# _________________________________________________

# trying to all cities attached to one country vvvv (these aren't right)

@travel_blueprint.route("/where-im-going/<country>/cities")
def cities(country):
    # something so use the country.name
    cities = country_repository.cities(country)
    return render_template("where-im-going/cities/index.html", country = country, cities = cities)

    


























# where ive been / memories (maybe seperate memory class if there is time)

# index pages
# @travel_blueprint.route("/where-ive-been")
# def memories():
#     return render_template("where-ive-been/index.html")

