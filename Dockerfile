FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /phone
WORKDIR /phone
COPY requirement.txt /phone/
RUN pip install -r requirement.txt
COPY . /phone/