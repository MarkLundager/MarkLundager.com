DROP TABLE IF EXISTS accounts;

PRAGMA foreign_keys = ON;

CREATE TABLE accounts (
    id INTEGER UNIQUE,
    email TEXT UNIQUE,
    username TEXT UNIQUE,
    password_hash TEXT,
    authority INTEGER,
    PRIMARY KEY (id)
);