FROM python:3.8-buster

LABEL version="1.0"
LABEL description="Animal Style - Service 1 Container."

EXPOSE 5000

WORKDIR /

COPY . .

RUN apt-get update
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "service1_wsgi.py"]
