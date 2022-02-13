FROM python:3-alpine3.9

WORKDIR /usr/src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add --no-cache --update sqlite=3.28.0-r3
RUN pip install --upgrade pip
COPY ../requirements.txt .
COPY ../entrypoint.sh .
COPY ./app ./app
RUN pip install -r requirements.txt



ENTRYPOINT ["/usr/src/entrypoint.sh"]