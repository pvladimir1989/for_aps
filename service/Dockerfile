FROM python:latest

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

RUN \
  apt-get update && \
  apt-get install -y python3 python3-pip python3-dev

RUN python -m venv venv
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip --no-cache-dir install -r requirements.txt

COPY . /usr/src/app/

EXPOSE 8000

ENV FLASK_APP /usr/src/app/server/app.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8000"]






