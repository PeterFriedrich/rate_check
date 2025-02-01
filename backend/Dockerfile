FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apk add --no-cache gcc musl-dev libxml2 libxml2-dev libxslt-dev vim

RUN echo "set belloff=all" > /root/.vimrc

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python"]
