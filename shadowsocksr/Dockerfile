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
echo_supervisord_conf > /etc/supervisord.conf && \
mkdir /etc/supervisord && \
echo "[include]" > /etc/supervisord.conf  && \
echo "files = /etc/supervisord/*.conf" > /etc/supervisord.conf && \
touch /etc/supervisord/ssr.conf && \
echo "[program:ssr]" > /etc/supervisord/ssr.conf && \
echo "directory=/root/shadowsocks" > /etc/supervisord/ssr.conf && \
echo "command = python server.py" > /etc/supervisord/ssr.conf && \
echo "user = root" > /etc/supervisord/ssr.conf && \
echo "autostart = true" > /etc/supervisord/ssr.conf && \
echo "autoresart = true" > /etc/supervisord/ssr.conf && \
supervisord -c /etc/supervisord.conf && \
chmod +x *.sh && \
pip install -r requirements.txt && \
ls -al
ONBUILD COPY apiconfig.py /root/shadowsocks/userapiconfig.py
ONBUILD COPY config.json  /root/shadowsocks/user-config.json 
WORKDIR /root/shadowsocks
ENTRYPOINT ["supervisorctl ","update"]

