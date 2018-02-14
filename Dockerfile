FROM python:2.7-alpine

MAINTAINER Fernando Ribeiro <fernando.ribeiro@geocrafter.eu>

# Install basic applications
RUN apk add --no-cache --update \
    git


RUN git clone https://github.com/geocrafter-studio/mobi.e-status.git && cd mobi.e-status && git checkout master && cd -

# Get pip to download and install requirements:
RUN LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "pip install -r /mobi.e-status/requirements.txt --cache-dir .pip-cache && rm -rf .pip-cache"

# Set the default directory where CMD will execute
WORKDIR /mobi.e-status

# Expose default port
EXPOSE 8000

# Bootstrap script
RUN python /mobi.e-status/server.py