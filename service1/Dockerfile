FROM python:3.8-alpine

LABEL version="1.0"
LABEL description="Animal Style - Service 1 Container."

EXPOSE 5000

WORKDIR /

COPY . /

RUN sudo apt-get update && sudo pip3 install requirements.txt

ENTRYPOINT ["/service1", "service1_wsgi.py"]