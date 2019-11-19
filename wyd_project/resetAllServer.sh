#!/bin/bash
echo "welcome to the server"

#file cleanup
shopt -s extglob
rm db.sqlite3
cd event/migrations
rm -v -r !("__init__.py")
cd ../..
cd rso/migrations
rm -v -r !("__init__.py")
cd ../..
cd university/migrations
rm -v -r !("__init__.py")
cd ../..
cd users/migrations
rm -v -r !("__init__.py")
cd ../..

#migragtions
# echo "migrating"
# python3 manage.py makemigrations
# python3 manage.py migrate

# #university creation
# ./creatingUniversities.sh
# #super user creation
# ./creatingSuperUser.sh
# #user creation
# ./creatingUsers.sh
# #rso creation
# ./creatingRSOs.sh
# #event creation
# ./creatingEvents.sh
# #location creation
# ./creatingLocations.sh
# #start server
# echo "starting server"
# python3 manage.py runserver
