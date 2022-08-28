release: python manage.py migrate
web: gunicorn -w 2 --log-file=- -b :$PORT dex.wsgi:application
