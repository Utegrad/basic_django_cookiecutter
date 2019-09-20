After generating the project from cookiecutter
==============================================

install packages from requirements.txt:

  - ``pip install -r requirements.txt``

copy the example .env file:

  - ``cp *project_slug*/*project_slug*/.env.EXAMPLE *project_slug*/*project_slug*/.env``

set the secret key in the .env file:

  - ``python secret-key-gen.py``
    
	To generate a secret key
  
  - replace '``A SECRET_KEY``' in the .env file with your secret key 

run database migrations:

  - ``python manage.py migrate``

create a super user (optional):

  - ``python manage.py createsuperuser``
	- follow the prompts

start an app:

  - ``python manage.py startapp my_app``

run the dev server:

  - ``python manage.py runserver``
