FROM ubuntu:latest

RUN apt-get update
RUN apt-get install stress
ENTRYPOINT ["stress"]
CMD ["--cpu", "2", "--timeout", "1800"]
