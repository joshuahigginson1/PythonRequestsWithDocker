FROM python:3.8-buster

LABEL version="1.0"
LABEL description="Animal Style - Service 2 Container."

EXPOSE 5001

WORKDIR /

COPY . .

RUN apt-get update
RUN pip3 install -r requirements.txt

ENTRYPOINT ["/usr/local/bin/python", "service2_wsgi.py"]