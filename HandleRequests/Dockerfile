FROM python:3.5-onbuild

#RUN mkdir /HandleRequests
#WORKDIR /HandleRequests

ENV PYTHONUNBUFFERED 1

COPY . /HandleRequests
RUN wget --load-cookies /tmp/cookies.txt "https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=1GkyJ1kbZoNiOlIFejGWoVR7kQ_AEOhMU' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=1GkyJ1kbZoNiOlIFejGWoVR7kQ_AEOhMU" -O model.pkl && rm -rf /tmp/cookies.txt

COPY start.sh /start.sh

CMD ["/start.sh"]



