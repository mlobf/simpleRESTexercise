
Criar o banco de dados resale no Postgres usando Linux Ubuntu.

postgres@seucomputador:/home/seuusuario$ psql
psql (12.6 (Ubuntu 12.6-0ubuntu0.20.04.1))

postgres=# create database resale;
CREATE DATABASE
postgres=# \c resale
You are now connected to database "resale" as user "postgres".
resale=# create user resale with password 'resale';
CREATE ROLE
resale=# grant all privileges on database resale to resale;
GRANT
resale=# grant ALL on ALL tables in schema public to resale;
GRANT
resale=# grant all on ALL  sequences in schema public to resale;
GRANT
resale=# grant ALL on ALL functions in schema public to resale;
GRANT
resale=# create extension unaccent;
CREATE EXTENSION
resale=#\q

