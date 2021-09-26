DROP TABLE IF EXISTS countries;
DROP TABLE IF EXISTS cities;

CREATE TABLE countries(
    id SERIAL PRIMARY KEY,
    country_name VARCHAR(255),
    visited BOOLEAN
);

CREATE TABLE cities(
    id SERIAL PRIMARY KEY,
    city_name VARCHAR(255),
    country_id INT REFERENCES countries(id),
    visited BOOLEAN
);

