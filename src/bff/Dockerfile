FROM python:3.12-alpine

RUN apk add build-base linux-headers
WORKDIR /code

ENV FLASK_CONFIG=production

COPY . ./bff
RUN pip install -r ./bff/requirements.txt

EXPOSE 8000
CMD ["flask", "-A", "./bff", "run", "-h", "0.0.0.0", "-p", "8000"]