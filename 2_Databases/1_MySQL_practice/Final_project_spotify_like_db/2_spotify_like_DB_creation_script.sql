drop database if exists spotify;
create database spotify character SET utf8 collate utf8_general_ci;
use spotify;

create table users (
	id serial primary key,
	username varchar(100) unique,
	`password` varchar(200),
	gender char(1),
	email varchar(100),
	birthday date,
	country char(2),
	created_date datetime default NOW(),
	updated_date datetime default NOW()
) comment = 'Spotify service users';

create table subscription_type (
	id serial primary key,
	`type` enum('free', 'premium_trial', 'premium_for_1', 'premium_for_2', 'premium_for_family', 'premium_for_students', 'spotify_employee'),
	description text,
	price decimal(10,2),
	advertising_enabled bool,
	trial_period bool,
	offline_access_to_music bool,
	option_to_disable_explicit_content bool
);

create table users_subscriptions_orders_history (
	id serial primary key,
	user_id bigint unsigned not null,
	subscription_id bigint unsigned not null,
	status enum('paid', 'refunded', 'awaiting payment'),
	purchase_date datetime default NOW(),
	foreign key(user_id) references users(id),
	foreign key(subscription_id) references subscription_type(id)
); 

create table users_subscriptions (
	user_id bigint unsigned not null,
	subscription_id bigint unsigned not null,
	order_id bigint unsigned not null,
	expiration_date datetime,
	is_active bool,
	foreign key(user_id) references users(id),
	foreign key(subscription_id) references subscription_type(id),
	foreign key(order_id) references users_subscriptions_orders_history(id)
); 

create table artists (	
	id serial primary key,
	name varchar(100),	
	artist_biography text,
	followers_quantity int unsigned, -- shows how many users added the artist to "follow"
	monthly_listeners_quantity int unsigned, -- shows how many times all spotify users listened to the artist at least once each month
	social_media_link_instagram varchar(255) unique,
	social_media_link_twitter varchar(255) unique,
	social_media_link_facebook varchar(255) unique
);

create table releases (
	id serial primary key,
	title varchar(100),
	image_file_link varchar(255),
	`type` enum('single', 'EP', 'album'),
	added_to_service_date datetime default NOW()
) comment = 'Singles, EPs and albums';

create table songs (
	id serial primary key,
	title varchar(100),
	artist_id bigint unsigned not null,
	release_id bigint unsigned not null,
	genre varchar(50),
	is_explicit bool default false, -- shows if song contains profanity
	duration time,
	daily_plays_quantity int unsigned,
	users_play_counter int unsigned, -- shows how many times all spotify users played this song
	added_to_service_date datetime default NOW(),
	foreign key(artist_id) references artists(id),
	foreign key(release_id) references releases(id)
);

create table songs_in_releases (
	song_id bigint unsigned not null,
	release_id bigint unsigned not null,
	foreign key(song_id) references songs(id),
	foreign key(release_id) references releases(id)		
);

create table users_songs_hisory (
	user_id bigint unsigned not null,
	song_id bigint unsigned not null,
	listened_date datetime default NOW(),
	listening_duration time,
	foreign key(user_id) references users(id),
	foreign key(song_id) references songs(id)	
);

create table user_playlists (
	id serial primary key,
	title varchar(100),
	user_id bigint unsigned not null,
	playlist_total_duration time,
	is_public bool,
	created_date datetime default NOW(),
	updated_date datetime default NOW(),
	foreign key(user_id) references users(id)
) comment = 'Playlists created by users';

create table public_playlists (
	id serial primary key,
	title varchar(100),
	description text,
	image_file_link varchar(255),
	playlist_total_duration time,
	created_date datetime default NOW(),
	updated_date datetime default NOW(),
	followers_counter int unsigned -- shows how many users added the playlist to "follow"
);

create table songs_in_user_playlists (
	playlist_id bigint unsigned not null,
	song_id bigint unsigned not null,
	added_to_playlist_date datetime default NOW(),
	foreign key(playlist_id) references user_playlists(id),
	foreign key(song_id) references songs(id)
) comment = 'Songs added to users playlists by users';

create table songs_in_public_playlists (
	playlist_id bigint unsigned not null,
	song_id bigint unsigned not null,
	added_to_playlist_date datetime default NOW(),
	foreign key(playlist_id) references public_playlists(id),
	foreign key(song_id) references songs(id)
) comment = 'Songs added to public playlists by the service administrator';

create table songs_liked_by_users (
	user_id bigint unsigned not null,
	song_id bigint unsigned not null,
	foreign key(user_id) references users(id),
	foreign key(song_id) references songs(id)
);

create table recommended_mixes_for_user (
	id serial primary key,
	title varchar(100),
	created_for bigint unsigned not null,
	mix_total_duration time,
	created_date datetime default NOW(),
	updated_date datetime default NOW(),
	foreign key(created_for) references users(id)	
) comment = 'Similar to playlists, but mixes created for using recommendations functionality for specific users based on liked songs';

create table songs_in_mixes (
	mix_id bigint unsigned not null,
	song_id bigint unsigned not null,
	added_to_mix_date datetime default NOW(),
	foreign key(mix_id) references recommended_mixes_for_user(id),
	foreign key(song_id) references songs(id)
) comment = 'Songs added to playlists by users';


create table genres_moods_categories ( 
	id serial primary key,
	title varchar(100),
	image_file_link varchar(255),
	created_date datetime default NOW(),
	updated_date datetime default NOW()
) comment = 'Groups various public playlists under different categories based on selected genre or user\'s mood';

create table playlists_in_genres_moods_categories (
	genre_mood_category_id bigint unsigned not null,
	public_playlist_id bigint unsigned not null,
	added_to_genre_mood_category_date datetime default NOW(),
	foreign key(genre_mood_category_id) references genres_moods_categories(id),
	foreign key(public_playlist_id) references public_playlists(id)
);

create table top_charts (
	id serial primary key,
	title varchar(100),
	description text,
	image_file_link varchar(255),
	followers_counter int unsigned,-- shows how many users added the chart to "follow"
	created_date datetime default NOW(),
	updated_date datetime default NOW()
) comment = 'Playlists of most popular songs based on quantity of listens by users in certain music genre';

create table songs_in_top_charts (
	top_chart_id bigint unsigned not null,
	song_id bigint unsigned not null,
	foreign key(top_chart_id) references top_charts(id),
	foreign key(song_id) references songs(id)		
);

create table user_follows_artists (
	user_id bigint unsigned not null,
	artist_id bigint unsigned not null,
	foreign key(user_id) references users(id),
	foreign key(artist_id) references artists(id)
);

create table user_follows_public_playlists (
	user_id bigint unsigned not null,
	playlist_id bigint unsigned not null,
	foreign key(user_id) references users(id),
	foreign key(playlist_id) references public_playlists(id)
);

create table user_follows_top_charts (
	user_id bigint unsigned not null,
	chart_id bigint unsigned not null,
	foreign key(user_id) references users(id),
	foreign key(chart_id) references top_charts(id)
);
