#!/bin/bash

echo "creating users"

python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo', password='bar', is_superuser=False, is_staff=False, email='c@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo1', password='bar', is_superuser=False, is_staff=False, email='c@gmail.com')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo2', password='bar', is_superuser=False, is_staff=False, email='c2@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo3', password='bar', is_superuser=False, is_staff=False, email='c3@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo4', password='bar', is_superuser=False, is_staff=False, email='c4@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo5', password='bar', is_superuser=False, is_staff=False, email='c5@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo6', password='bar', is_superuser=False, is_staff=False, email='c6@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo7', password='bar', is_superuser=False, is_staff=False, email='c7@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo8', password='bar', is_superuser=False, is_staff=False, email='c8@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo9', password='bar', is_superuser=False, is_staff=False, email='c9@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo10', password='bar', is_superuser=False, is_staff=False, email='c10@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo11', password='bar', is_superuser=False, is_staff=False, email='c11@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo12', password='bar', is_superuser=False, is_staff=False, email='c12@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo13', password='bar', is_superuser=False, is_staff=False, email='c13@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo14', password='bar', is_superuser=False, is_staff=False, email='c14@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo15', password='bar', is_superuser=False, is_staff=False, email='c15@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo16', password='bar', is_superuser=False, is_staff=False, email='c16@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo17', password='bar', is_superuser=False, is_staff=False, email='c7@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo18', password='bar', is_superuser=False, is_staff=False, email='c18@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo19', password='bar', is_superuser=False, is_staff=False, email='c19@knights.ucf.edu')"
python3 manage.py shell -c "from django.contrib.auth.models import User; user=User.objects.create_user('foo20', password='bar', is_superuser=False, is_staff=False, email='c20@knights.ucf.edu')"