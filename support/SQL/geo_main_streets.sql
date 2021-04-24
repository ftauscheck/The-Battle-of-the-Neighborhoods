CREATE TABLE `geo_main_streets` (
	`code` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`name` VARCHAR(100) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`status` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`sub_system` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`geometry` LINESTRING NOT NULL,
	INDEX `Index 1` (`geometry`(32))
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
