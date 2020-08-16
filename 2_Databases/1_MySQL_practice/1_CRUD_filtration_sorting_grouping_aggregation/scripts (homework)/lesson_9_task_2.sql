-- Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.
use shop;

create or replace view name_plus_catalog as (
	select products.name as product_name, catalogs.name as catalog_name from products
	join
		catalogs 
	on 
		products.catalog_id = catalogs.id
);

select * from name_plus_catalog;