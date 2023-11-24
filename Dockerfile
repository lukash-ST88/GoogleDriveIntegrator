FROM python:3.11-alpine3.17

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /requirements.txt

COPY . /GoogleDriveIntegrator

WORKDIR /GoogleDriveIntegrator

RUN pip install -r /requirements.txt


