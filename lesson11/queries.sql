queries.sql

SELECT * FROM films ORDER BY imdb DESC;

SELECT * FROM films ORDER BY imdb ASC;

SELECT film_name FROM films ORDER BY film_name DESC LIMIT 3;

SELECT DISTINCT film_name, release_year FROM films ORDER BY release_year;

SELECT * FROM films ORDER BY imdb DESC;

SELECT * FROM films ORDER BY imdb ASC;

SELECT film_name FROM films ORDER BY film_name DESC LIMIT 3;

SELECT * FROM films WHERE imdb >= 7.5 ORDER BY imdb DESC;

SELECT * FROM directors WHERE film_amount BETWEEN 4 AND 12;

SELECT DISTINCT film_name, release_year FROM films ORDER BY release_year;

SELECT film_name, films.director_lname, films.director_fname FROM films INNER JOIN directors ON (directors.director_id = films.director_id);

SELECT actor_fname, actor_lname, actors.birth_date FROM actors LEFT JOIN directors ON (actors.actor_id = directors.actor_id);

SELECT actor_fname, actor_lname, actors.birth_date FROM actors RIGHT JOIN directors ON (actors.actor_id = directors.actor_id);

SELECT directors.director_fname || ' ' || directors.director_lname, film_amount FROM directors WHERE EXTRACT (YEAR FROM birth_date) > 1970 ORDER BY director_lname; 

SELECT director_fname, director_lname, film_amount,
CASE WHEN film_amount < 5 THEN 'Unsatisfying performance'
WHEN film_amount < 8 THEN 'Excellent performance' 
ELSE 'Unbelievable performance'
END AS criteria
FROM directors
ORDER BY film_amount;

SELECT film_name, films.director_lname
FROM films
FULL JOIN directors ON (films.director_id = directors.director_id);

SELECT a.actor_lname, a.actor_fname, f.film_name, f.director_lname, f.director_fname
FROM actors AS a
JOIN films AS f
ON a.actor_id = f.actor_id
WHERE a.actor_id > 2
ORDER BY f.release_year;

SELECT af.act_id, a.actor_fname, a.actor_lname, f.film_name, f.release_year 
FROM actors_to_films AS af
JOIN actors AS a
ON af.act_id = a.actor_id
JOIN films as f
ON af.film_id = f.film_id 
ORDER BY af.act_id;
