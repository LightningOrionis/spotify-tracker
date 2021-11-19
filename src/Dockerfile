FROM python:3.8.10

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR  /app

# RUN apt-get install netcat

COPY ./app/requirements.txt .
RUN pip install -r /app/requirements.txt

COPY ./app /app

RUN chmod +x ./entrypoint.sh

CMD sh entrypoint.sh
