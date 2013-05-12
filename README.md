# Django project layout template

## Introduction

This project layout is based on the following links:

* [http://stackoverflow.com/questions/11216829/django-directory-structure](http://stackoverflow.com/questions/11216829/django-directory-structure)
* [https://github.com/twoscoops/django-twoscoops-project](https://github.com/twoscoops/django-twoscoops-project)

There are some changes:

### Split models.py and views.py into several files.

To establish new model, for example, UploadFile, you can create new file named
`upload_file.py` in `models` directory:

example_app/models/upload_file.py

```python
from django.db import models

class UploadFile(models.Model):
    pass  # Add fields here

    class Meta:
        app_label = 'example_app'  # The prefix of sheet name for database
```

Then you need to edit `models/__init__.py`, and add the following contents:

```python
from example_app.models.upload_file import UploadFile

__all__ = ['UploadFile']
```

In views, to import UploadFile model and use it:

```python
from example_app.models import UploadFile

upload_file = UploadFile.objects.get(...)
```

### Split settings.py into several files.

[https://code.djangoproject.com/wiki/SplitSettings#SimplePackageOrganizationforEnvironments](https://code.djangoproject.com/wiki/SplitSettings#SimplePackageOrganizationforEnvironments)

`settings/dev.py` is for local development.

`settings/production.py` is for deployment. ( Do not commit this file)

## Creating your project

```bash
$ django-admin.py startproject --template=https://github.com/jlhg/django-layout-template/zipball/master project_name
```

## How to run server - for local development

```bash
$ cd /path/to/your_project_root
$ python manage.py runserver --settings=your_project_name.settings.dev
```

## How to run server - for deployment

For apache2: [https://docs.djangoproject.com/en/1.2/howto/deployment/modwsgi/](https://docs.djangoproject.com/en/1.2/howto/deployment/modwsgi/)

1. Edit `settings/production.py` and add a new secret key.
2. Install mod_wsgi:

```bash
$ sudo apt-get install libapache2-mod-wsgi
```

3. Add the following contents to `http.conf`:

```
WSGIScriptAlias / /path/to/wsgi.py
```

3. Restart apache2:

```bash
$ sudo service apache2 restart
```

## Coding style

* [Django coding style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/)
* [Google python style guide](http://google-styleguide.googlecode.com/svn/trunk/pyguide.html)
