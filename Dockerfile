FROM ubuntu:latest

RUN sudo apt get update
RUN sudo apt install stress
RUN git clone https://github.com/eduardogomescampos1/test1_SFI2
RUN cd test1_SFI2/
RUN test_setup_execution.sh
