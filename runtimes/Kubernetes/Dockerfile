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
        && rm -rf /var/lib/apt/lists/* \
        && apt-cache search linux-headers-generic

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

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip six && pip install --no-cache-dir -r requirements.txt

ENV PYTHONUNBUFFERED TRUE

ENV GRASSBIN=/usr/bin/grass

# Copy Lithops proxy and lib to the container image.
ENV APP_HOME /lithops

WORKDIR $APP_HOME

COPY lithops_k8s.zip .

RUN unzip lithops_k8s.zip && rm lithops_k8s.zip

RUN export CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt
