/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;



CREATE DATABASE if not exists heroku_c7805820ef04b71;
use heroku_c7805820ef04b71;

create table  if not exists jobpost (
jobpostID INT(6) auto_increment primary key,
title varchar(255) NOT NULL,
jobtype varchar(255) NOT NULL,
description varchar(255) NOT NULL,
qualification varchar(255) NOT NULL,
category varchar(255) NOT NULL,
salaryFrom varchar(255) NOT NULL,
status1 varchar(255) NOT NULL,
experience varchar(255) NOT NULL,
postedDate date NOT NULL,
closeddate date NOT NULL,
salaryTo varchar(255) NOT NULL

);

create table if not exists user_account (
userID INT(6) auto_increment primary key,
fullName varchar(255) NOT NULL,
username varchar(255) NOT NULL,
email varchar(255) NOT NULL,
phoneNo varchar(255) NOT NULL,
password varchar(255) NOT NULL,
country varchar(255) NOT NULL
);

create table if not exists jobApply (
jobapplyID INT(6) auto_increment primary key,
jobpostID INT(6),
userID INT(6),
applicantStatus varchar(255) NOT NULL,
FOREIGN KEY (jobpostID) REFERENCES jobpost(jobpostID)
ON DELETE CASCADE
ON UPDATE CASCADE,
FOREIGN KEY (userID) REFERENCES user_account(userID)
ON DELETE CASCADE
ON UPDATE CASCADE,
date date NOT NULL
);

