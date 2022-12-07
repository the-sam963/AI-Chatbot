-- create table greeting(
-- id BIGINT(8) PRIMARY KEY AUTO_INCREMENT,
-- tag CHAR(8) DEFAULT 'greeting',
-- pattern VARCHAR(100),
-- response VARCHAR(100)
-- );


-- INSERT INTO greeting ('pattern', 'response') VALUES ('hi', 'hi');


-- INSERT INTO greeting (pattern, response) 
-- VALUES 
--     ('Hey', '');



create table name(
id BIGINT(8) PRIMARY KEY AUTO_INCREMENT,
tag CHAR(8) DEFAULT 'name',
pattern VARCHAR(100),
response VARCHAR(100)
);


-- INSERT INTO name ('pattern', 'response') VALUES ('hi', 'hi');


INSERT INTO name (pattern, response) 
VALUES 
    ('what is your name', 'my name is _name_'),
    ('what can I call you', 'you can call me _name_'),
    ('who are you', "I'm _name_"),
    ('name', '_name_');