CREATE DATABASE IF NOT EXISTS color_repo;

USE color_repo;

CREATE TABLE IF NOT EXISTS colors (
    color_id int(11) PRIMARY KEY AUTO_INCREMENT,
    created_at DATETIME,
    name VARCHAR(32),
    hex VARCHAR(6)
);

INSERT INTO colors (
    created_at,
    hex,
    name
) VALUES 
(NOW(), 'FF0000', 'red'),
(NOW(), '00FF00', 'green'),
(NOW(), '0000FF', 'blue');
