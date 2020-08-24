--  список всех оплаченных подписок с деталями о пользователе и подписке

create or replace view 
	paid_subscriptions_with_user_details
as select
	u.id,
	u.username,
	u.email as user_email,
	u.country as user_country,
	usoh.purchase_date as subscription_purchase_date,
	st.`type` as subscription_type,
	st.price as subscription_price	
from
	subscription_type as st
join
	users_subscriptions_orders_history as usoh on st.id = usoh.subscription_id 
join 
	users as u on usoh.user_id = u.id
where 
	st.price > 0 and usoh.status = 'paid'
order by
	usoh.purchase_date;

-- проверим

select * from paid_subscriptions_with_user_details; 
