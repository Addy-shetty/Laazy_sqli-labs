-- Common tables for all CVEs
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    is_admin BOOLEAN
);

CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price DECIMAL(10,2)
);

CREATE TABLE IF NOT EXISTS projects (
    id SERIAL PRIMARY KEY,
    project VARCHAR(100),
    owner VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS contacts (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100)
);

-- Sample data
INSERT INTO users (username, password, is_admin) VALUES 
('admin', 'admin123', true),
('user1', 'password1', false);

INSERT INTO products (name, price) VALUES
('Product A', 19.99),
('Product B', 29.99);

INSERT INTO projects (project, owner) VALUES
('Project X', 'admin'),
('Project Y', 'user1');

INSERT INTO contacts (name, email) VALUES
('John Doe', 'john@example.com'),
('Jane Smith', 'jane@example.com');
