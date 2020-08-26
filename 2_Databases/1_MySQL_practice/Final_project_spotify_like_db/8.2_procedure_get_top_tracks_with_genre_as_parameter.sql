-- процедура для поиска самых попурярных треков в указанном пользователем жанре
use spotify; 

delimiter //
drop procedure if exists get_top_songs //

create procedure get_top_songs(in value varchar(30))
 begin
	select
		s.daily_plays_quantity as song_daily_play_quantity,
		a.name as artist_name,
		s.title as song_title,
		s.genre as song_genre,
		s.duration as song_duration	
	from 
		songs as s	
	join 
		artists as a on s.artist_id = a.id
	where 
		s.genre = value
	order by 
		s.daily_plays_quantity desc
	limit 100;
 end //
 
delimiter ;

-- проверим

call get_top_songs('electronic');



