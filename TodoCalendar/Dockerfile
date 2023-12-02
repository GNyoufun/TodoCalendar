# Pull base image
FROM python:3.11.4-slim-bullseye

# Set env vars
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work dir
WORKDIR /code

RUN apt-get update && apt-get upgrade
RUN apt-get install libtiff5-dev libjpeg62-turbo-dev libopenjp2-7-dev zlib1g-dev \
    libfreetype6-dev liblcms2-dev libwebp-dev tcl8.6-dev tk8.6-dev python3-tk \
    libharfbuzz-dev libfribidi-dev libxcb1-dev -y

# Install deps
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# Copy project
COPY . .