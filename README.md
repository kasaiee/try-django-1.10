# try-django-1.10
Learn django 1.10 by create a blog site

installation
--------------------
- requirements:
 - python 2.7
  install following packages via **pip** or **easy_install**
 - `pip install django==1.10.2`
 - `pip install djangorestframework==3.5.2`
 - `pip install django-filter==1.0.1`
 - `pip install django-crispy-forms==1.6.1`
 - `pip install django-ckeditor==5.1.1`
 - `pip install wheel==0.24.0`
 - `pip install pillow==3.4.0`
- create database by typing `python manage.py migrate`
- run your server by typing `python manage.py runserver`

> **Note:**

> - You need to create an admin user to manage your blog site by this command: `python manage.py createsuperuser`

Create url: open teminal and type this url. Note that httpie must be installed.

`$ http -a <USERNAME>:<PASSWORD> http://127.0.0.1:8000/api/create/ title='<YOUR_TITLE>' content='<YOUR_CONTENT>' owner=<OWNER_ID>`

Delete url: open teminal and type this url.

`$ http -a <USERNAME>:<PASSWORD> DELETE http://127.0.0.1:8000/api/<POST_ID>/delete`

Update url: open teminal and type this url.

`$ http -a <USERNAME>:<PASSWORD> PUT http://127.0.0.1:8000/api/<POST_ID>/edit title='<YOUR_TITLE>' content='<YOUR_CONTENT>' owner=<OWNER_ID>``




#### Follow me
- [Github](https://github.com/kasaiee)
- [Telegram](https://telegram.me/pydeveloper2)
- [Aparat](http://www.aparat.com/kasaie)
- [Linkedin](https://www.linkedin.com/in/kasaiee)
