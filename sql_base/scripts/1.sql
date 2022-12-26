insert INTO publishing_house (name)
VALUES ('Речь');
insert INTO publishing_house (name)
VALUES ('Росмэн');
insert INTO publishing_house (name)
VALUES ('Стрекоза');
insert INTO publishing_house (name)
VALUES ('Эксмо');


insert INTO reader (name, surname, phone, address, login, password)
VALUES ('Богдан', 'Иванов', 88883467170,'Москва', '1', '1');
insert INTO reader (name, surname, phone, address, login, password)
VALUES ('Борис', 'Столяров', 88883467171,'Москва', '2', '2');
insert INTO reader (name, surname, phone, address, login, password)
VALUES ('Надежда', 'Кудряшова', 88883467172,'Волгоград', '3', '3');
insert INTO reader (name, surname, phone, address, login, password)
VALUES ('Богдан', 'Козлов', 88883467173,'Краснодар', '4', '4');



insert INTO author  (name, surname,born_year, dead_year)
VALUES ('Рэй', 'Брэдбери', 1920, 2012);
insert INTO  author (name, surname, born_year, dead_year)
VALUES ('Михаил', 'Шолохов', 1905, 1984);
insert INTO  author (name, surname,born_year, dead_year)
VALUES ('Шарлотта', 'Бронте', 1816, 1855);
insert INTO  author (name, surname,born_year, dead_year)
VALUES ('Луиза', 'Олкотт', 1832, 1888);


insert INTO book  (name, author_id, year, page_count, publishing_house_id)
VALUES ('Канун для всех святых', 1, 2022, 192, 1);
insert INTO  book (name, author_id, year, page_count, publishing_house_id)
VALUES ('Тихий дон', 2, 2022, 2176, 2);
insert INTO  book (name, author_id, year, page_count, publishing_house_id)
VALUES ('Джейн Эйр', 3, 2022, 624, 3);
insert INTO  book (name, author_id, year, page_count, publishing_house_id)
VALUES ('Маленькие женщины', 4, 2020, 320, 4);


insert INTO extradition_duration (date_start, date_end, book_id, reader_id)
VALUES ('2022-30-10', '2022-06-11', 2, 1);
insert INTO extradition_duration (date_start, date_end, book_id, reader_id)
VALUES ('2022-31-10', '2022-07-11', 3, 2);
insert INTO extradition_duration (date_start, date_end, book_id, reader_id)
VALUES ('2022-07-11', '2022-14-11', 1, 3);
insert INTO extradition_duration (date_start, date_end, book_id, reader_id)
VALUES ('2022-07-11', '2022-14-11', 4, 4);

insert INTO staff (name, surname, phone, post)
VALUES ('Илья', 'Филипов', 89994561220,'Администратор');
insert INTO staff (name, surname, phone, post)
VALUES ('Кристина', 'Соловьева', 89994561225,'Библиотекарь');
insert INTO staff (name, surname, phone, post)
VALUES ('Надежда', 'Брускова', 89994561226,'Библиотекарь');
insert INTO staff (name, surname, phone, post)
VALUES ('Светлана', 'Козлова', 89994561227,'Администратор');
