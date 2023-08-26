-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: searchtable
-- ------------------------------------------------------
-- Server version	8.0.32

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
-- Table structure for table `buy`
--

DROP TABLE IF EXISTS `buy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `buy` (
  `Books` varchar(50) DEFAULT NULL,
  `Book_Number` int unsigned DEFAULT NULL,
  `Price` double DEFAULT NULL,
  `Book_Quantity` int unsigned DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `buy`
--

LOCK TABLES `buy` WRITE;
/*!40000 ALTER TABLE `buy` DISABLE KEYS */;
INSERT INTO `buy` VALUES ('More Peak District',101,12.99,10),('Lincoinshire Worlds',102,10.99,40),('Value Of York',103,11.99,10),('Peak District',104,12.99,10),('Snowdonia',105,13.99,0),('Malvern and Warwickshire',106,10.99,10),('Cheshire',107,12.99,8);
/*!40000 ALTER TABLE `buy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `search`
--

DROP TABLE IF EXISTS `search`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `search` (
  `Id` int NOT NULL AUTO_INCREMENT,
  `Area` varchar(50) DEFAULT NULL,
  `Book` varchar(100) DEFAULT NULL,
  `WalkName` varchar(100) DEFAULT NULL,
  `Distance` double DEFAULT NULL,
  `Difficult` varchar(50) DEFAULT NULL,
  `Page` int unsigned DEFAULT NULL,
  PRIMARY KEY (`Id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search`
--

LOCK TABLES `search` WRITE;
/*!40000 ALTER TABLE `search` DISABLE KEYS */;
INSERT INTO `search` VALUES (1,'peakdistrict','More Peak District','Hathasage',7,'Easy',67),(2,'peakdistrict','More Peak District','Hope and Win Hill',4.5,'Medium',18),(3,'lincoinshire','Lincolnshire Worlds','Thornton Abbey',3.5,'Easy',20),(4,'lincoinshire','Lincolnshire Worlds','Tennyson County',5,'Hard',28),(5,'york','Value of York','Cowlam and Cotham',8,'Hard',64),(6,'york','Value of York','Friedaythorpe',7,'Easy',42),(7,'peakdistrict','Peak District','Magpie Mine',4.5,'Medium',20),(8,'peakdistrict','Peak District','Loard\'s Seat',5.5,'Easy',28),(9,'northwales','Snowdonia','Around Aber',4,'hard',24),(10,'northwales','Snowdonia','Yr Eifl',3.5,'Medium',42),(11,'warwickshire','Malvern and Warwickshire','Bidford-Upon-Avon',8.5,'Medium',78),(12,'cheshire','Cheshire','Dane Valley',5,'Easy',20),(13,'cheshire','Cheshire','Malpas',8.5,'Medium',80),(14,'cheshire','Cheshire','Farndon',6,'Hard',48),(15,'cheshire','Cheshire','Delamere Forest',5.5,'Easy',30);
/*!40000 ALTER TABLE `search` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `Useripaddr` varchar(50) DEFAULT NULL,
  `portofuser` int unsigned DEFAULT NULL,
  `books_buy` int unsigned DEFAULT NULL,
  `Total_Cost` int unsigned DEFAULT NULL,
  `Back_order` int unsigned DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('192.168.56.1',62043,8,11,7),('192.168.56.1',62043,8,11,7),('192.168.56.1',59605,8,11,7),('192.168.56.1',59653,8,11,7),('192.168.56.1',59661,8,11,7),('192.168.56.1',59663,8,11,7),('192.168.56.1',59672,8,11,7),('192.168.56.1',59699,8,11,7),('192.168.56.1',59705,8,11,7),('192.168.56.1',59706,8,11,7),('192.168.56.1',59708,8,11,7),('192.168.56.1',59709,8,11,7);
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

-- Dump completed on 2023-03-25  8:58:22
