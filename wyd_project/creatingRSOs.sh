#!/bin/bash

echo "creating RSOs"

python3 manage.py shell -c "from rso.models import RSO; from django.contrib.auth.models import User; from university.models import University; RSO.objects.create(admin=User.objects.all().get(id=1),name='Test1',description='TestData',approved=True, university=University.objects.all().get(id=1));
RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=1)); RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=2)); RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=3)); RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=4)); RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=5));"

python3 manage.py shell -c "from rso.models import RSO; from django.contrib.auth.models import User; from university.models import University; RSO.objects.create(admin=User.objects.all().get(id=2),name='Test2',description='TestData',approved=True, university=University.objects.all().get(id=1)); RSO.objects.all().get(id=2).members.add(User.objects.all().get(id=6));
RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=2)); RSO.objects.all().get(id=2).members.add(User.objects.all().get(id=8)); RSO.objects.all().get(id=2).members.add(User.objects.all().get(id=9)); RSO.objects.all().get(id=2).members.add(User.objects.all().get(id=7));"

python3 manage.py shell -c "from rso.models import RSO; from django.contrib.auth.models import User; from university.models import University; RSO.objects.create(admin=User.objects.all().get(id=3),name='Test3',description='TestData',approved=True, university=University.objects.all().get(id=1)); RSO.objects.all().get(id=3).members.add(User.objects.all().get(id=10));
RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=3)); RSO.objects.all().get(id=3).members.add(User.objects.all().get(id=11)); RSO.objects.all().get(id=3).members.add(User.objects.all().get(id=12)); RSO.objects.all().get(id=3).members.add(User.objects.all().get(id=13));"

python3 manage.py shell -c "from rso.models import RSO; from django.contrib.auth.models import User; from university.models import University; RSO.objects.create(admin=User.objects.all().get(id=10),name='Test4',description='TestData',approved=True, university=University.objects.all().get(id=1)); RSO.objects.all().get(id=4).members.add(User.objects.all().get(id=14));
RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=10)); RSO.objects.all().get(id=4).members.add(User.objects.all().get(id=15)); RSO.objects.all().get(id=4).members.add(User.objects.all().get(id=16)); RSO.objects.all().get(id=4).members.add(User.objects.all().get(id=17));"

python3 manage.py shell -c "from rso.models import RSO; from django.contrib.auth.models import User; from university.models import University; RSO.objects.create(admin=User.objects.all().get(id=15),name='Test5',description='TestData',approved=True, university=University.objects.all().get(id=1)); RSO.objects.all().get(id=5).members.add(User.objects.all().get(id=18));
RSO.objects.all().get(id=1).members.add(User.objects.all().get(id=15)); RSO.objects.all().get(id=5).members.add(User.objects.all().get(id=19)); RSO.objects.all().get(id=5).members.add(User.objects.all().get(id=20)); RSO.objects.all().get(id=5).members.add(User.objects.all().get(id=1));"
