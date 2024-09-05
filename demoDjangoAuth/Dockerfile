FROM python:3.12.3

WORKDIR /app
COPY . /app

EXPOSE 80

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN pip install --upgrade pip
RUN pip install -r requirements.txt