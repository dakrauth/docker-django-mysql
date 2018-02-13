#!/bin/bash
python app.py migrate
python app.py runserver 0:80
echo Running Django on the local host at http://localhost:9000
