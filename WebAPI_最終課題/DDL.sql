create database accountbook;

drop table if EXISTS accountbooks;

create table accountbooks(
    id INT NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    payment INT,
    price INT NOT NULL,
    PRIMARY KEY (id)
)