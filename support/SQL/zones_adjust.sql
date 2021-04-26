-- --------------------------------------------------------
-- Servidor:                     127.0.0.1
-- Versão do servidor:           8.0.23-0ubuntu0.20.04.1 - (Ubuntu)
-- OS do Servidor:               Linux
-- HeidiSQL Versão:              11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

-- Copiando estrutura para tabela project.zones_adjust
CREATE TABLE IF NOT EXISTS `zones_adjust` (
  `sg_zone` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci DEFAULT NULL,
  `sg_short` char(5) COLLATE utf8mb4_general_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- Copiando dados para a tabela project.zones_adjust: ~0 rows (aproximadamente)
/*!40000 ALTER TABLE `zones_adjust` DISABLE KEYS */;
INSERT INTO `zones_adjust` (`sg_zone`, `sg_short`) VALUES
	('APA-IGUACU', 'APA'),
	('APA-PASSAUNA', 'APA'),
	('CONEC-1', 'CONEC'),
	('CONEC-2', 'CONEC'),
	('CONEC-3', 'CONEC'),
	('CONEC-4', 'CONEC'),
	('POLO-LV', 'POLO'),
	('SC-SF', 'SC'),
	('SC-UM', 'SC'),
	('SE', 'SE'),
	('SE-AC', 'SE'),
	('SE-CB', 'SE'),
	('SE-CC', 'SE'),
	('SE-CF', 'SE'),
	('SE-I', 'SE'),
	('SE-LE', 'SE'),
	('SE-LV', 'SE'),
	('SE-MF', 'SE'),
	('SE-NC', 'SE'),
	('SE-OI', 'SE'),
	('SE-PS', 'SE'),
	('SE-PT', 'SE'),
	('SE-WB', 'SE'),
	('SEHIS', 'SEHIS'),
	('SER-CIC', 'SER'),
	('SH', 'SH'),
	('UC', 'UC'),
	('Z-CON', 'Z-CON'),
	('ZC', 'ZC'),
	('ZE-D', 'ZE'),
	('ZE-D-LV', 'ZE'),
	('ZE-E', 'ZE'),
	('ZE-M', 'ZE'),
	('ZES', 'ZE'),
	('ZI', 'ZI'),
	('ZI-LV', 'ZI'),
	('ZR-1', 'ZR1'),
	('ZR-2', 'ZR2'),
	('ZR-3', 'ZR3'),
	('ZR-4', 'ZR4'),
	('ZR-4-LV', 'ZR4'),
	('ZR-AG', 'ZR'),
	('ZR-B', 'ZR'),
	('ZR-M', 'ZR'),
	('ZR-OC', 'ZR'),
	('ZR-P', 'ZR'),
	('ZR-SF', 'ZR'),
	('ZR-U', 'ZR'),
	('ZS-1', 'ZS1'),
	('ZS-2', 'ZS2'),
	('ZS-2-LV', 'ZS2'),
	('ZT-LV', 'ZT'),
	('ZT-MF', 'ZT'),
	('ZT-NC', 'ZT'),
	('ZUM', 'ZUM');
/*!40000 ALTER TABLE `zones_adjust` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
