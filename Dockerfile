FROM python:3.6

MAINTAINER Amit Kumar Jaiswal <amitkumarj441@gmail.com>

# Install dependencies
RUN apt-get update && \
    apt-get install -y libssl-dev build-essential automake pkg-config libtool libffi-dev libgmp-dev

# Download and install pybiblecoin
WORKDIR /code
RUN git clone https://github.com/biblecoin/pybiblecoin.git
WORKDIR /code/pybiblecoin
RUN python setup.py install
