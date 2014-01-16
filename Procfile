web: python manage.py runserver 0.0.0.0:$PORT --noreload
web: python manage.py collectstatic --noinput ; gunicorn --bind 0.0.0.0:$PORT wsgi:application