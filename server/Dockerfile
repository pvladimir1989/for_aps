#FROM python:latest
#
## set work directory
#WORKDIR /usr/src/app
#
## set environment variables
#ENV PYTHONDONTWRITEBYTECODE 1
#ENV PYTHONUNBUFFERED 1
#
## install dependencies
#RUN pip install --upgrade pip
#RUN python -m venv venv
#COPY ./requirements.txt /usr/src/app/requirements.txt
#RUN pip install -r requirements.txt
#
## copy project
#COPY . /usr/src/app/


FROM python:3
ENV PYTHONUNBUFFERED=1
RUN pip install psycopg2
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -r requirements.txt




