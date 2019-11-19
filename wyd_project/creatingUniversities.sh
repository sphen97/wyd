#!/bin/bash

echo "creating universitys"

python3 manage.py shell -c "from university.models import University; University.objects.create(name='UCF', description='UCF', population=10000, domain='ucf.edu')"
python3 manage.py shell -c "from university.models import University; University.objects.create(name='gmail', description='gmail', population=10000, domain='gmail.com')"
