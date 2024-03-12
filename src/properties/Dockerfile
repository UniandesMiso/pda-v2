FROM python:3.12-alpine

RUN apk add build-base linux-headers
WORKDIR /code

ENV FLASK_CONFIG=production

COPY . ./properties
RUN pip install -r ./properties/requirements.txt

EXPOSE 3000
CMD ["flask", "-A", "./properties/api", "run", "-h", "0.0.0.0", "-p", "3000"]