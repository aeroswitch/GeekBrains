/* Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".*/

-- вариант  реализации через функцию

delimiter //

drop function if exists hello//
create function hello()
returns text deterministic
begin
	if (curtime() between '06:00:00' and '12:00:00') then
		return 'Доброе утро';
	elseif (curtime() between '12:00:00' and '18:00:00') then
		return 'Добрый день';
	elseif (curtime() between '18:00:00' and '00:00:00') then
		return 'Добрый вечер';
	else
		return 'Доброй ночи';
	end if;
end//

-- вариант  реализации через процедуру

drop procedure if exists hello//
create procedure hello()
begin
	if (curtime() between '06:00:00' and '12:00:00') then
		select 'Доброе утро';
	elseif (curtime() between '12:00:00' and '18:00:00') then
		select'Добрый день';
	elseif (curtime() between '18:00:00' and '00:00:00') then
		select 'Добрый вечер';
	else
		select 'Доброй ночи';
	end if;
end//


-- проверка

delimiter ;

select hello();
call hello();