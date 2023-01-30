FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /admin_app
COPY requirements.txt /admin_app/requirements.txt
RUN pip install -r requirements.txt
COPY . /admin_app

CMD python manage.py runserver 0.0.0.0:10000