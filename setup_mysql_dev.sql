-- script that prepares a MySQL server for the project:
-- Privileges for new user (hbnb_test)

CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the hbnb_dev user if it doesn't already exist
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost';

-- Set password for the user hbnb_dev
SET PASSWORD FOR 'hbnb_dev'@'localhost' = 'hbnb_dev_pwd';
USE hbnb_dev_db;

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Flush the privileges
FLUSH PRIVILEGES;


