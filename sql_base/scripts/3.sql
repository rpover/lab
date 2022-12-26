PRAGMA foreign_keys=FALSE;
DROP TABLE if exists publishing_house;
CREATE TABLE publishing_house (
id INTEGER  PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL);

DROP TABLE if EXISTS reader;
CREATE TABLE reader (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
surname TEXT NOT NULL,
phone INTEGER UNIQUE,
address TEXT NOT NULL,
login TEXT NOT NULL,
password TEXT NOT NULL);

DROP TABLE if exists author;
CREATE TABLE author (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
surname TEXT NOT NULL,
born_year TEXT NOT NULL, 
dead_year TEXT);

DROP TABLE if exists book;
CREATE TABLE book (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
author_id INTEGER NOT NULL,
year TEXT NOT NULL,
page_count INTEGER NOT NULL,
publishing_house_id INTEGER NOT NULL,
FOREIGN KEY (author_id) REFERENCES author(id),
FOREIGN KEY (publishing_house_id) REFERENCES publishing_house(id));

DROP TABLE if EXISTS extradition_duration;
CREATE TABLE extradition_duration (
id INTEGER PRIMARY KEY AUTOINCREMENT,
date_start TEXT NOT NULL,
date_end TEXT NOT NULL,
book_id INTEGER NOT NULL,
reader_id INTEGER NOT NULL,
FOREIGN KEY (book_id) REFERENCES book(id),
FOREIGN KEY (reader_id) REFERENCES reader(id));

DROP TABLE if EXISTS staff;
CREATE TABLE staff (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
surname TEXT NOT NULL,
phone INTEGER UNIQUE,
post TEXT NOT NULL);