FROM willmao/ubuntu-bbr
MAINTAINER jiangtao103cp@gmail.com

RUN apt-get update && \			
cd /root && \
git clone -b manyuser https://github.com/esdeathlove/shadowsocks.git && \
cd shadowsocks && \
pip install cymysql && \
chmod +x *.sh && \
pip install -r requirements.txt && \
ls -al
ONBUILD COPY apiconfig.py userapiconfig.py
ONBUILD COPY config.py  user-config.json 
WORKDIR /root/shadowsocks && \

ENTRYPOINT ["python","server.py"]
