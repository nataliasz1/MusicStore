FROM python:3.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN python3 manage.py generateschema > ./api/static/api/openapi-schema.yml
