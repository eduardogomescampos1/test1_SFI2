FROM ubuntu:latest

RUN apt-get update
RUN apt-get install stress
RUN apt-get install -y git
RUN git clone https://github.com/eduardogomescampos1/test1_SFI2
WORKDIR "/test1_SFI2"
RUN git pull
RUN chmod +x /test1_SFI2/test1_hamperer.sh
RUN /test1_SFI2/test1_hamperer.sh
