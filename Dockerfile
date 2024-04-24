FROM python:3.11.6-bullseye

WORKDIR /tmp

COPY . .

RUN pip install -r requirements.txt