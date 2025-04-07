FROM python:3.8-slim

RUN apt-get update && apt-get install -y \
    postgresql-client \
    default-libmysqlclient-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir \
    psycopg2-binary \
    flask \
    pymysql \
    mysqlclient

EXPOSE 80
CMD ["python", "app.py"]
