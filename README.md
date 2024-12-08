How to start?
  Windows:
    1) Create virtual environment - python -m venv env
    2) Call virtual environment - call env/Scripts/activate.bat
    3) Install all packages from requirements.txt - pip install -r requirements.txt
    4) Make migrations - python manage.py makemigrations
    5) Migrate - python manage.py migrate
    6) Run server - python manage.py runserver
    7) Go on localhost - http://localhost:8000/users
  
  
  
  Linux:
    1) Create virtual environment - python3 -m venv env
    2) Activate virtual environment - source env/bin/activate
    3) Install all packages from requirements.txt - pip install -r requirements.txt
    4) Make migrations - python manage.py makemigrations
    5) Migrate - python manage.py migrate
    6) Run server - python manage.py runserver
    7) Go on localhost - http://localhost:8000/users
