FROM python:3.9

RUN apt-get update \
&& apt-get install -y binutils libproj-dev gdal-bin python3-gdal

RUN pip install --upgrade pip

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/