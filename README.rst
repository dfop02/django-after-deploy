============
After Deploy
============

After deploy helps you to create and manage automated deploy tasks in your Django application. Inspired by [Rails after_party](https://github.com/theSteveMitchell/after_party).

Quick start
-----------

1. Add "after_deploy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'after_deploy',
    ]

2. Now after_deploy commands are available, use install flag::

    python manage.py after_deploy --install

3. Run `python manage.py -g my_first_task` to create your first task, they'll stay at root project, on tasks folder::

    my-project
    |-- my-app
    |   |-- __init__.py
    |   |-- apps.py
    |   |-- models.py
    |   |-- settings.py
    |-- tasks
    |   |-- __init__.py
    |   |-- _000001_my_first_task.py
    |-- manage.py

4. For execute all unapplied tasks you can run `python manage.py --run`. If you need execute again a specfic task, you can run `python manage.py -r my_first_task`.

Authors
-------

[Diogo Fernandes](https://github.com/dfop02)
