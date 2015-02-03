# Flask WWW API

Install Flask `pip install Flask`

Run app `python run.py`



Set up Flask to run with apache-modwsgi by pointing wsgi to `flaskapp.wsgi` 
(see http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/)

All routes and logic can be modified in `views.py`

All static html pages (aka templates) are in the templates folder.

Base template which all pages use => `templates/layout/base.html`


Change your info (github url, youtube vid, menu links, ...) in `config.py`
