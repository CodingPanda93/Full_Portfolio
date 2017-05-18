1.
USE sakila;
SELECT customer.first_name, customer.last_name, customer.email, address.address, city.city FROM city
LEFT JOIN address ON city.city_id = address.city_id
LEFT JOIN customer ON address.address_id = customer.address_id
WHERE city.city_id = 312;
2.
USE sakila;
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name FROM category
LEFT JOIN film_category ON film_category.category_id = category.category_id
LEFT JOIN film ON film.film_id = film_category.film_id
WHERE category.name = 'Comedy'
ORDER BY title;
3.
USE sakila;
SELECT actor.first_name, actor.last_name, film.title AS film_title, film.description, film.release_year FROM actor
JOIN film_actor ON actor.actor_id = film_actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5
ORDER BY film.title;
4.
USE sakila;
SELECT customer.first_name, customer.last_name, customer.email, address.address, address.address2, city.city FROM store
JOIN customer ON store.store_id = customer.store_id
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE store.store_id = 1 AND city.city_id = IN (1, 42, 312, 459)
ORDER BY customer.first_name;
5.
USE sakila;
SELECT film.title, film.release_year, film.rating, film.special_features FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE actor.actor_id = 15 AND rating = 'G' AND film.special_features LIKE '%Behind the Scenes%'
ORDER BY film.title;
6.
USE sakila;
SELECT film.film_id, film.title, actor.actor_id, CONCAT(actor.first_name, ' ', actor.last_name) FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film.film_id = film_actor.film_id
WHERE film.film_id = 369;
7.
USE sakila;
SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name FROM category
JOIN film_category ON film_category.category_id = category.category_id
JOIN film ON film.film_id = film_category.film_id
WHERE category.name = 'Drama' AND film.rental_rate = 2.99
ORDER BY film.title;
8.
USE sakila;
SELECT film.title, film.description, film.release_year, film.rating, film.special_features , category.name, CONCAT_WS(' ', actor.first_name, actor.last_name) as actor_name FROM film
JOIN film_actor ON film.film_id = film_actor.film_id
JOIN actor ON film_actor.actor_id = actor.actor_id
JOIN film_category on film.film_id = film_category.film_id
JOIN category on film_category.category_id = category.category_id
WHERE category.name = 'Action' AND actor.first_name = 'SANDRA' and actor.last_name = 'KILMER'
ORDER BY film.title;
