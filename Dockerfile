# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY . /code
COPY requirements.txt /code/
WORKDIR /code
RUN pip install -r requirements.txt
RUN pip install Django --upgrade
RUN pip install -U djangorestframework

#below lines are for standalone Dockerization(Not with Docker compose)
EXPOSE 8000

CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# CMD ["%%CMD%%"]