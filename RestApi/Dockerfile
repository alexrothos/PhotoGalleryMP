FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /rest_api
COPY requirements.txt /rest_api/requirements.txt
RUN pip install -r requirements.txt
COPY . /rest_api/

CMD python restApi.py runserver 127.0.0.1:10001