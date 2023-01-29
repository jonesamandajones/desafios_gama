-- Exercício de normalização

create database livraria;

create table inicio (
	nome varchar (20),
    endereco varchar (40),
    telefone integer,
    data_nascimento date,
    titulo varchar (15),
    autor varchar (20),
    numero_de_paginas integer,
    data_emprestimo date
);

select * from clientes;

create table clientes (
	id int primary key auto_increment,
    nome varchar (20),
    endereco int,
    telefone int,
    data_nascimento date
);
create table enderecos (
	id int primary key auto_increment,
    logradouro varchar (30),
    cidade varchar (20),
    estado varchar (2)
);
create table telefones (
	id int primary key auto_increment,
    principal int,
    celular int,
    recado int
);
create table catalogo (
	id int primary key auto_increment,
    titulo varchar (30),
    autor varchar (30),
    paginas int
);
create table emprestimos (
	id_cliente int,
    id_livro int,
    data_emprestimo date,
    foreign key (id_cliente) references clientes(id),
    foreign key (id_livro) references catalogo(id)
);
