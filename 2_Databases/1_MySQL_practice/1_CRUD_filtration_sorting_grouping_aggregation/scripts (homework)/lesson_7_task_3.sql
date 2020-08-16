/* (по желанию) Пусть имеется таблица рейсов flights (id, from, to) и таблица городов cities (label, name). 
 * Поля from, to и label содержат английские названия городов, поле name — русское. Выведите список рейсов flights с русскими названиями городов.*/

-- для начала создадим две таблицы (flights и cities) как указано в задании

create database flights_cities;
use flights_cities;

create table flights (
	id serial primary key,
	`from` varchar(255) comment 'Место отправления',
	`to` varchar(255) comment 'Место назначения'
);

create table cities (
	label varchar(255) comment 'Код города на латинице',
	name varchar(255) comment 'Название города на кириллице'
);

-- добавим данные в наши таблицы

insert into 
	flights (`from`, `to`)
values 
	('moscow', 'omsk'), 
	('novgorod', 'kazan'), 
	('irkutsk', 'moscow'), 
	('omsk', 'irkutsk'), 
	('moscow', 'kazan');
	
insert into 
	cities (label, name)
values 
	('moscow', 'Москва'), 
	('irkutsk', 'Иркутск'), 
	('novgorod', 'Новгород'), 
	('kazan', 'Казань'), 
	('omsk', 'Омск');

-- и последним шагом выполним само задание через двойной left join

select
	f.id,
	cities_from.name,
	cities_to.name
from
	flights as f
left join
	cities as cities_from 
on 
	f.`from` = cities_from.label
left join 
	cities as cities_to
on 
	f.`to` = cities_to.label;
	