-- сделаем триггер на добавление трека в плейлист юзера, который будет выдавать ошибку если трек содержит ненормативную лексику

delimiter //
use spotify//

drop trigger if exists restrict_adding_explicit_tracks//

create trigger restrict_adding_explicit_tracks before insert on songs_in_user_playlists
for each row
begin
 if
	 (new.song_id in(select id from songs where is_explicit = 1))
 then
	signal sqlstate '45000' set message_text = 'explicit track!';
 end if;
end//
delimiter ;


-- проверим триггер на примере трека с ненормативной лексикой

insert into 
	songs_in_user_playlists (playlist_id, song_id) 
values
	(12, 6);


-- и на примере трека без ненормативной лексики
insert into 
	songs_in_user_playlists (playlist_id, song_id) 
values
	(12, 4);
	

	