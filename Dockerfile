FROM python:3.11-slim

WORKDIR /usr/src/app

RUN apt update \
    && apt install -y moreutils \
    && apt install -y jq \
    && apt install -y vim \
    && apt install -y telnet \
    && apt install -y wait-for-it
#    && apt install -y libpq-dev
#    && apt install -y gcc \
#    && apt install -y build-essential checkinstall libffi-dev \
#    && apt install -y libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev



RUN pip install --upgrade pip
COPY ./ ./

#RUN chmod +x ./entrypoint.sh

RUN pip install -r requirements.txt


#ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["bash", "./entrypoint_scrapyd.sh"]


