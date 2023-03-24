FROM python:3
ENV PYTHONUNBUFFERED 1
WORKDIR /testtask
ADD ./testtask
RUN pip install -r requirements.txt