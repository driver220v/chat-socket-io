FROM ubuntu:18.04
RUN apt update
RUN apt install -y python3.8 python3-pip
RUN apt install -y nano
COPY chat-socketio  /home/chat
WORKDIR /home/chat
RUN pip3 install -r requirements.txt
