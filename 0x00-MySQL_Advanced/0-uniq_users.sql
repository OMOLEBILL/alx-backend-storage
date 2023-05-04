-- we create a table users with uniques email
-- id is the priary key and not null
CREATE TABLE IF NOT EXISTS users (
	    id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	    email VARCHAR(255) UNIQUE NOT NULL,
	    name VARCHAR(255)
	);
