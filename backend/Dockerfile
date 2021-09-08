# pull official base image
FROM python:3.9.5-slim-buster

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    libpq-dev \
    gcc \
    netcat \
    tzdata \
    python3-setuptools \
    python3-pip \
    python3-dev \
    python3-venv \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
COPY ./Pipfile /usr/src/app/Pipfile
RUN pipenv install --skip-lock --dev --system

# copy project
COPY . /usr/src/app/

# so as to run gunicorn --bind 0.0.0.0:5000 manage:app
# WORKDIR /usr/src/app/src