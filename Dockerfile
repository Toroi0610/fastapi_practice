FROM python:3.7-slim

WORKDIR /home

RUN mkdir -p /home/app
COPY app/ /home/app/

COPY requirements.txt /home
RUN pip install -r requirements.txt

COPY bootstrap.sh /home

EXPOSE 80
CMD ["./bootstrap.sh"]