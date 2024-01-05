#!/bin/bash


IMAGE_NAME="moonsapp"

echo "FROM python:3">Dockerfile
echo "WORKDIR /app">>Dockerfile
echo "COPY . /app">>Dockerfile
echo "RUN pip install django">>Dockerfile
echo "EXPOSE 8001">>Dockerfile
echo "CMD python manage.py runserver 0.0.0.0:8001">>Dockerfile

docker build -t "$IMAGE_NAME" .

container_ID=$(docker run -p 8001:8001 -d "$IMAGE_NAME")

echo "Docker container ID: $container_ID"

docker logs -f "$container_ID"



