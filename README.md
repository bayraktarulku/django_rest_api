# Django application example

## Project setup
```
mkdir tutorial
sudo apt-get install python3-venv
python3 -m venv nv env
source env/bin/activate
pip install django
pip install djangorestframework
```

### Running the server
```
django-admin startproject tutorial
django-admin startapp quickstart
pwd
find .
python manage.py migrate
```

### Creating user on the DB Server
```
python manage.py createsuperuser --email admin@example.com --username admin
```

### Curl Request Examples
```
curl -H 'Accept: application/json; indent=4' -u admin:password123 http://127.0.0.1:8000/users/
```
