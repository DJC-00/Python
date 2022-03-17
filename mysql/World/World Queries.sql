
SELECT countries.name, languages.language, languages.percentage
FROM countries 
JOIN languages ON countries.id = languages.country_id
WHERE (language = 'Slovene')
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(cities.country_id)
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name, cities.country_id
ORDER BY COUNT(cities.country_id) DESC;

SELECT cities.name AS "Cities in Mexico", FORMAT (cities.population, 'NO') AS "Population"
FROM cities
WHERE cities.population >= 500000 and cities.country_code = 'MEX';

SELECT countries.name, languages.language, languages.percentage
FROM countries 
JOIN languages ON countries.id = languages.country_id
WHERE (percentage > 89)
ORDER BY languages.percentage DESC;

SELECT countries.name, FORMAT (countries.population, 'NO') AS "Population", countries.surface_area
FROM countries
WHERE (population > 100000 and surface_area < 501)
ORDER BY population DESC;

SELECT countries.name, countries.government_form, countries.capital, countries.life_expectancy
FROM countries
WHERE (government_form = "Constitutional Monarchy" and capital > 200 and life_expectancy > 75)
ORDER BY countries.name;

SELECT countries.name AS "Country", cities.name AS "City", cities.district, FORMAT(cities.population, 'NO')
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE (countries.name = "Argentina" and cities.district = "Buenos Aires" and cities.population > 500000)
ORDER BY cities.name;

SELECT countries.region, COUNT(countries.region)  AS "Number of Countries"
FROM countries
GROUP BY countries.region , "Count"
ORDER BY COUNT(countries.region) desc;