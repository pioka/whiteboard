FROM python:3

ENV DJANGO_SECRET_KEY=XXXXXXXXXXX

WORKDIR /opt/whiteboard
COPY . .
RUN pip install -r requirements.txt && \
    python ./manage.py makemigrations board && \
    python ./manage.py migrate
