--  список треков с именем артиста, названием и деталями релиза

create or replace view 
	songs_with_artist_release 
as select
	s.id as song_id,
	s.title as song_title,
	a.name as artist_name,
	s.genre as song_genre,
	s.duration as song_duration,
	r.title as release_title,
	r.`type` as release_type	
from 
	songs as s
join 
	artists as a on s.artist_id = a.id
join
	releases as r on s.release_id = r.id
order by 
	s.id;

-- проверим

select * from songs_with_artist_release; 
