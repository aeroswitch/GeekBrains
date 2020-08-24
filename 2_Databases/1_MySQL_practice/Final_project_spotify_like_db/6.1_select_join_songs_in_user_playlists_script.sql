-- просмотр треков в плейлисте юзера с детальной информацией о треке и артисте

select 
	u.id as user_id,
	u.username,
	up.title as playlist_title,
	s.title as song_title,
	a.name as artist_name,
	s.duration as song_duration,
	s.genre as song_genre
from 
	songs as s
join 
	artists as a on s.artist_id = a.id
join 
	songs_in_user_playlists as siup on s.id = siup.song_id
join 
	user_playlists as up on up.id = siup.playlist_id
join 
	users as u on u.id = up.user_id 
order by
	u.id, playlist_id
limit 40;

