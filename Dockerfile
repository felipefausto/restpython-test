FROM ubuntu:18.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y python3 python3-pip libmysqlclient-dev

COPY . /application
WORKDIR /application/public

RUN pip3 install -r requirements.txt

ENV FLASK_CONFIG development
ENV FLASK_APP run.py
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]