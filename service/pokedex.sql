CREATE DATABASE IF NOT EXISTS `pokemon_db` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
SHOW DATABASES;

USE `pokemon_db`;


CREATE TABLE IF NOT EXISTS `pokedex_id` (
    `p_id` INT(11) AUTO_INCREMENT,  
    PRIMARY KEY (`p_id`)
) ENGINE=myISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `pokedex` (
    `pokemon_id` INT,
    `id` INT,
    `num` INT,
    `name` VARCHAR(45),
    `img` VARCHAR(45),
    `height` VARCHAR(45),
    `weight` VARCHAR(45),
    `candy` VARCHAR(45),
    `candy_count` INT,
    `egg` VARCHAR(45),
    `spawn_chance` INT,
    `avg_spawns` INT,
    `spawn_time` VARCHAR(45),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`pokemon_id`) REFERENCES pokedex_id(`p_id`)
)ENGINE=myISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `pokemon_type` (
    `type_id` INT,
    `id` INT,
    `value` VARCHAR(45),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`type_id`) REFERENCES pokedex(`id`)
)ENGINE=myISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `pokemon_multipliers` (
    `type_id` INT,
    `id` INT,
    `value` VARCHAR(45),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`type_id`) REFERENCES pokedex(`id`)
)ENGINE=myISAM DEFAULT CHARSET=utf8;

CREATE TABLE  IF NOT EXISTS `pokemon_weaknesses` (
    `type_id` INT,
    `id` INT,
    `value` VARCHAR(45),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`type_id`) REFERENCES pokedex(`id`)
)ENGINE=myISAM DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `pokemon_next_evolution` (
    `type_id` INT,
    `id` INT,
    `num` VARCHAR(45),
    `name` VARCHAR(45),
    PRIMARY KEY (`id`),
    FOREIGN KEY (`type_id`) REFERENCES pokedex(`id`)
)ENGINE=myISAM DEFAULT CHARSET=utf8;