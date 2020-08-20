============
After Deploy
============

After deploy helps you to create and manage automated deploy tasks in your Django application. Inspired by `Rails after_party`_

Quick start
-----------

1. Install the package using pip by running::

    pip install django-after-deploy

2. Add "after_deploy" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'after_deploy',
    ]

3. Now after_deploy commands are available, use install flag::

    python manage.py after_deploy --install

4. Run ``python manage.py after_deploy -g my_first_task`` to create your first task, they'll stay at root project, on tasks folder::

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

5. For execute all unapplied tasks you can run ``python manage.py after_deploy --run``. If you need execute again a specfic task, you can run ``python manage.py after_deploy -r my_first_task``.

Authors
-------

- `Diogo Fernandes`_

Contribute
----------

If you find an issue with AfterDeploy please log an issue. I will accept pull requests.

.. _Rails after_party: https://github.com/theSteveMitchell/after_party.
.. _Diogo Fernandes: https://github.com/dfop02
