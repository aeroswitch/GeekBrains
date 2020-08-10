/* В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. Используйте транзакции.*/

use sample;

start transaction;

insert into sample.users (id, name)
	select id, name 
	from shop.users
	where shop.users.id = 1;

-- из задания непонятно требуется ли удалять перемещенного юзера из первой таблицы, поэтому при необходимости код можно убрать
delete from shop.users
	where shop.users.id = 1;

commit;

-- проверяем
select * from users;

use shop;
select * from users;