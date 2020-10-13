-- выборка топ 3 артистов по количеству прослушанных треков этих артистов каждый день

select 
	a.id as artist_id,
	a.name as artist_name,
	sum(s.daily_plays_quantity) as total_daily_plays_quantity_for_this_artist
from 
	artists as a
join 
	songs as s on s.artist_id = a.id
group by 
	artist_id
order by 
	total_daily_plays_quantity_for_this_artist desc limit 3;







