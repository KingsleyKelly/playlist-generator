Modified todo list in to playlist generator.
Chance to try out lots of things in Django and use the Youtube api.
Nice live player with JS.


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

