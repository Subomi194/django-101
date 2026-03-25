#django-admin startproject taskproject
#python manage.py runserver
#python manage.py startapp tasks - to create a python app
#python manage.py makemigrations - to make a migrations
#python manage.py migrate - to apply migration to database
#python manage.py createsuperuser - to create superuser from admin.py

#python manage.py changepassword [what your username is] -- to change admin password

#python manage.py shell - if you forgot username

#NEW CODE TO CHANGE SUPER_USER DETAILS: -- will override username and password
from django.contrib.auth.models import User
user = User.objects.get(username = 'admin')
user.set_password('newpassword')
user.save()

#CLASS 4:
#create url for task

#ready made form - from django.contrib.auth.forms import UserCreationForm

#csrf - anybody that is not coming from the site, kill it - cross site request forgery

#decorator for login protection - @login_required

#admin123 - superuserpassword