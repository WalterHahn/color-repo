CREATE DATABASE IF NOT EXISTS color_repo;

USE color_repo;

CREATE TABLE IF NOT EXISTS colors (
    color_id int(11) PRIMARY KEY AUTO_INCREMENT,
    created_at DATETIME,
    name VARCHAR(32),
    hex VARCHAR(6)
);
