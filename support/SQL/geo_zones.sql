CREATE TABLE `geo_zones` (
	`nm_groups` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`cd_zone` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`nm_zone` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`sg_zone` VARCHAR(50) NULL DEFAULT NULL COLLATE 'utf8_general_ci',
	`geometry` POLYGON NOT NULL,
	INDEX `idx_geometry` (`geometry`(32)) USING BTREE,
	INDEX `idx_sgzone` (`sg_zone`) USING BTREE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
