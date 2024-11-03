# FROM python:3.12
FROM mambaorg/micromamba:latest
WORKDIR /usr/local/app

COPY env.yaml /tmp
# Install the application dependencies
RUN micromamba install -y -n base -c conda-forge /tmp/env.yaml
#RUN pip install --no-cache-dir -r requirements.txt
