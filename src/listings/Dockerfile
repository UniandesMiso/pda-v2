FROM python:3.12-alpine

RUN apk add build-base linux-headers
WORKDIR /code

ENV FLASK_CONFIG=production

COPY . ./listings
RUN pip install -r ./listings/requirements.txt

EXPOSE 3002
CMD ["flask", "-A", "./listings/api", "run", "-h", "0.0.0.0", "-p", "3002"]