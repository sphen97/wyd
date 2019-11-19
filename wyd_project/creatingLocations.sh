#!/bin/bash

echo "creating locations"

python3 manage.py shell -c "from event.models import Location; Location.objects.create(name='Student Union', description='The University of Central Florida is a state university in Orlando, Florida. It has more students enrolled on campus than any other U.S. university. Founded in 1963 by the Florida Legislature, UCF opened in 1968 as Florida Technological University, with the mission of providing personnel to support the growing U.S. space program at the Kennedy Space Center and Cape Canaveral Air Force Station on Florida\'s Space Coast. As the school\'s academic scope expanded beyond engineering and technology, Florida Tech was renamed The University of Central Florida in 1978. UCF\'s space roots continue, as it leads the NASA Florida Space Grant Consortium. Initial enrollment was 1,948 students; enrollment today exceeds 66,000 students from 157 countries, all 50 states and Washington, D.C.')"

python3 manage.py shell -c "from event.models import Location; Location.objects.create(name='Test', description='Test Description')"
