FROM python:3.8

WORKDIR /code

COPY ./requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY . .