Basic To Do App in Django
=========================

This is a basic to do app in django. Its meant to be a more complicated hello world for django that utilizes a database.

Getting setup
-------------

::

    virtualenv --no-site-packages venv
    source venv/bin/activate
    pip install -r requirements.txt
    python app/manage.py syncdb
    python app/manage.py runserver

Deploying to Heroku
-------------------

::

    heroku create -s cedar
    git push heroku master
    heroku run python app/manage.py syncdb
    heroku open

