FROM alpine
MAINTAINER jiangtao103cp@gmail.com

RUN set -ex && \
    apk add --no-cache --virtual .build-deps \
                                autoconf \
                                build-base \
                                git \
                                libev-dev \
                                libtool \
                                linux-headers \
                                libsodium-dev \
cd ~ && \
git clone -b manyuser https://github.com/Ssrbackup/shadowsocksr.git && \
cd shadowsocksr && \
./setup_cymysql.sh
./initcfg.sh
ADD userapiconfig.py /root/shadowsocksr/userapiconfig.py
ADD usermysql.json /root/shadowsocksr/usermysql.json
ADD user-config.json /root/shadowsocksr/user-config.json
ENTRYPOINT ["bash","./logrun.sh"]