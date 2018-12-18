	FROM python:3.5-onbuild

#RUN mkdir /MainGUI
#WORKDIR /MainGUI

ENV PYTHONUNBUFFERED 1

COPY . /MainGUI
COPY start.sh /start.sh

CMD ["/start.sh"]