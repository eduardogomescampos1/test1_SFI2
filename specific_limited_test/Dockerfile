FROM ubuntu:latest

RUN apt-get update
RUN apt-get install stress
RUN apt-get install cpulimit
WORKDIR /test
COPY n_sec_test.sh /test
RUN chmod +x n_sec_test.sh
ENTRYPOINT ["bash","n_sec_test.sh", "4","5","360"]
