FROM python:3.6

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY   . /Templates

WORKDIR /app

EXPOSE 8080/tcp

VOLUME my_data

CMD ["python", "app.py"]
