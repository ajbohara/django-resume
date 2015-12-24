# django-resume

This is a quick django project I whipped out to host my resume. Live Demo can be found here: URL.
This project requires

Installation
============

Asuming you have python 3 and git installed on your system.
Install Instructions:

Cloning the git repo:

`git clone https://github.com/ajbohara/django-resume.git`

Install and setup a virtual environment to run this project on:

`pip install venv`

`virtualenv -p python3 env`

`source env/bin/activate`

Install and setup requirements of the project:

`pip install -r requirements.txt`

Go to the project root and then run:

`python manage.py makemigrations`

`python manage.py migrate`

Usage
=====

Go ahead and create a superuser to login to your admin page:

`python manage.py createsuperuser`

`python manage.py runserver`

Remember that you will have to create a user profile from the admin page


