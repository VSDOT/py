#FROM python:latest

#WORKDIR /app

#COPY app .

#RUN pip install -r /app/requirements.txt

#EXPOSE 8080/tcp

#CMD ['pytho','/app/appi.py']
FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5000/tcp

VOLUME my_test_volume

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
