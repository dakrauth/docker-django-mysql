FROM python:3.6.4-alpine3.7
RUN apk --update add build-base mysql-dev bash
RUN pip install --no-cache-dir "Django<2.1" mysqlclient

WORKDIR /app
COPY . .

EXPOSE 80
ENTRYPOINT [ "/bin/bash", "entrypoint.sh"]
