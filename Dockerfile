FROM debian

MAINTAINER donnici "yep.dias@gmail.com"

RUN apt-get update && apt-get install -y nginx && apt-get clean
RUN apt-get install -y python3 python3-pip python3-dev python3-psycopg2 postgresql-client
RUN apt-get install -y python python-pip python-dev python-psycopg2
RUN apt-get install virtualenv -y
RUN apt-get -y update && apt-get -y autoremove
RUN mkdir concilia-api
RUN cd concilia-api
RUN virtualenv venv_concilia
RUN source venv_concilia/bin/activate
RUN pip install -r requirements.txt

EXPOSE 8000
