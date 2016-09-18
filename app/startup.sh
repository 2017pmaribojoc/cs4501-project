#!/bin/bash
python /app/webapp/manage.py makemigrations
python /app/webapp/manage.py migrate
python /app/webapp/manage.py loaddata db.json
mod_wsgi-express start-server --working-directory /app/webapp  --reload-on-changes /app/webapp/webapp/wsgi.py
