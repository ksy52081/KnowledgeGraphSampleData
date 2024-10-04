FROM python:3.9

ENV LANGUAGE C.UTF-8
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
RUN ln -sf /usr/share/zoneinfo/Asia/Seoul /etc/localtime

ADD requirements.txt /root/agent/requirements.txt
RUN pip install -r /root/agent/requirements.txt

ADD ./main.py /root/agent/
ADD ./common/ /root/agent/common
ADD ./generator/ /root/agent/generator
ADD ./runner/ /root/agent/runner

WORKDIR /root
ENTRYPOINT ["python3", "-m", "agent.main"]
