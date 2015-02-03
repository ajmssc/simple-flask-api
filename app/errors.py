from flask import render_template, request
from app import app


@app.errorhandler(404)
def page_not_found(error):
	app.logger.debug("Error 404 %s" % request.url)
	return render_template('errors/404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500
