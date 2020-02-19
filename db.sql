/*
SQLyog Community v13.0.1 (64 bit)
MySQL - 5.1.32-community : Database - chatbot
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`chatbot` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `chatbot`;

/*Table structure for table `college` */

DROP TABLE IF EXISTS `college`;

CREATE TABLE `college` (
  `clg_id` int(11) NOT NULL AUTO_INCREMENT,
  `clg_name` varchar(30) NOT NULL,
  `location` varchar(20) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(30) NOT NULL,
  PRIMARY KEY (`clg_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `college` */

insert  into `college`(`clg_id`,`clg_name`,`location`,`phone`,`email`) values 
(1,'nss manjeri','manjeri',999988877,'nssmanjeri@gmail.com'),
(2,'ccit manjeri','manjeri',9876543210,'mji@gmail.com'),
(3,'ccsit calicut','calicut',9087654321,'ccsitcl@gmail.com'),
(4,'cas vazhakkad','vazhakkad',8790654321,'casvzk@gmail.com'),
(7,'cas calicut','calicut',7098654321,'casclt@gmail.com'),
(9,'ccsit vadakara','vadakara',8097654321,'ccsitvd@gmail.com');

/*Table structure for table `college_course` */

DROP TABLE IF EXISTS `college_course`;

CREATE TABLE `college_course` (
  `ccid` int(11) NOT NULL AUTO_INCREMENT,
  `clg_id` int(11) NOT NULL,
  `course_id` int(11) NOT NULL,
  `fee` int(11) NOT NULL,
  PRIMARY KEY (`ccid`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `college_course` */

insert  into `college_course`(`ccid`,`clg_id`,`course_id`,`fee`) values 
(1,1,1,18000),
(2,2,1,18500),
(6,2,7,20000);

/*Table structure for table `course` */

DROP TABLE IF EXISTS `course`;

CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `cname` varchar(30) NOT NULL,
  `dept_id` int(11) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `syllabus` varchar(300) NOT NULL,
  `status` varchar(20) NOT NULL,
  PRIMARY KEY (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `course` */

insert  into `course`(`course_id`,`cname`,`dept_id`,`duration`,`syllabus`,`status`) values 
(1,'msc computer science',2,'2','20200115_114243_UNIVERSITY_CHATBOT_2.pdf','approved'),
(7,'mca',2,'3','20200115_114224_UNIVERSITY_CHATBOT_2.pdf','approved');

/*Table structure for table `dataset` */

DROP TABLE IF EXISTS `dataset`;

CREATE TABLE `dataset` (
  `qtn_id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(500) DEFAULT NULL,
  `answer` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`qtn_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `dataset` */

insert  into `dataset`(`qtn_id`,`question`,`answer`) values 
(1,'hello','hai'),
(2,'can u help me','yes'),
(3,'exam shedule','time table'),
(4,'course fee','fee'),
(5,NULL,NULL);

/*Table structure for table `department` */

DROP TABLE IF EXISTS `department`;

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL AUTO_INCREMENT,
  `depart_name` varchar(20) NOT NULL,
  `head` varchar(20) DEFAULT NULL,
  `address` varchar(30) DEFAULT NULL,
  `cont_no` bigint(20) NOT NULL,
  `email` varchar(20) DEFAULT NULL,
  `lid` int(11) NOT NULL,
  PRIMARY KEY (`dept_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;

/*Data for the table `department` */

insert  into `department`(`dept_id`,`depart_name`,`head`,`address`,`cont_no`,`email`,`lid`) values 
(1,'computer science',NULL,NULL,9876543210,NULL,2),
(2,'commerce',NULL,NULL,90876543,NULL,7),
(3,'sddds',NULL,NULL,9876543210,NULL,8);

/*Table structure for table `doubt` */

DROP TABLE IF EXISTS `doubt`;

CREATE TABLE `doubt` (
  `dbid` int(11) NOT NULL AUTO_INCREMENT,
  `doubt` text NOT NULL,
  `st_id` int(11) NOT NULL,
  `reply` text,
  `date` date DEFAULT NULL,
  PRIMARY KEY (`dbid`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

/*Data for the table `doubt` */

insert  into `doubt`(`dbid`,`doubt`,`st_id`,`reply`,`date`) values 
(1,'hello',4,NULL,NULL),
(2,'hello',4,'hai',NULL),
(3,'hello',4,'hai',NULL),
(4,'hello',4,'hai',NULL),
(5,'hello',4,'hai',NULL),
(6,'hello',4,'hai',NULL),
(7,'hello',4,'hai',NULL),
(8,'hello',4,'hai',NULL),
(9,'hello',4,'hai',NULL),
(10,'hello',4,'hai',NULL),
(11,'hello',4,'hai',NULL),
(12,'can u help me',4,'yes',NULL),
(13,'can u help me',4,'yes',NULL),
(14,'can u help me',4,'yes',NULL),
(15,'can u help me',4,'yes',NULL),
(16,'hello ',4,'hai',NULL),
(17,'hello ',4,'hai',NULL),
(18,'can you help me ',4,'yes',NULL),
(19,'can you help me ',4,'yes',NULL);

/*Table structure for table `exam` */

DROP TABLE IF EXISTS `exam`;

CREATE TABLE `exam` (
  `exid` int(11) NOT NULL AUTO_INCREMENT,
  `exam_noti` varchar(300) NOT NULL,
  `date` date NOT NULL,
  `course_id` int(11) NOT NULL,
  `time_table` varchar(500) NOT NULL,
  PRIMARY KEY (`exid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `exam` */

insert  into `exam`(`exid`,`exam_noti`,`date`,`course_id`,`time_table`) values 
(1,'mcs','2020-01-06',1,'msc'),
(5,'3rd sem exam','2020-01-15',1,'20200116_120155_TABLES.docx');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `lid` int(11) NOT NULL AUTO_INCREMENT,
  `lname` varchar(20) NOT NULL,
  `password` varchar(30) NOT NULL,
  `type` varchar(30) NOT NULL,
  PRIMARY KEY (`lid`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`lid`,`lname`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'cucs001','cs001','dept'),
(3,'stud','stud','student'),
(4,'anu','anu','student'),
(5,'joy','joy','student'),
(7,'cm','cm','dept'),
(8,'sd','sd','dept'),
(9,'sharath','sharath005','pending');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `not_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(500) NOT NULL,
  `date` date NOT NULL,
  `course_id` int(11) NOT NULL,
  PRIMARY KEY (`not_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`not_id`,`notification`,`date`,`course_id`) values 
(1,'time table','2020-01-05',1),
(2,'gff','2020-01-15',1);

/*Table structure for table `response` */

DROP TABLE IF EXISTS `response`;

CREATE TABLE `response` (
  `rs_id` int(11) NOT NULL AUTO_INCREMENT,
  `response` varchar(100) NOT NULL,
  `db_id` int(11) NOT NULL,
  PRIMARY KEY (`rs_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `response` */

insert  into `response`(`rs_id`,`response`,`db_id`) values 
(1,'hai',1);

/*Table structure for table `result` */

DROP TABLE IF EXISTS `result`;

CREATE TABLE `result` (
  `reslid` int(11) NOT NULL AUTO_INCREMENT,
  `reg_no` varchar(20) NOT NULL,
  `exid` int(11) NOT NULL,
  `stresult` varchar(500) NOT NULL,
  PRIMARY KEY (`reslid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `result` */

insert  into `result`(`reslid`,`reg_no`,`exid`,`stresult`) values 
(1,'msc009',5,'20200116_121234_JAVA_PROGRAMS.docx');

/*Table structure for table `student` */

DROP TABLE IF EXISTS `student`;

CREATE TABLE `student` (
  `st_id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(20) NOT NULL,
  `last_name` varchar(20) NOT NULL,
  `dob` date NOT NULL,
  `place` varchar(30) NOT NULL,
  `district` varchar(30) NOT NULL,
  `pin` int(11) NOT NULL,
  `gender` varchar(20) NOT NULL,
  `phone` bigint(20) NOT NULL,
  `email` varchar(20) NOT NULL,
  `clg_id` int(11) DEFAULT NULL,
  `course_id` int(11) DEFAULT NULL,
  `regno` varchar(20) DEFAULT NULL,
  `sem` int(11) DEFAULT NULL,
  PRIMARY KEY (`st_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;

/*Data for the table `student` */

insert  into `student`(`st_id`,`first_name`,`last_name`,`dob`,`place`,`district`,`pin`,`gender`,`phone`,`email`,`clg_id`,`course_id`,`regno`,`sem`) values 
(3,'shanvi','k','2018-08-05','pulikkal','malappuram',673637,'female',90999888,'shanvi@gmail.com',1,1,'msc009',3),
(4,'Alen','p','2018-10-14','neerad','malappuram',673638,'male',99998887,'alen@gmail.com',1,1,'msc007',2),
(5,'joy','k','2019-12-01','clt','kannur',673645,'male',9998877,'joy@gmail.com',2,1,'msc003',4),
(6,'sharath','k','1998-01-26','aroor','Malappuram',673638,'Male',8606278795,'sharath@gmail.com ',2,1,'CWAPSCS004',2),
(7,'sharath','k','1998-01-26','aroor','Malappuram',673638,'Male',8606278795,'sharath@gmail.com ',2,1,'CWAPSCS004',2);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
