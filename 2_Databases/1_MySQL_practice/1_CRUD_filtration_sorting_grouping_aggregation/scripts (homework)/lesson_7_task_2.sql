-- Выведите список товаров products и разделов catalogs, который соответствует товару.

select 
	p.name as product_name,
	p.description,
	p.price,
	c.name as category_name
from 
	products as p
left join
	catalogs as c 
on 
	p.catalog_id = c.id;


	
