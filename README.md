----------------------------------------------------------------------
- Como realizar o Run Server em sua Maquina Local.

----------------------------------------------------------------------

Roteiro para rodar o Programa em Maquina Local usando  Ubuntu.

Este programa devera obrigatoriamente usar:

  -> python3.8.5 com todas as libs de desenvolvimento pre instaladas.

  -> postgres

----------------------------------------------------------------------
Primeiro Passo - Banco de Dados.

----------------------------------------------------------------------
  Criar o banco de dados resale no Postgres usando Linux Ubuntu.

  No Terminal...:

  1-sudo su postgres

  2-postgres@seucomputador:/home/seuusuario$ psql
  psql (12.6 (Ubuntu 12.6-0ubuntu0.20.04.1))

  3-postgres=# create database resale;
  CREATE DATABASE

  4-postgres=# \c resale
  You are now connected to database "resale" as user "postgres".

  5-resale=# create user resale with password 'resale';
  CREATE ROLE

  6-resale=# grant all privileges on database resale to resale;
  GRANT

  7-resale=# grant ALL on ALL tables in schema public to resale;
  GRANT

  8-resale=# grant all on ALL  sequences in schema public to resale;
  GRANT

  9-resale=# grant ALL on ALL functions in schema public to resale;
  GRANT

  10-resale=# create extension unaccent;
  CREATE EXTENSION

  11-resale=#\q

----------------------------------------------------------------------
Segundo Passo - O Repositorio.

----------------------------------------------------------------------

  Clonar o repositorio:
  
  git clone https://github.com/mlobf/TestDev.git

  No caso de algum imprevisto, o repositorio tambem estara disponivel via 
  google drive com o endereço compartilhado por email para d​iego@resale.com.br​.


----------------------------------------------------------------------

