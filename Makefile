SHELL=/bin/bash

ACTIVATE=source ./.venv/bin/activate &&

CD=${ACTIVATE} cd ./jwt_check &&


main: run


# make init name=jwt_check
init:
	python3 -m venv .venv
	${ACTIVATE} pip3 install django
	${ACTIVATE} django-admin startproject ${name}
	cd ${name} && echo 'django' > ./requirements.txt
	sed -i -e 's/jwt_check/${name}/' ./Makefile


venv:
	if [ ! -d ./.venv ]; then python3 -m venv ./.venv; fi;


install: venv
	${CD} pip3 install -r ./requirements.txt
	${CD} python3 manage.py makemigrations
	${CD} python3 manage.py migrate
	- ${CD} python3 manage.py collectstatic --noinput


# make test args=my_app
test:
	${CD} python3 manage.py test ${args};


# make new app=my_app
new:
	${CD} python3 manage.py startapp ${app};


user:
	${CD} python3 manage.py createsuperuser;


tra:
	${CD} if [ ! -d ./locale ]; then mkdir locale; fi;
	${CD} python3 manage.py makemessages -l ar
	${CD} python3 manage.py compilemessages


run:
	${CD} python3 manage.py runserver


shell:
	${CD} python3 manage.py shell
