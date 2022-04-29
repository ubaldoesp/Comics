FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code
COPY . /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["gunicorn","-c", "config/gunicorn/conf.py", "--bind", ":8000", "api.wsgi:application"]