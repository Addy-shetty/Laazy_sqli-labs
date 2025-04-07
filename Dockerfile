FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install psycopg2-binary flask

EXPOSE 80
CMD ["python", "app.py"]
