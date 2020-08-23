-- (по желанию) Создайте SQL-запрос, который помещает в таблицу users миллион записей.

-- обозначим количество юзеров, которых нужно добавить, в качестве аргумента процедуры

drop procedure if exists insert_n_users;
delimiter //
create procedure insert_n_users (quantity int)
 begin
	 declare x int default 1;
	 while quantity > 0 do
		 insert into users(name, birthday_at) values (concat('user_', x), now());
		 set x = x + 1;
		 SET quantity = quantity - 1;
	 end while;
 end //
delimiter ;


-- проверка
select * from users;

call insert_n_users(10000); -- 10000 записей добавляются 20+ секунд, при желании аргумент можно изменить на 1 000 000

select * from users limit 1000;

-- truncate users;