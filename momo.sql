-- MySQL dump 10.13  Distrib 5.5.40, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: momo
-- ------------------------------------------------------
-- Server version	5.5.40-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `discount`
--

DROP TABLE IF EXISTS `discount`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `discount` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `mall_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '商场id',
  `major_type` mediumint(8) unsigned NOT NULL DEFAULT '0' COMMENT '主类别',
  `minor_type` mediumint(8) unsigned NOT NULL DEFAULT '0' COMMENT '从类别',
  `brand_id` int(10) unsigned NOT NULL DEFAULT '0' COMMENT '品牌id',
  `sex` tinyint(3) unsigned NOT NULL DEFAULT '0' COMMENT '性别',
  `type` tinyint(3) unsigned NOT NULL COMMENT '折扣方式。1,折扣，2：价格',
  `discount` smallint(5) unsigned NOT NULL DEFAULT '0' COMMENT '折扣值，折扣*100',
  `price` decimal(10,2) NOT NULL DEFAULT '0.00' COMMENT '折扣价格',
  `start_time` datetime DEFAULT NULL COMMENT '开始时间',
  `end_time` datetime DEFAULT NULL COMMENT '结束时间',
  `last_edit` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT '最后更新时间',
  PRIMARY KEY (`id`),
  UNIQUE KEY `all_type` (`mall_id`,`major_type`,`minor_type`,`brand_id`,`sex`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `goods`
--

DROP TABLE IF EXISTS `goods`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `goods` (
  `gid` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT '商品id',
  `mall_id` int(10) unsigned DEFAULT NULL COMMENT '商场id',
  `major_type` mediumint(8) unsigned DEFAULT NULL COMMENT '主类别',
  `minor_type` mediumint(8) unsigned DEFAULT NULL COMMENT '从类别',
  `sex` tinyint(3) unsigned DEFAULT NULL COMMENT '性别',
  `brand_id` mediumint(8) unsigned DEFAULT NULL COMMENT '品牌id',
  `price` decimal(10,2) unsigned NOT NULL COMMENT '价格',
  PRIMARY KEY (`gid`),
  KEY `gid` (`gid`),
  KEY `all_type` (`mall_id`,`major_type`,`minor_type`,`sex`,`brand_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-01-14 11:46:07
