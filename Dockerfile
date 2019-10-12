FROM python:3

ADD . /

RUN pip install flask
RUN pip install mysql-connector

CMD [ "python", "./app.py" ]