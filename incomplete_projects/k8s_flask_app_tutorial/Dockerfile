FROM python:3.10

RUN pip install flask pytz uwsgi

RUN mkdir /usr/src/app
WORKDIR /user/src/app
COPY clock.py /usr/src/app

EXPOSE 5000
CMD ["uwsgi", "--http", ":5000", "-w", "clock:app"]