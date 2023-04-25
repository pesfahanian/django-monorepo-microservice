FROM python:3.11.2-slim-buster

RUN mkdir /app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH "${PYTHONPATH}:/app"

RUN ls

COPY . .

COPY ./service/wallet/scripts/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

RUN pip install -r requirements.txt
RUN pip install -r service/wallet/requirements.txt

EXPOSE 8200

ENTRYPOINT ["/entrypoint.sh"]
