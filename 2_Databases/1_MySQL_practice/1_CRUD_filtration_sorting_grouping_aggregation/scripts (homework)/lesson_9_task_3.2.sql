/* В таблице products есть два текстовых поля: name с названием товара и description с его описанием. Допустимо присутствие обоих полей или одно из них. 
Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены.
 При попытке присвоить полям NULL-значение необходимо отменить операцию.*/
delimiter //
use shop//

drop trigger if exists products_null_blocker//

create trigger products_null_blocker before insert on products
for each row
begin
	if((new.name is null) and (new.description is null)) then
		signal sqlstate '45000' set message_text = 'NULL cannot be set for both name and description, operation cancelled';
	end if;
end// 

delimiter ;

select * from products;

-- проверяем, что вставка с одним NULL сработает
insert into products 
	(name, description, price, catalog_id)
values 
	("AMD Radeon RX 570", NULL, 8000, 12);

select * from products;

-- проверяем, что вставка с двумя NULL не сработает
insert into products 
	(name, description, price, catalog_id)
values 
	(NULL, NULL, 8500, 1);

select * from products;
