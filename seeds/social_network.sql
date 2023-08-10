DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;


-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username text,
    email text
);


INSERT INTO users (username, email) VALUES ('Pixies', 'pixie@msn');
INSERT INTO users (username, email) VALUES ('Dixies', 'dixie@msn');
INSERT INTO users (username, email) VALUES ('Lixies', 'lixie@msn');
INSERT INTO users (username, email) VALUES ('Tixies', 'tixie@msn');

DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;

-- Then the table with the foreign key second.
CREATE SEQUENCE IF NOT EXISTS posts_id_seq;
CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text,
    content text,
    views int,
    user_id int
);



INSERT INTO posts (title, content, views, user_id) VALUES ('Title1', 'Content1', 2, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Title2', 'Content2', 5, 1);
INSERT INTO posts (title, content, views, user_id) VALUES ('Title3', 'Content3', 10, 2);
INSERT INTO posts (title, content, views, user_id) VALUES ('Title4', 'Content4', 15, 4);
INSERT INTO posts (title, content, views, user_id) VALUES ('Title4', 'Content5', 20, 4);
INSERT INTO posts (title, content, views, user_id) VALUES ('Title4', 'Content6', 25, 3);
INSERT INTO posts (title, content, views, user_id) VALUES ('Title4', 'Content7', 30, 2);
