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

ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip six && pip install --no-cache-dir -r requirements.txt

### Install Sen2Cor-02.09.00-Linux64.run
### Sen2cor Version 2.9.0
RUN mkdir /opt/sen2cor && \
    wget http://step.esa.int/thirdparties/sen2cor/2.9.0/Sen2Cor-02.09.00-Linux64.run && \
    chmod +x Sen2Cor-02.09.00-Linux64.run && \
    bash Sen2Cor-02.09.00-Linux64.run --target /opt/sen2cor && \
    rm Sen2Cor-02.09.00-Linux64.run

ENV PATH $PATH:/opt/sen2cor/bin/

# Setting environment variables
ENV PYTHONUNBUFFERED 1

ENV FLASK_PROXY_PORT 8080

# create action working directory
RUN mkdir -p /action \
    && mkdir -p /actionProxy \
    && mkdir -p /pythonAction

ADD https://raw.githubusercontent.com/apache/openwhisk-runtime-docker/8b2e205c39d84ed5ede6b1b08cccf314a2b13105/core/actionProxy/actionproxy.py /actionProxy/actionproxy.py
ADD https://raw.githubusercontent.com/apache/openwhisk-runtime-python/3%401.0.3/core/pythonAction/pythonrunner.py /pythonAction/pythonrunner.py

CMD ["/bin/bash", "-c", "cd /pythonAction && python -u pythonrunner.py"]
