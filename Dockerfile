FROM nvidia/cuda:11.8.0-base-ubuntu20.04
ENV PIP_ROOT_USER_ACTION=ignore

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get -qq install -y ffmpeg
RUN apt-get install python3.10 -y git -y
RUN apt-get install pip -y
RUN pip install --upgrade pip
COPY requirements/base.txt base.txt
COPY requirements/tests.txt tests.txt
RUN pip install -r base.txt
RUN pip install -r tests.txt
