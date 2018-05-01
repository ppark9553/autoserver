#! /bin/bash

DB_ID=arbiter
DB_PW=makeitpopweAR!1

su -c "psql -c \"CREATE DATABASE $DB_ID;\"" postgres
su -c "psql -c \"CREATE USER $DB_ID WITH PASSWORD '$DB_PW';\"" postgres
su -c "psql -c \"ALTER ROLE $DB_ID SET client_encoding TO 'utf8';\"" postgres
su -c "psql -c \"ALTER ROLE $DB_ID SET default_transaction_isolation TO 'read committed';\"" postgres
su -c "psql -c \"ALTER ROLE $DB_ID SET timezone TO 'UTC';\"" postgres
su -c "psql -c \"GRANT ALL PRIVILEGES ON DATABASE $DB_ID TO $DB_ID;\"" postgres
