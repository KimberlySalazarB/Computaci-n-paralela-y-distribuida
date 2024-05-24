FROM ubuntu:20.04
RUN apt-get update && \
apt-get install -y python
COPY hola.py .
ENTRYPOINT ["python", "hola.py"]
