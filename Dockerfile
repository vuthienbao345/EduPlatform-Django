FROM python:3.8.10-slim

# set envt var
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# set working directory
WORKDIR /code


# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt .
# RUN pip install -r requirements.txt
RUN apt-get update && apt-get install -y \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p /code
RUN chown -R 1000:1000 /code
USER 1000:1000

RUN chmod 777 /code


# copy the django project
COPY . .