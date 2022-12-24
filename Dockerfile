FROM ubuntu:20.04
FROM python:3.10

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt