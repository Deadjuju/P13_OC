FROM cimg/python:3.10.7

ARG DJANGO_SETTINGS_MODULE=oc_lettings_site.settings.develop

ENV DJANGO_SETTINGS_MODULE=${DJANGO_SETTINGS_MODULE}
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN pip install --upgrade pip 
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .

CMD python manage.py runserver 0.0.0.0:8000 --settings=$DJANGO_SETTINGS_MODULE