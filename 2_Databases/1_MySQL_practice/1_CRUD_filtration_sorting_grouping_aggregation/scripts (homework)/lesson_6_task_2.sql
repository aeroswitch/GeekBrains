-- Пусть задан некоторый пользователь. Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем.

select count(messages.id) as count_of_messages,
from_profile_id as id_of_friend,
p2.name as friend_name,
p2.lastname as friend_lastname
from messages
join profiles as p2 on p2.id = messages.from_profile_id 
where to_profile_id = 1 and from_profile_id in (select initiator_profile_id from friend_requests where target_profile_id = 1 and status = 'approved')
group by from_profile_id
order by count_of_messages desc limit 1;