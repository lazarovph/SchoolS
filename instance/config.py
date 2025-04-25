import os

# SECRET KEY
SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

# config DB SQLite
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# logging
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')

# other
# EMAIL_USER = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
