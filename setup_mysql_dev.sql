-- Prepares a MySQL server for the project.
-- Creates a "hbnb_dev_db" database.

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
SET PASSWORD FOR 'hbnb_dev'@'localhost' = PASSWORD('hbnb_dev_pwd');
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;
