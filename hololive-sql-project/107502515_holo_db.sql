CREATE DATABASE  IF NOT EXISTS `holo_db` /*!40100 DEFAULT CHARACTER SET utf8 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `holo_db`;
-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: holo_db
-- ------------------------------------------------------
-- Server version	8.0.22

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `holo_info`
--

DROP TABLE IF EXISTS `holo_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `holo_info` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT 'holo_id',
  `holo_name` varchar(32) NOT NULL COMMENT '本名',
  `holo_gender` enum('男','女') NOT NULL COMMENT '性别',
  `holo_age` varchar(32) NOT NULL COMMENT '年龄',
  `holo_height` varchar(32) NOT NULL COMMENT '身高',
  `holo_alias` varchar(32) NOT NULL COMMENT '別名',
  `holo_group` varchar(32) NOT NULL COMMENT '團體',
  PRIMARY KEY (`id`),
  UNIQUE KEY `holo_name` (`holo_name`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holo_info`
--

LOCK TABLES `holo_info` WRITE;
/*!40000 ALTER TABLE `holo_info` DISABLE KEYS */;
INSERT INTO `holo_info` VALUES (25,'赤井心','女','16','154cm','哈洽瑪','JP一期生'),(28,'星街彗星','女','18','160cm','有點神經病的藍髮大姊姊','零期生(又稱無印生)'),(30,'兔田佩可拉','女','111','153(不含兔耳)','PekoPeko~~','JP三期生'),(31,'寶鐘瑪琳','女','17','150cm','船長','JP三期生'),(32,'桐生可可','女','3501','180cm(人型)7m(龍型)','會長','JP四期生'),(33,'雪花菈米','女','210(人類年齡的21歲)','158cm','雪媽','JP五期生'),(34,'森美聲','女','沒有','167cm','死神','EN一期生'),(35,'小鳥遊キアラ','女','不死鳥','165cm','火雞','EN一期生'),(36,'Gawr Gura','男','9000','141cm','A','EN一期生');
/*!40000 ALTER TABLE `holo_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int unsigned NOT NULL AUTO_INCREMENT COMMENT '帳戶id',
  `user_name` varchar(32) NOT NULL COMMENT '帳戶',
  `user_password` varchar(23) NOT NULL COMMENT '密碼',
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_name` (`user_name`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'a','a'),(2,'gura','shark'),(3,'usagi','pecopeco');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-23  0:39:33
