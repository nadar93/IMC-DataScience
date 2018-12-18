FROM python:3.5-onbuild

#RUN mkdir /HandleRequests
#WORKDIR /HandleRequests

ENV PYTHONUNBUFFERED 1

COPY . /HandleRequests
COPY start.sh /start.sh

CMD ["/start.sh"]