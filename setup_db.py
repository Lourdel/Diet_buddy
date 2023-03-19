-- setup test
CREATE DATABASE IF NOT EXISTS dietbud_dev_db;
CREATE USER IF NOT EXISTS 'dietbud_dev'@'localhost' IDENTIFIED BY 'dietbud_dev_pwd';
GRANT USAGE ON *.* TO 'dietbud_dev'@'localhost';
GRANT SELECT ON `performance_schema`.* TO 'dietbud_dev'@'localhost';
GRANT ALL PRIVILEGES ON `dietbud_dev_db`.* TO 'dietbud_dev'@'localhost';
