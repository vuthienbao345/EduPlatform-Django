FROM python:3.8.10-slim

# set envt var
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# set working directory
WORKDIR /code


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN apt-get update && apt-get install -y libpq-dev
RUN pip install psycopg2-binary

RUN apt-get update && apt-get install -y build-essential gcc


# copy the django project
COPY . .