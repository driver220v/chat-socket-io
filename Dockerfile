FROM ubuntu:18.04
RUN apt update
RUN apt install -y python3.8 python3-pip
RUN apt install -y nano
COPY chat2  /home/chat
RUN cd home/chat && pip3 install -r requirements.txt
