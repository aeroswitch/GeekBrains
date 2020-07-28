-- Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.

SELECT 
	DATE_FORMAT(CONCAT(YEAR(NOW()), '-', DATE_FORMAT(birthday_at, '%m-%d')), '%W') AS day_of_birthday_current_year,
	COUNT(*) as `count`
FROM 
	users
GROUP BY
	day_of_birthday_current_year;
