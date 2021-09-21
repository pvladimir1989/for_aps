FROM python:latest

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

RUN \
  apt-get update && \
  apt-get install -y python3 python3-pip python3-dev

RUN python -m venv venv
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip --no-cache-dir install -r requirements.txt

# copy project
COPY . /usr/src/app/

#WORKDIR /usr/src/app/

EXPOSE 5000

#ENTRYPOINT [ "app.py" ]


ENV FLASK_APP /usr/src/app/server/app.py


#CMD ["flask", "run"]
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
#CMD [ "flask", "run", "--host=0.0.0.0"]
#ENTRYPOINT["python3"]
#CMD python3 app.py


#CMD["app.py"]






