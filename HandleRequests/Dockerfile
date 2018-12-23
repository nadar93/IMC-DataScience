FROM python:3.5-onbuild

#RUN mkdir /HandleRequests
#WORKDIR /HandleRequests

ENV PYTHONUNBUFFERED 1

COPY . /HandleRequests
RUN wget --no-check-certificate --directory-prefix=/usr/src/app/HandleRequests/api/ 'https://docs.google.com/uc?export=download&id=1GkyJ1kbZoNiOlIFejGWoVR7kQ_AEOhMU' -O model.pkl

COPY start.sh /start.sh

CMD ["/start.sh"]