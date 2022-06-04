CREATE DATABASE if not exists hiringSystem;
use hiringSystem;

create table  if not exists jobpost (
jobpostID INT(6) auto_increment primary key,
title varchar(255) NOT NULL,
jobtype varchar(255) NOT NULL,
description varchar(255) NOT NULL,
closeddate date NOT NULL,
postedDate date NOT NULL,
salaryFrom varchar(255) NOT NULL,
status1 varchar(255) NOT NULL,
experience varchar(255) NOT NULL
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




