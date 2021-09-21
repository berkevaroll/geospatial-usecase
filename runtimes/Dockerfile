FROM python:3.8-buster

RUN apt-get update && \
        apt-get upgrade -y && \
        apt-get install -y --no-install-recommends \
        build-essential \
        gcc \
        grass \
        grass-dev \        
        libc-dev \
        libxslt-dev \
        libxml2-dev \
        libffi-dev \
        libssl-dev \
        zip \
        unzip \
        vim \
        libgdal-dev \
        gdal-bin \
        && rm -rf /var/lib/apt/lists/*

# Workaround to work with grass74:

# RUN wget http://archive.ubuntu.com/ubuntu/pool/universe/g/grass/grass-core_7.4.0-1_amd64.deb && \
#         wget http://archive.ubuntu.com/ubuntu/pool/universe/g/grass/grass-dev_7.4.0-1_amd64.deb && \
#         wget https://repo.mysql.com/apt/debian/pool/mysql-5.7/m/mysql-community/libmysqlclient20_5.7.34-1debian10_amd64.deb && \
#         wget http://ftp.br.debian.org/debian/pool/main/p/proj/libproj12_4.9.3-1_amd64.deb

# RUN dpkg -i libproj12_4.9.3-1_amd64.deb && \
#         dpkg -i libmysqlclient20_5.7.34-1debian10_amd64.deb && \
#         dpkg -i grass-core_7.4.0-1_amd64.deb && \
#         dpkg -i grass-dev_7.4.0-1_amd64.deb

# RUN rm *.deb

# End

RUN pip install --upgrade setuptools six pip \
        && pip install --no-cache-dir \
        flask \
        glob2 \
        ibm-cos-sdk \
        redis \
        PyYAML \
        kubernetes \
        numpy \
        cloudpickle \
        ps-mem \
        tblib \
        gevent \
        namegenerator \
        pika \
        cryptography \
        scikit-learn \
        scipy \
        pandas \
        Pillow \
        affine==2.2.2 \
        attrs==18.2.0 \
        bs4==0.0.1 \
        certifi==2018.11.29 \
        chardet==3.0.4 \
        cligj==0.5.0 \
        cycler==0.10.0 \
        GDAL==2.4.0 \
        geojson==2.4.1 \
        geomet==0.2.0.post2 \
        grass-session==0.5 \
        html2text==2018.1.9 \
        idna==2.8 \
        kiwisolver==1.0.1 \
        pyparsing==2.3.1 \
        snuggs==1.4.2 \
        soupsieve==1.7.3 \
        rasterio==1.1.0 \
        pyproj==2.4.1 \
        Fiona==1.8.11 \
        Shapely==1.6.4.post2

RUN apt-cache search linux-headers-generic

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

ENV PYTHONUNBUFFERED TRUE

ENV GRASSBIN=/usr/bin/grass

# Copy Lithops proxy and lib to the container image.
ENV APP_HOME /lithops

WORKDIR $APP_HOME

COPY lithops_k8s.zip .

RUN unzip lithops_k8s.zip && rm lithops_k8s.zip

RUN export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
