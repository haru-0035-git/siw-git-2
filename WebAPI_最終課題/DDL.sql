-- Active: 1699190975827@@127.0.0.1@3306
create database accountbook;

use accountbook

drop table if EXISTS accountbooks;

create table accountbooks(
    id INT NOT NULL AUTO_INCREMENT,
    date DATE NOT NULL,
    bop INT NOT NULL,
    breakdown VARCHAR(100) NOT NULL,
    price INT NOT NULL,
    PRIMARY KEY (id)
)

--insert文
INSERT INTO accountbooks (date, bop, breakdown, price) VALUES
('2024-01-01', 1, '給料', 300000),
('2024-01-02', 2, '家賃', 80000),
('2024-01-03', 2, '光熱費', 10000),
('2024-01-04', 2, '食料品', 20000),
('2024-01-05', 1, '副業収入', 50000),
('2024-01-06', 2, '交通費', 5000),
('2024-01-07', 2, '娯楽費', 15000),
('2024-01-08', 1, '投資利益', 40000),
('2024-01-09', 2, '医療費', 10000);
