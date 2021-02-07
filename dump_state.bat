@echo off

docker exec -it django python manage.py dumpdata
