FROM python:3.9-alpine

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update && \
     apk add postgresql-dev gcc python3-dev musl-dev && \
     pip install --upgrade pip
COPY ../requirements.txt .
RUN pip install -r requirements.txt
COPY ./app/entrypoint.sh .
COPY ./app/first_start.sh .
COPY ./app ./app
ENTRYPOINT ["/usr/src/entrypoint.sh"]
CMD gunicorn --bind 0.0.0.0:8000 config.wsgi:application