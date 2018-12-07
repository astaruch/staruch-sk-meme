FROM ubuntu:18.04

RUN apt-get update && apt-get install -y python3 python3-pip libsm6 libxrender1 libfontconfig1 libxtst6

RUN mkdir /src
COPY requirements.txt /src
COPY img.jpg /src
COPY server.py /src

WORKDIR /src

RUN pip3 install -r requirements.txt

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

EXPOSE 80

CMD ["python3", "server.py"]