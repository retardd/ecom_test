FROM python:3.12

ENV PYTHONUNBUFFERED 1

COPY . /test_job
WORKDIR /test_job

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
