-- Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.

-- Т.к. таблица orders и orders_product в базе shop пустые, добавим несколько значений в эти таблицы
use shop;

insert into orders (user_id) values (2), (4), (6);

insert into 
	orders_products (order_id, product_id, total)
values 
	(1, 2, 1), 
	(2, 4, 2), 
	(3, 3, 1);
	

-- Выполним задание через join нескольких таблиц чтобы посмотреть детали каждого заказа 

select 
	u.id as user_id, 
	u.name, 
	o.id as order_id, 
	op.product_id, 
	op.total as quantity,
	p.name as product_name,
	p.description as product_description
from 
	users as u 
join 
	orders as o 
on 
	u.id = o.user_id
join 
	orders_products as op 
on 
	o.id = op.order_id
join 
	products as p 
on 
	op.product_id = p.id;

-- вариант от geekbrains

select 
	id, name, birthday_at
from 
	users
where
	id in (select distinct user_id from orders);
	