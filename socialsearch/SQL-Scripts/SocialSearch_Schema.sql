/* SocialSearch Schema */


CREATE TABLE IF NOT EXISTS 
`users` (
	`id` int(11) AUTO_INCREMENT,
	`given_name` varchar(256),
	`formatted` varchar(256),			
	`family_name` varchar(256),
	`email` varchar(256) UNIQUE NOT NULL,
	`about` varchar(512),
	`password` varchar(256),
	`user_id` varchar(256),
	`domain` varchar(256),
	`access_token` varchar(256),
	`refresh_token` varchar(256),
	`profile_pic` varchar(512),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`user_stats` (
	`id` int(11) AUTO_INCREMENT,
	`user_id` int(11),
	`points` int(11),
	FOREIGN KEY (`user_id`) REFERENCES users(`id`),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`badges` (
	`id` int(11) AUTO_INCREMENT,
	`name` varchar(256),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`user_badges` (
	`id` int(11) AUTO_INCREMENT,
	`user_id` int(11),
	`badge_id` int(11),
	FOREIGN KEY (`user_id`) REFERENCES users(`id`),
	FOREIGN KEY (`badge_id`) REFERENCES badges(`id`),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`tags` (
	`id` int(11) AUTO_INCREMENT,
	`name` varchar(256),
	`created_by` int(11),
	FOREIGN KEY (`created_by`) REFERENCES users(`id`),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`user_followed_tags` (
	`id` int(11) AUTO_INCREMENT,
	`user_id` int(11),
	`tag_id` int(11),
	FOREIGN KEY (`user_id`) REFERENCES users(`id`),
	FOREIGN KEY (`tag_id`) REFERENCES tags(`id`),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`posts` (
	`id` int(11) AUTO_INCREMENT,
	`time` int(20),
	`user_id` int(11),
	`rank_weight` int(11),
	`content` varchar(2048),
	`content_type` varchar(256),
	FOREIGN KEY (`user_id`) REFERENCES users(`id`),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`post_tags` (
	`id` int(11) AUTO_INCREMENT,
	`post_id` int(11),
	`tag_id` int(11),
	FOREIGN KEY (`post_id`) REFERENCES posts(`id`),
	FOREIGN KEY (`tag_id`) REFERENCES tags(`id`),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`post_likes` (
	`id` int(11) AUTO_INCREMENT,
	`post_id` int(11),
	`user_id` int(11),
	FOREIGN KEY (`post_id`) REFERENCES posts(`id`),
	FOREIGN KEY (`user_id`) REFERENCES users(`id`),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



CREATE TABLE IF NOT EXISTS 
`post_dislikes` (
	`id` int(11) AUTO_INCREMENT,
	`post_id` int(11),
	`user_id` int(11),
	FOREIGN KEY (`post_id`) REFERENCES posts(`id`),
	FOREIGN KEY (`user_id`) REFERENCES users(`id`),
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



/*

CREATE TABLE IF NOT EXISTS 
`dummy` (
	`id` int(11) AUTO_INCREMENT,
	PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1; 

*/
