DROP TABLE IF EXISTS accounts;

PRAGMA foreign_keys = ON;

CREATE TABLE accounts (
    id INTEGER UNIQUE PRIMARY KEY,
    email TEXT UNIQUE,
    username TEXT UNIQUE,
    password_hash TEXT,
    authority INTEGER
);

CREATE TABLE lamps (
    lamp_id INTEGER PRIMARY KEY,
    authority INTEGER,
    lamp TEXT,
    FOREIGN KEY (authority) REFERENCES accounts(authority)
);