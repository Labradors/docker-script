FROM willmao/ubuntu-bbr
MAINTAINER jiangtao103cp@gmail.com

RUN apt-get update && apt-get install -y git \
										python-pip \
										python3-pip && \
cd /root && \
git clone -b manyuser https://github.com/esdeathlove/shadowsocks.git && \
cd shadowsocks && \
pip install cymysql && \
pip install supervisor && \
echo_supervisord_conf > /etc/supervisord.conf 
COPY supervisor /root/shadowsocks/supervisor && \
chmod a+x /root/shadowsocks/supervisor && \
bash /root/shadowsocks/supervisor && \
supervisord -c /etc/supervisord.conf && \
chmod +x *.sh && \
pip install -r requirements.txt && \
ls -al
ONBUILD COPY apiconfig.py /root/shadowsocks/userapiconfig.py
ONBUILD COPY config.json  /root/shadowsocks/user-config.json 
WORKDIR /root/shadowsocks
ENTRYPOINT ["supervisorctl ","update"]

