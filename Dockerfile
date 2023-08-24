FROM python:3.11-slim

WORKDIR /usr/src/app

RUN apt update \
    && apt install -y moreutils \
    && apt install -y jq \
    && apt install -y vim \
    && apt install -y telnet \
    && apt install -y wait-for-it \
    && apt install -y libpq-dev

RUN pip install --upgrade pip
COPY ./ ./

#RUN chmod +x ./entrypoint.sh

RUN pip install -r requirements.txt


ENTRYPOINT ["tail", "-f", "/dev/null"]
#ENTRYPOINT ["bash", "./entrypoint.sh"]


