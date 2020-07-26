-- (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. Месяцы заданы в виде списка английских названий (may, august)
 
SELECT name, birthday_at FROM users WHERE DATE_FORMAT(birthday_at, '%M') IN ('May', 'August');