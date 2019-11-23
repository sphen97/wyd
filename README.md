# wyd
Database Systems - UCF Fall 2019 Term Project

## Team Members
- [Stephen Bennnett](https://github.com/sphen97)
- [Cameron Mortus](https://github.com/CamMortus)
- [Kenny Cheng](https://github.com/Chengalang)

## Recommended Process For Testing
in file '[creatingSuperUser.sh](https://github.com/sphen97/wyd/blob/master/wyd_project/creatingSuperUser.sh)' Fill in your email where the Your_Email_Here@test.com is currently
in the terminal bash run the '[resetServer.sh](https://github.com/sphen97/wyd/blob/master/wyd_project/resetServer.sh)' script
the first super admin is 'admin' with the pass word being 'adminpass'
a generic user is 'foo' with password is 'bar'

once server starts go to the provided local host address from terminal with /admin/ at the end of the adress from your browser
sign in using the admin credentials, and then go to profiles, click on admin, and selct a university for the super admin. click save and now your ready to go

at this point the sign in is at the address provided by the terminal 

## Requirements 
python 3 
pip installs and requirements listed in [requirements.txt](https://github.com/sphen97/wyd/blob/master/wyd_project/requirements.txt)

on some systems 
- [mostly linux you must sudo chmod 774 'bash scripts' look in hte main folder to find the list of files to do this for](https://github.com/sphen97/wyd/tree/master/wyd_project)
