pip install -r requirements.txt
python manage.py collecstatic --no-input
python manage.py migrate
python manage.py runserver
python load.py