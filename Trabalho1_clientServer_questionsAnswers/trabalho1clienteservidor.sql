DROP DATABASE IF EXISTS `trabalho1clienteservidor`;
CREATE DATABASE IF NOT EXISTS `trabalho1clienteservidor`;
USE `trabalho1clienteservidor`;

drop table if exists `questions`;
create table if not exists questions (
   id int not null auto_increment primary key,
   question varchar(50),
   option1 varchar(30),
   option2 varchar(30),
   option3 varchar(30),
   option4 varchar(30),
   correct_answer int not null  

);
INSERT INTO questions (question, option1, option2, option3, option4, correct_answer) VALUES 
('Qual é a capital do Brasil?', 'A) São Paulo', 'B) Rio de Janeiro', 'C) Brasília', 'D) Salvador', '3'),
('Quem Descobriu o Brasil?', 'A) José de Abreu', 'B) Pedro 2', 'C) Cristovão Colombo', 'D) Pedro Alvarez Cabral', '4');
SELECT * FROM questions;