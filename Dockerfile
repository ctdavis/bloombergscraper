FROM python:3.5

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["scrapy","crawl","bloomberg","-a","section=commodities"]
