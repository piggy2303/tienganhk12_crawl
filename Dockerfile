FROM python:3.7-slim

WORKDIR /app

# COPY . . 

RUN pip3 install --upgrade pip
RUN pip install requests

# CMD /bin/bash