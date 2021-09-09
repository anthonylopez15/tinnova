# Pull base image
FROM python:3.8-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code/

# Install dependencies

COPY Pipfile Pipfile.lock /code/

RUN apt-get update -qq && \
    apt-get clean && \
    rm -rf /var/cache/apk/* && \
    pip install --upgrade pip==20.2.3 --no-cache-dir

RUN pip install pipenv --no-cache-dir && \
    pipenv install --system --ignore-pipfile --deploy

COPY . /code/

EXPOSE 8000
