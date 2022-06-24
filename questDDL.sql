create database Assessment;

use Assessment;

CREATE TABLE User_Table (
  user_id int NOT NULL AUTO_INCREMENT,
  student_id int,
  First_Name varchar(255),
  Last_Name varchar(255) NOT NULL,
  Email varchar(255),
  Registered_On timestamp DEFAULT CURRENT_TIMESTAMP,
  Degree varchar(255),
  Country varchar(255),
  PRIMARY KEY (user_id),
);

CREATE TABLE Questions_Table (
  quest_id int NOT NULL AUTO_INCREMENT,
  topic varchar(255),
  difficulty int,
  Created_on timestamp DEFAULT CURRENT_TIMESTAMP,
  Content varchar(255),
  PRIMARY KEY (quest_id),
);

CREATE TABLE Course_Table (
  course_id int NOT NULL AUTO_INCREMENT,
  course_number int,
  topic varchar(255),
  quantity int,
  summary varchar(255),
  PRIMARY KEY (course_id),
  FOREIGN KEY (topic) REFERENCES Questions_Table(topic),
);

CREATE TABLE Options_Table (
  options_id int NOT NULL AUTO_INCREMENT,
  quest_id int,
  is_correct boolean,
  created_on timestamp DEFAULT CURRENT_TIMESTAMP,
  Content varchar(255),
  PRIMARY KEY (options_id),
  FOREIGN KEY (quest_id) REFERENCES Questions_Table(quest_id),
);

CREATE TABLE Results Table (
  results_id int NOT NULL AUTO_INCREMENT,
  quest_id int,
  options_id int,
  course_id int,
  user_id int,
  attempt_id int,
  grouping_id int,
  taken_on timestamp DEFAULT CURRENT_TIMESTAMP,
  expiration datetime DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (results_id),
  FOREIGN KEY (user_id) REFERENCES User_Table(user_id),
  FOREIGN KEY (options_id) REFERENCES Options_Table(options_id),
  FOREIGN KEY (quest_id) REFERENCES Questions_Table(quest_id),
  FOREIGN KEY (course_id) REFERENCES Course_Table(course_id),
);

