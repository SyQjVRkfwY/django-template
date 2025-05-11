FROM python:3.14.0b1-bookworm

RUN mkdir /workspace
WORKDIR /workspace

COPY ./initdata/requirements.txt /

RUN pip install --upgrade pip && pip install -r /requirements.txt