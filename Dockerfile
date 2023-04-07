FROM python:3.8.10-buster

LABEL authors="Miguel Rojo"

WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

#OS update + install common packages
RUN apt-get update
RUN apt-get -y install software-properties-common
RUN apt-get -y install curl apt-transport-https
RUN apt-get -y install vim
RUN apt-get -y install bash-completion

#Python installation
COPY ./requirements.txt /app/requirements.txt

RUN pip3 install --upgrade pip
RUN pip3 install --default-timeout=100 --no-cache-dir --upgrade -r  /app/requirements.txt

COPY . /app

CMD ["bash"]