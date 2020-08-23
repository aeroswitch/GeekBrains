use spotify;
 
insert into subscription_type (`type`, description, price, advertising_enabled, trial_period, offline_access_to_music, option_to_disable_explicit_content) values
	('free', 'Возможность слушать музыку бесплатно с периодическим перерывов на рекламу', 0.00, true, false, false, false),
	('premium_trial', ' Попробуй Spotify сейчас! На любом устройстве. 3 месяца пробного Premium доступа', 0.00, false, true, true, false),
	('premium_for_1', 'Музыка без рекламы. Доступ к музыке в офлайн-режиме. Выбор любого трека', 169.00, false, false, true, false),
	('premium_for_2', 'Микс для двоих — плейлист с музыкой, которая нравится вам обоим. Обновляется регулярно.', 219.00, false, false, true, false),
	('premium_for_family', 'Микс для семьи — плейлист с музыкой, которая нравится всей семье. Музыку для взрослых можно заблокировать', 269.00, false, false, true, true),
	('premium_for_students', 'Скидка для студентов аккредитованных вузов', 169.00, false, false, true, false);

