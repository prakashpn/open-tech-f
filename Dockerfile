# syntax=docker/dockerfile:1

FROM python:3.8

RUN mkdir -p /foryou
COPY ./requirements.txt /requirements.txt

RUN pip3 install -r requirements.txt

WORKDIR /foryou
COPY . /foryou

CMD [ "python3", "./app.py"]
# CMD python3 main.py --port=8081
EXPOSE 8081
EXPOSE 81
