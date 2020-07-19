DROP DATABASE IF EXISTS vk;
CREATE DATABASE vk;
USE vk;

DROP TABLE IF EXISTS users;
CREATE TABLE users(
	id SERIAL PRIMARY KEY,
	email VARCHAR(120) UNIQUE,
	phone VARCHAR(15),
	pass VARCHAR(200)
);

DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles(
	id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	gender CHAR(1),
	name VARCHAR(100),
	surname VARCHAR(100),
	birthday DATE,
	photo_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	hometown VARCHAR(100),
	-- bio TEXT,
	FOREIGN KEY (user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS messages;
CREATE TABLE messages(
	id SERIAL PRIMARY KEY,
	from_user_id BIGINT UNSIGNED NOT NULL,
	to_user_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	is_read BOOL,
	created_at DATETIME default NOW(),
	INDEX(from_user_id),
	INDEX(to_user_id),
	FOREIGN KEY (from_user_id) REFERENCES users(id),
	FOREIGN KEY (to_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS friend_requests;
CREATE TABLE friend_requests(
	initiator_user_id BIGINT UNSIGNED NOT NULL,
	target_user_id BIGINT UNSIGNED NOT NULL,
	status ENUM('requested', 'approved', 'unfriended', 'declined') DEFAULT 'requested',
	requested_at DATETIME DEFAULT NOW(),
	confirmed_at DATETIME DEFAULT NULL,
	PRIMARY KEY(initiator_user_id, target_user_id),
	INDEX(initiator_user_id),
	INDEX(target_user_id),
	FOREIGN KEY(initiator_user_id) REFERENCES users(id),
	FOREIGN KEY(target_user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS communities;
CREATE TABLE communities(
	id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	INDEX(name)
);

DROP TABLE IF EXISTS users_communities;
CREATE TABLE users_communities(
	user_id BIGINT UNSIGNED NOT NULL,
	community_id BIGINT UNSIGNED NOT NULL,
	is_admin BOOL,
	PRIMARY KEY(user_id, community_id),
	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY(community_id) REFERENCES communities(id)
);

DROP TABLE IF EXISTS posts;
CREATE TABLE posts(
	id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	attachments JSON,
	metadata JSON,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY(user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS comments;
CREATE TABLE comments(
	id SERIAL PRIMARY KEY,
	user_id BIGINT UNSIGNED NOT NULL,
	post_id BIGINT UNSIGNED NOT NULL,
	body TEXT,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY(post_id) REFERENCES posts(id)
);

DROP TABLE IF EXISTS photos;
CREATE TABLE photos(
	id SERIAL PRIMARY KEY,
	file VARCHAR(255),
	user_id BIGINT UNSIGNED NOT NULL,
	description TEXT,
	created_at DATETIME DEFAULT NOW(),
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	FOREIGN KEY(user_id) REFERENCES users(id)
);

DROP TABLE IF EXISTS repost;
CREATE TABLE repost(
	id SERIAL PRIMARY KEY,
	post_id BIGINT UNSIGNED NOT NULL,
	reposted_to BIGINT UNSIGNED NOT NULL,
	reposted_from BIGINT UNSIGNED NOT NULL,
	reposted_at DATETIME DEFAULT NOW(),
	FOREIGN KEY(post_id) REFERENCES posts(id),
	FOREIGN KEY(reposted_to) REFERENCES users(id),
	FOREIGN KEY(reposted_from) REFERENCES posts(id)
);

DROP TABLE IF EXISTS liked_photos;
CREATE TABLE liked_photos(
	user_id BIGINT UNSIGNED NOT NULL,
	photo_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	PRIMARY KEY(user_id, photo_id),
	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY(photo_id) REFERENCES photos(id)	
);

DROP TABLE IF EXISTS liked_posts;
CREATE TABLE liked_posts(
	user_id BIGINT UNSIGNED NOT NULL,
	post_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	PRIMARY KEY(user_id, post_id),
	FOREIGN KEY(user_id) REFERENCES users(id),
	FOREIGN KEY(post_id) REFERENCES posts(id)	
);

DROP TABLE IF EXISTS liked_users;
CREATE TABLE liked_users(
	initiator_user_id BIGINT UNSIGNED NOT NULL,
	target_user_id BIGINT UNSIGNED NOT NULL,
	created_at DATETIME DEFAULT NOW(),
	FOREIGN KEY(initiator_user_id) REFERENCES users(id),
	FOREIGN KEY(target_user_id) REFERENCES users(id)
);
