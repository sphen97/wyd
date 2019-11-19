#!/bin/bash

echo "creating super user"
python3 manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'cmortus@knights.ucf.edu', 'adminpass')"
