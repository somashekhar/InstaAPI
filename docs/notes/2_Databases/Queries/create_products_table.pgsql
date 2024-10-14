-- Create a products table
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

/* Add a new column is_sale with default value false*/
ALTER TABLE products
ADD COLUMN is_sale BOOLEAN DEFAULT FALSE;

/* Add inventory column. If there is no default values then it fails!! */
ALTER TABLE products
ADD COLUMN inventory INT NOT NULL;

-- Add created at
ALTER TABLE products
ADD COLUMN created_at TIMESTAMP DEFAULT NOW();

-- Get products 
SELECT * 
FROM products
ORDER BY id ASC;

/* Add rows */
INSERT INTO products (name, price) VALUES
('TV', 200),
('DVD Player', 80),
('remote', 10),
('microphone', 30),
('Car', 40),
('pencil', 2),
('keyboard', 28),
('toilet paper', 4);

-- returning 
INSERT INTO products(name, price, is_sale) VALUES
('pencil sharpner', 4, true),
('soda', 2, true),
('pizza', 13, true),
('toothbrush', 2, true),
('xbox', 380, true)
returning;

-- DELETE data from table
DELETE FROM products
WHERE id = 10
RETURNING * ;

-- UPDATE data in table
UPDATE products
SET name = 'flower totitla', price = 40 
WHERE id = 25
RETURNING *;
