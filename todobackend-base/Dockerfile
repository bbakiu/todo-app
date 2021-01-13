FROM ubuntu:trusty

LABEL author="bbakiu"

ENV TERM=xterm-256color

# Install Python runitme
RUN apt-get update && \
    apt-get install -y \
    -o APT::Install-Recommend=false -o APT::Install-Suggests=false \
    python python-virtualenv


# Create virtual envrionment
RUN virtualenv /appenv && \
    . /appenv/bin/activate && \
    pip install pip --upgrade