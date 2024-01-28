
FROM --platform=linux/amd64 python:3.8-slim-buster as build



WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


ARG MONGO_URI


RUN echo "MONGO_URI=${MONGO_URI}" > .env


COPY . /app


CMD ["python", "app.py"]


