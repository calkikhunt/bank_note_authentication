FROM continuumio/anaconda3

WORKDIR /usr/app/

COPY ./requirements.txt /usr/app/
RUN pip3 install -r requirements.txt
COPY . /usr/app/

EXPOSE 5000

CMD python3 app.py