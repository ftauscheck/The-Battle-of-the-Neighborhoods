CREATE TABLE `geo_neighbour` (
	`id` INT(10) UNSIGNED NOT NULL,
	`type` VARCHAR(50) NOT NULL DEFAULT '' COLLATE 'utf8mb4_unicode_ci',
	`name` VARCHAR(100) NOT NULL DEFAULT '' COLLATE 'utf8mb4_unicode_ci',
	`area` DECIMAL(20,6) NOT NULL,
	`regional_id` INT(10) UNSIGNED NOT NULL,
	`regional_name` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_unicode_ci',
	`geometry` GEOMETRY NOT NULL,
	INDEX `idx_id` (`id`) USING BTREE,
	INDEX `Index 2` (`geometry`(32))
)
COLLATE='utf8mb4_unicode_ci'
ENGINE=InnoDB
;
