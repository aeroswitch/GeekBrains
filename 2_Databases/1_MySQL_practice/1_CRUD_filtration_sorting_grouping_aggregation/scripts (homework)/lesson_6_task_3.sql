/*  Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей. Предположим, что в таблицу likes_posts колонка likepage показывает id профиля, 
которая получила лайк */

-- посмотрим на наших 10 самых молодых пользователей 
select 
p.name,
p.lastname,
p.id,
p.birthday, 
timestampdiff(year, p.birthday, now()) as age
from likes_posts as lp
join profiles as p on p.id = lp.likepage 
where timestampdiff(year, p.birthday, now()) is not null
group by p.id 
order by age limit 10;

-- посчитаем сумму лайков постов 10 самых молодых пользователей 
select sum(count_of_posts_likes)
from (
	select count(lp.likepage) as count_of_posts_likes,
	timestampdiff(year, p.birthday, now()) as age
	from likes_posts as lp
	join profiles as p on p.id = lp.likepage
	where timestampdiff(year, p.birthday, now()) is not null
	group by p.id
	order by age limit 10
) as tbl_calculating_likes;