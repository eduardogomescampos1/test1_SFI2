FROM ubuntu:latest

RUN apt-get update
RUN apt-get install stress
ENTRYPOINT ["stress"]
CMD ["--cpu", "3", "--timeout", "1800"]
