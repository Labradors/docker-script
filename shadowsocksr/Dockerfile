FROM willmao/ubuntu-bbr
MAINTAINER jiangtao103cp@gmail.com

RUN apt-get update && apt-get install -y git \
										build-essential \
										wget
										python-pip \
										python3-pip && \
cd /root && \
wget https://github.com/jedisct1/libsodium/releases/download/1.0.10/libsodium-1.0.10.tar.gz && \
tar xf libsodium-1.0.10.tar.gz && cd libsodium-1.0.10 && \
./configure && make -j2 && make install && \
ldconfig && \
cd ..  && \
git clone -b manyuser https://github.com/esdeathlove/shadowsocks.git && \
cd shadowsocks && \
pip install cymysql && \
# pip install supervisor && \
# echo_supervisord_conf > /etc/supervisord.conf && \
# echo "[program:ssr]" >> /etc/supervisord.conf && \
# echo "directory=/root/shadowsocks" >> /etc/supervisord.conf  && \
# echo "command = python server.py" >> /etc/supervisord.conf && \
# echo "user = root" >> /etc/supervisord.conf && \
# echo "autostart = true" >> /etc/supervisord.conf && \
# echo "autoresart = true" >> /etc/supervisord.conf && \
chmod +x *.sh && \
pip install -r requirements.txt && \
ls -al
ONBUILD COPY apiconfig.py /root/shadowsocks/userapiconfig.py
ONBUILD COPY config.json  /root/shadowsocks/user-config.json 
WORKDIR /root/shadowsocks
ENTRYPOINT ["python","server.py"]

