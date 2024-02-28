FROM ubuntu:latest

RUN apt-get update
RUN apt-get install stress
RUN stress --cpu 3 --timeout 360
