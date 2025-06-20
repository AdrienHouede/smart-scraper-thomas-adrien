FROM node:20 AS frontend-build
WORKDIR /app
COPY ../frontend/ .
RUN npm install && npm run build

FROM python:3.11-slim

RUN apt-get update && apt-get install -y gcc build-essential python3-dev libffi-dev && rm -rf /var/lib/apt/lists/*

# Install deps
WORKDIR /app
COPY ../backend/ .
COPY ../frontend/build/ ./frontend_build/
RUN pip install --no-cache-dir -r requirements.txt

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*
COPY docker/nginx.conf /etc/nginx/nginx.conf

CMD service nginx start && flask run --port=5000
