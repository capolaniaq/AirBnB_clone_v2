-- Prepares a MySQL server for the project.
-- Creates a "hbnb_dev_db" database.

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
SET PASSWORD FOR 'hbnb_test'@'localhost' = PASSWORD('hbnb_test_pwd');
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
FLUSH PRIVILEGES;
