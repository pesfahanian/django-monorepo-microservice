FROM python:3.10.6-slim-buster

RUN mkdir /user

WORKDIR /user

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/user"

COPY . .

COPY ./scripts/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN apt-get update
RUN apt-get install -y postgresql-client

RUN pip install -r requirements.txt

EXPOSE 8200

ENTRYPOINT ["/entrypoint.sh"]
