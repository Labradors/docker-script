FROM willmao/ubuntu-bbr
MAINTAINER jiangtao103cp@gmail.com

RUN apt-get update && apt-get install -y git \
										build-essential \
										wget \
										python-pip \
										python-m2crypto \
										python-dev \
										libevent-dev \
										python-setuptools \
										python-gevent \
										python3-pip && \
cd /root && \
wget https://github.com/jedisct1/libsodium/releases/download/1.0.10/libsodium-1.0.10.tar.gz && \
tar xf libsodium-1.0.10.tar.gz && cd libsodium-1.0.10 && \
./configure && make -j2 && make install && \
ldconfig && \
echo "fs.file-max = 1024000" >> /etc/sysctl.conf && \
echo "net.core.rmem_max = 67108864" >> /etc/sysctl.conf && \
echo "net.core.wmem_max = 67108864" >> /etc/sysctl.conf && \
echo "net.core.rmem_default = 65536" >> /etc/sysctl.conf && \
echo "net.core.wmem_default = 65536" >> /etc/sysctl.conf && \
echo "net.core.netdev_max_backlog = 4096" >> /etc/sysctl.conf && \
echo "net.core.somaxconn = 4096" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_syncookies = 1" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_tw_reuse = 1" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_tw_recycle = 0" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_fin_timeout = 30" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_keepalive_time = 1200" >> /etc/sysctl.conf && \
echo "net.ipv4.ip_local_port_range = 10000 65000" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_max_syn_backlog = 4096" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_max_tw_buckets = 5000" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_rmem = 4096 87380 67108864" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_wmem = 4096 65536 67108864" >> /etc/sysctl.conf && \
echo "net.ipv4.tcp_mtu_probing = 1" >> /etc/sysctl.conf && \
echo "net.ipv4.ip_forward = 1" >> /etc/sysctl.conf && \
sysctl -p && \
echo "* soft nofile 512000" >> /etc/security/limits.conf && \
echo "* hard nofile 1024000" >> /etc/security/limits.conf && \
ulimit -n 1024000 && \
easy_install greenlet gevent && \
cd ..  && \
git clone -b manyuser https://github.com/esdeathlove/shadowsocks.git && \
cd shadowsocks && \
pip install cymysql && \
chmod +x *.sh && \
pip install -r requirements.txt && \
ls -al
ONBUILD COPY apiconfig.py /root/shadowsocks/userapiconfig.py
ONBUILD COPY config.json  /root/shadowsocks/user-config.json 
WORKDIR /root/shadowsocks
ENTRYPOINT ["python","server.py"]

