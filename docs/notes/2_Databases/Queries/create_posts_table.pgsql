CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NUll, 
    content VARCHAR NOT NULL
);

INSERT INTO posts (title, content) VALUES 
('title of post 1', 'content of post 1'),
('title of post 2', 'content of post 2');

SELECT * FROM posts;

ALTER TABLE posts
    ADD COLUMN published BOOLEAN, 
    ADD COLUMN created_at TIMESTAMP DEFAULT NOW();

ALTER COLUMN posts
    ALTER COLUMN published SET DEFAULT TRUE;