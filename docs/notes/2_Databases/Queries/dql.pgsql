SELECT *
FROM products;

SELECT id AS products_id
FROM products;

-- Operators =, > , < , >= , <=, !=
SELECT * 
FROM products
WHERE id = 10;

-- Logical operators AND, OR, 
SELECT * 
FROM products
WHERE price > 20 AND is_sale != false;

-- IN
SELECT *
FROM products
WHERE id IN (1,2,3);

-- LIKE
SELECT * 
FROM products
WHERE name LIKE 'TV%';

-- ORDER BY ASC/DESC
SELECT *
FROM products
ORDER BY price DESC, created_at ;

-- LIMIT
SELECT *
FROM products
WHERE price > 10 
LIMIT 2;

-- OFFSET [LIMIT and OFFSET is used in pagination]
SELECT *
FROM products
WHERE price > 10 
LIMIT 2
OFFSET 2;





