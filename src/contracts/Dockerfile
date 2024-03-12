FROM python:3.12-alpine

RUN apk add build-base linux-headers
WORKDIR /code

ENV FLASK_CONFIG=production

COPY . ./contracts
RUN pip install -r ./contracts/requirements.txt

EXPOSE 3001
CMD ["flask", "-A", "./contracts/api", "run", "-h", "0.0.0.0", "-p", "3001"]