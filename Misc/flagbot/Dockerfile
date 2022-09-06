FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev curl

WORKDIR /app

RUN pip3 install discord

COPY flagbot.py /app 
COPY secretstuff.py /app 

ENTRYPOINT [ "python3" ]

CMD [ "/app/flagbot.py" ]
