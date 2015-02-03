#!flask/bin/python
from flask import Flask
from app import app as application


if __name__ == '__main__':
    application.run(debug=True)