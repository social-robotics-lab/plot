FROM python:3.8-slim

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    tk 
RUN pip install matplotlib seaborn pandas numpy

ENV DISPLAY host.docker.internal:0.0

RUN useradd -m -d /home/sota -s /bin/bash sota
USER sota
WORKDIR /tmp