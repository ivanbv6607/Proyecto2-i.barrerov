-- MySQL dump 10.13  Distrib 8.0.31, for Win64 (x86_64)
--
-- Host: localhost    Database: heladerias_db
-- ------------------------------------------------------
-- Server version	8.0.31

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
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `id` int NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `costo` decimal(6,2) DEFAULT NULL,
  `calorias` int DEFAULT NULL,
  `inventario` decimal(5,2) DEFAULT NULL,
  `tipo` tinyint DEFAULT NULL,
  `es_vegetariano` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (1,'Helado de Fresa',500.00,5,5.00,1,0),(2,'Helado Ron con pasas',700.00,6,10.00,1,0),(3,'Crema de vainila',400.00,4,15.00,1,0),(4,'Fresas',150.00,3,10.00,0,1),(5,'Uvas pasas',200.00,5,10.00,0,1),(6,'Mani japones',100.00,4,10.00,0,0),(7,'Crema chantilli',80.00,3,10.00,0,0),(8,'Mandarinas',150.00,5,10.00,0,1);
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `producto_ingrediente`
--

DROP TABLE IF EXISTS `producto_ingrediente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `producto_ingrediente` (
  `id` int NOT NULL,
  `producto` int NOT NULL,
  `ingrediente` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `prd_1` (`producto`) /*!80000 INVISIBLE */,
  KEY `ing_1` (`ingrediente`),
  CONSTRAINT `fk_ing` FOREIGN KEY (`ingrediente`) REFERENCES `ingredientes` (`id`),
  CONSTRAINT `fk_prd` FOREIGN KEY (`producto`) REFERENCES `productos` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `producto_ingrediente`
--

LOCK TABLES `producto_ingrediente` WRITE;
/*!40000 ALTER TABLE `producto_ingrediente` DISABLE KEYS */;
INSERT INTO `producto_ingrediente` VALUES (1,1,1),(2,1,4),(3,2,3),(4,2,8),(5,3,3),(6,3,4);
/*!40000 ALTER TABLE `producto_ingrediente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `id` int NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `precio` decimal(6,2) DEFAULT NULL,
  `tipo` tinyint DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Samurai de fresas',1200.00,1),(2,'Samurai de mandarinas',2000.00,1),(3,'Malteada chocoespacial',3500.00,0),(4,'Cupihelado',2000.00,0);
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-03-14 16:55:25
