CREATE DATABASE IF NOT EXISTS db;
USE db;

SET auto_increment_increment = 2;

CREATE TABLE IF NOT EXISTS id_test (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT
);

ALTER TABLE id_test AUTO_INCREMENT = 3001;