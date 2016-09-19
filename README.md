# Development enviorment for Django with Docker

$ docker build -t nathanguenther/django-docker .

$ docker run -d -p 80:80 -v $(pwd):/code --env DJANGO_PRODUCTION=false nathanguenther/django-docker
