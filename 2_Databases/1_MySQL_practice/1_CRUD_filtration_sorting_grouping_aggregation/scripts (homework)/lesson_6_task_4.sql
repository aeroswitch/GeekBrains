/* Определить кто больше поставил лайков (всего) - мужчины или женщины? 

определять id пользователя который поставил лайк будем по колонке profile_id в таблице likes_posts. */

select count(profile_id) as count_of_likes, p.gender
from likes_posts as lp
join profiles as p on p.id = lp.likepage 
group by gender
order by count_of_likes desc;
-- Как мы видим, больше лайков ставили женщины