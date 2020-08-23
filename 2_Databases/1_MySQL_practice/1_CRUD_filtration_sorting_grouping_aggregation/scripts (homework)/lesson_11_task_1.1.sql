/* Создайте таблицу logs типа Archive. Пусть при каждом создании записи в таблицах users, catalogs и products в таблицу logs помещается время и дата создания записи, 
название таблицы, идентификатор первичного ключа и содержимое поля name.*/
use shop;

drop table if exists logs;
create table logs (
	id bigint(10) unsigned not null,
	created_datetime datetime not null default current_timestamp,
	table_name varchar(50) not null, -- not sure if it's more efficient to use 'char' data type here
	name varchar(50) not null
) comment = 'stores logs for operations with data in tables users, catalogs and products'
engine=archive;

delimiter //

drop trigger if exists write_users_event_to_log//
create trigger write_users_event_to_log after insert on users
 for each row
 begin
	insert into logs (id, table_name, name) -- created_datetime has a default value, so no need to add it to the trigger
	values (new.id, 'users', new.name);
 end//
 
drop trigger if exists write_catalogs_event_to_log//
create trigger write_catalogs_event_to_log after insert on catalogs
 for each row
 begin
	insert into logs (id, table_name, name) -- created_datetime has a default value, so no need to add it to the trigger
	values (new.id, 'catalogs', new.name);
 end//
 
drop trigger if exists write_products_event_to_log//
create trigger write_products_event_to_log after insert on products
 for each row
 begin
	insert into logs (id, table_name, name) -- created_datetime has a default value, so no need to add it to the trigger
	values (new.id, 'products', new.name);
 end//
 
delimiter ;

-- проверка для users

select id, name, birthday_at from users;
select * from logs;

insert into users (name, birthday_at)
values ('Test_trigger_users', now());

select id, name, birthday_at from users;
select * from logs;

-- проверка для catalogs

select id, name from catalogs;
select * from logs;

insert into catalogs (name)
values ('Test_trigger_catalogs');

select id, name from catalogs;
select * from logs;

-- проверка для products

select id, name, description, price, catalog_id from products;
select * from logs;

insert into products (name, description, price, catalog_id)
values ('Test_trigger_products', 'Test_description', 99999, 1);

select id, name from products;
select * from logs;

