DROP TABLE IF EXISTS accounts;

DROP TABLE IF EXISTS lampauthority;

PRAGMA foreign_keys = ON;

CREATE TABLE accounts (
    id INTEGER UNIQUE PRIMARY KEY,
    email TEXT UNIQUE,
    username TEXT UNIQUE,
    password_hash TEXT,
    authority INTEGER,
    FOREIGN KEY (authority) REFERENCES lampauthority(authority)
);

CREATE TABLE lampauthority (
    authority INTEGER PRIMARY KEY,
    lamp TEXT
);

INSERT INTO
    lampauthority(authority, lamp)
VALUES
    (4, 'GREEN,BLUE,YELLOW,RED'),
    (3, 'BLUE'),
    (2, 'YELLOW'),
    (1, 'RED');