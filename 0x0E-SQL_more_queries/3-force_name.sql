-- Create a table called force_name
-- Should not fail if table doesnt exist and name cant be NULL
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);