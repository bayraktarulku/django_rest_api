=================
django-helloworld
=================

Installation
============
$ sudo apt update
$ sudo apt install python3-dev python3-pip python3-virtualenv sqlitebrowser
$ sudo pip install -r requirements.txt
$ python3 manage.py migrate

$ python3 manage.py createsuperuser --username admin --email admin@mail.com

At which point you should see:

::
    (8 character)
    Password:
    Password (again):

    Superuser created successfully.


Run application
===============

After which you can run::

    $ python3 manage.py runserver

Then, you can open the URL http://127.0.0.1:8000/ in your web browser

