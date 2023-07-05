FROM python:3.8-alpine

WORKDIR /app

COPY . .

RUN pip install Flask

EXPOSE 5000

VOLUME New_volume

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
