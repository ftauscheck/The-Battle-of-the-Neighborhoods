CREATE TABLE `data_neighbour` (
	`neighbourhood` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_general_ci',
	`norm_neighbourhood` VARCHAR(100) NOT NULL COLLATE 'utf8mb4_general_ci',
	`area` DECIMAL(20,3) NOT NULL,
	`num_man` INT(10) UNSIGNED NOT NULL DEFAULT '0',
	`num_woman` INT(10) UNSIGNED NOT NULL DEFAULT '0',
	`pop_total` INT(10) UNSIGNED NOT NULL DEFAULT '0',
	`num_houses` INT(10) UNSIGNED NOT NULL DEFAULT '0',
	`mean_revenue_house` DECIMAL(20,3) NOT NULL,
	INDEX `idx_neighbour` (`norm_neighbourhood`) USING BTREE
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;
