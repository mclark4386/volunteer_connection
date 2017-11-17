from python:3.6
maintainer Matt Clark <matt@motionmobs.com>

ENV PYTHONUNBUFFERED 1

RUN apt-get -y update \
    && apt-get install -y \
       swig \
       libssl-dev \
       dpkg-dev \
       netcat \
        fonts-font-awesome \
        libffi-dev \
        libgdk-pixbuf2.0-0 \
        libpango1.0-0 \
        python-dev \
        python-lxml \
        shared-mime-info \
        libcairo2 \
    && apt-get -y clean \
    && mkdir /code \
    && pip install -U pip 
    
WORKDIR /code
COPY requirements.txt /code/

RUN pip install -Ur requirements.txt

COPY . /code/

RUN python /code/manage.py collectstatic --noinput

EXPOSE 8000

CMD ["/code/prod_run.sh"]

