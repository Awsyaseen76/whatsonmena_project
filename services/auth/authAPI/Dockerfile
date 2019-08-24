# Pull base image
FROM python:3.7-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /auth_service

# Install dependencies
RUN pip install pipenv
COPY Pipfile Pipfile.lock /auth_service/
RUN pipenv install djangorestframework
RUN pipenv install --system


# Copy project
COPY . /auth_service/