-- Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
USE shop;
UPDATE users SET created_at = NOW(), updated_at = NOW();

/* Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения
 в формате 20.10.2017 8:10. Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.*/

DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	birthday_at DATE,
	created_at VARCHAR(30),
	updated_at VARCHAR(30)
);

INSERT INTO users (name, birthday_at, created_at, updated_at) VALUES
  ('Геннадий', '1990-10-05', '20.10.2017 8:10', '20.10.2017 8:10'),
  ('Наталья', '1984-11-12', '24.03.2019 9:13', '24.03.2019 9:13'),
  ('Александр', '1985-05-20', '01.02.2020 21:14', '01.02.2020 21:14'),
  ('Сергей', '1988-02-14', '01.02.2020 21:14', '01.02.2020 21:14'),
  ('Иван', '1998-01-12', '01.02.2020 21:14', '01.02.2020 21:14'),
  ('Мария', '1992-08-29', '01.02.2020 21:14', '01.02.2020 21:14');
 
-- конвертируем VARHCHAR в DATETIME
UPDATE users SET created_at = STR_TO_DATE(created_at, '%d.%m.%Y %T'), updated_at = STR_TO_DATE(updated_at, '%d.%m.%Y %T');
-- изменяем тип данных столбцов created_at и updated_at в DATETIME
ALTER TABLE users CHANGE created_at created_at DATETIME, CHANGE updated_at updated_at DATETIME;


/* В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, 
если на складе имеются запасы. Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. 
Однако нулевые запасы должны выводиться в конце, после всех записей. */

INSERT INTO storehouses_products (storehouse_id, product_id, value) VALUES
  (1, 12, 0),
  (2, 2, 2500),
  (3, 5, 0),
  (3, 7, 300),
  (4, 2, 500),
  (4, 4, 1);
 
 SELECT * FROM storehouses_products ORDER BY IF(value = 0, 1, 0), value;

-- (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. Месяцы заданы в виде списка английских названий (may, august)
 
SELECT name, birthday_at FROM users WHERE DATE_FORMAT(birthday_at, '%M') IN ('May', 'August');

-- (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); Отсортируйте записи в порядке, заданном в списке IN.

SELECT * FROM catalogs WHERE id IN (5, 1, 2)  ORDER BY FIELD(id, 5, 1, 2);

-- Подсчитайте средний возраст пользователей в таблице users.

SELECT ROUND(AVG(TIMESTAMPDIFF(YEAR, birthday_at, NOW())), 0) AS average_age FROM users;

-- Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.

SELECT 
	DATE_FORMAT(CONCAT(YEAR(NOW()), '-', DATE_FORMAT(birthday_at, '%m-%d')), '%W') AS day_of_birthday_current_year,
	COUNT(*) as `count`
FROM 
	users
GROUP BY
	day_of_birthday_current_year;