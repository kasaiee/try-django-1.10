
# try-django-1.10
Learn django 1.10 by create a blog site

installation
--------------------
- requirements:
 - python 2.7
  install following packages via **pip** or **easy_install**
 - `pip install django==1.10.2`
 - `pip install djangorestframework==3.5.2`
 - `pip install django-ckeditor==5.1.1`
 - `pip install wheel==0.24.0`
 - `pip install pillow==3.4.0`
- create database by typing `python manage.py migrate`
- run your server by typing `python manage.py runserver`

> **Note:**

> - You need to create an admin user to manage your blog site by this command: `python manage.py createsuperuser`

Create url: open teminal and type bellow url. Note that httpie must be installed.
'$ http -a admin:asdf@1234 [http://127.0.0.1:8000/api/create/](http://127.0.0.1:8000/api/create/) title='post 1' content='my content' owner=1'

'Delete url: open teminal and type bellow url.
$ http DELETE [http://127.0.0.1:8000/api/6/delete](http://127.0.0.1:8000/api/6/delete)'


#### Follow me
- [Github](https://github.com/kasaiee)
- [Telegram](https://telegram.me/pydeveloper2)
- [Aparat](http://www.aparat.com/kasaie)
- [Linkedin](https://www.linkedin.com/in/kasaiee)
