-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: schoolcommunity
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `Id` bigint NOT NULL AUTO_INCREMENT,
  `UserName` varchar(50) DEFAULT NULL,
  `UserPWD` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'admin','123456');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communityforums`
--

DROP TABLE IF EXISTS `communityforums`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communityforums` (
  `Id` bigint NOT NULL AUTO_INCREMENT,
  `UsersId` bigint DEFAULT NULL,
  `path` varchar(255) DEFAULT NULL,
  `Title` varchar(255) DEFAULT NULL,
  `Content` longtext,
  `PublichTime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communityforums`
--

LOCK TABLES `communityforums` WRITE;
/*!40000 ALTER TABLE `communityforums` DISABLE KEYS */;
INSERT INTO `communityforums` VALUES (2,1,'eb02052b-8f0c-4ef1-ad28-689364c065e6.jpg;c4d7c1ab-55bd-4362-a2a4-dcc1ec73a8f8.jpg;dc1162d0-a909-4808-96c9-a00756e226a3.jpg;484e5e85-db91-496b-905e-f053bc7ac86d.jpg;','杞欢宸ョ▼椤圭洰','闂藉畞璺ㄥ煙鍗忎綔瀹?,'2024-10-05 19:35:42');
/*!40000 ALTER TABLE `communityforums` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `communityforumscomments`
--

DROP TABLE IF EXISTS `communityforumscomments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `communityforumscomments` (
  `Id` bigint NOT NULL AUTO_INCREMENT,
  `UsersId` bigint DEFAULT NULL,
  `CommunityForumsId` bigint DEFAULT NULL,
  `CommentsContent` longtext,
  `CommentsTime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `communityforumscomments`
--

LOCK TABLES `communityforumscomments` WRITE;
/*!40000 ALTER TABLE `communityforumscomments` DISABLE KEYS */;
/*!40000 ALTER TABLE `communityforumscomments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goods` (
  `Id` bigint NOT NULL AUTO_INCREMENT,
  `UsersId` bigint DEFAULT NULL,
  `GoodsPath` varchar(255) DEFAULT NULL,
  `GoodsName` varchar(255) DEFAULT NULL,
  `GoodsDetail` longtext,
  `GoodsPrices` decimal(10,2) DEFAULT NULL,
  `PublichTime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goods`
--

LOCK TABLES `goods` WRITE;
/*!40000 ALTER TABLE `goods` DISABLE KEYS */;
INSERT INTO `goods` VALUES (2,1,'8df60c85-80fe-4fc9-a06f-0eed0b815598.jpg;9c73458d-ee23-475e-a40f-d0eab8ef413c.jpg;6ee9a963-86d0-45bf-848c-e53e6f9ed341.jpg;b135e1a3-62d2-4984-adc9-8c057cf5c366.jpg;','鍥介缁樼敾','鎷涘嫙缁樼敾涓撲笟銆乸s銆乸r鐨勫悓瀛?,1234444.00,'2024-10-07 14:48:03'),(3,1,'91dbddfc-6aa5-42a2-80e4-aa37395bb6e4.jpg;07d73763-8506-4738-9518-8488bfcbbe59.jpg;5501c5de-6d69-4d8a-b504-6da07ad478fc.jpg;a4464759-765a-4418-bc78-9447dcaa20d2.jpg;','鍐版縺鍑屽皬绋嬪簭','瑕佹眰绮鹃€欰ndroid銆乸ython銆亀eb绛夊悓瀛﹀姞鍏ヨ繘鏉?,2500000.00,'2024-10-07 14:53:08');
/*!40000 ALTER TABLE `goods` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `goodscomments`
--

DROP TABLE IF EXISTS `goodscomments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `goodscomments` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `UsersId` varchar(45) DEFAULT NULL,
  `GoodsId` varchar(45) DEFAULT NULL,
  `CommentsContent` varchar(45) DEFAULT NULL,
  `CommentsTime` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `goodscomments`
--

LOCK TABLES `goodscomments` WRITE;
/*!40000 ALTER TABLE `goodscomments` DISABLE KEYS */;
INSERT INTO `goodscomments` VALUES (1,'1','2','鎴戞兂鍔犲叆锛?!','2024-10-07 15:07:05'),(2,'1','2','闃垮崱鐪嬩笉鍑?,'2024-10-07 15:07:30');
/*!40000 ALTER TABLE `goodscomments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schoolnewcomments`
--

DROP TABLE IF EXISTS `schoolnewcomments`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schoolnewcomments` (
  `Id` bigint NOT NULL AUTO_INCREMENT,
  `UsersId` bigint DEFAULT NULL,
  `SchoolNewId` bigint DEFAULT NULL,
  `CommentsContent` longtext,
  `CommentsTime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schoolnewcomments`
--

LOCK TABLES `schoolnewcomments` WRITE;
/*!40000 ALTER TABLE `schoolnewcomments` DISABLE KEYS */;
/*!40000 ALTER TABLE `schoolnewcomments` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `schoolnewname`
--

DROP TABLE IF EXISTS `schoolnewname`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `schoolnewname` (
  `Id` bigint NOT NULL AUTO_INCREMENT,
  `SchoolNewPath` varchar(255) DEFAULT NULL,
  `SchoolNewName` varchar(255) DEFAULT NULL,
  `SchoolNewContent` longtext,
  `PublichTime` datetime DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `schoolnewname`
--

LOCK TABLES `schoolnewname` WRITE;
/*!40000 ALTER TABLE `schoolnewname` DISABLE KEYS */;
INSERT INTO `schoolnewname` VALUES (1,'59f5cbfc-8086-4e87-8ea7-c02efb4497c2.jpg;c0835812-8a9f-4fa3-8881-dd9b5be4eb08.jpg;1fb16bab-0271-4469-b2c2-a2142b7fd88c.jpg;5969e034-ec4f-43a7-83b7-a0ed770123bf.jpg;','椤圭洰璧勮',' 鈥滈椊瀹佽法鍩熷悎浣滃疂鈥濄€傚畾浣嶄负涓€娆句笓闂ㄦ湇鍔′簬澶у鐢熺殑璺ㄤ笓涓氶」鐩悎浣滃钩鍙帮紝鏃ㄥ湪鎵撶牬涓撲笟澹佸瀿锛屼績杩涗笉鍚屽绉戝鐢熶箣闂寸殑浜ゆ祦涓庡悎浣滐紝鎻愬崌澶у鐢熺殑缁煎悎鑳藉姏鍜屽垱鏂版按骞炽€?,'2024-10-07 07:12:00');
/*!40000 ALTER TABLE `schoolnewname` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `UserName` varchar(50) DEFAULT NULL,
  `PWD` varchar(50) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Phone` varchar(45) DEFAULT NULL,
  `Card` varchar(50) DEFAULT NULL,
  `StudentClass` varchar(255) DEFAULT NULL,
  `Address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'qqq','123456','鐜嬫鑱?,'112345678','610xxxxxxxxxxxx','澶ф暟鎹?鐝?,'绂忓窞澶у');
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

-- Dump completed on 2024-10-09 11:23:48
