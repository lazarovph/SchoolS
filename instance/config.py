import os

# Секретен ключ за сесии и сигурност
SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(24)

# Конфигурация за базата данни (SQLite в случая)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///site.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Настройки за логване
LOGGING_LEVEL = os.environ.get('LOGGING_LEVEL', 'DEBUG')

# Други конфигурации (по избор)
# EMAIL_USER = os.environ.get('EMAIL_USER')
# EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
