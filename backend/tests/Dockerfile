FROM python:3.12-alpine

WORKDIR /app

COPY test/requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY tests/ /app/tests

CMD ["pytest", "/app/tests"]
