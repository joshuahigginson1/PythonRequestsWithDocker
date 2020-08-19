FROM python:3.8-alpine

LABEL version="1.0"
LABEL description="Animal Style - Service 2 Container."

EXPOSE 5001

WORKDIR /

COPY . /

RUN sudo apt-get update && sudo pip3 install requirements.txt

ENTRYPOINT ["/service2", "service2_wsgi.py"]