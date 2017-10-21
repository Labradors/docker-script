FROM alpine:3.6
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
                                mbedtls-dev \
                                pcre-dev \
                                tar \
                                c-ares-dev  \
                                openssl-dev \
                                udns-dev \
                                automake \
                                asciidoc \
								python \
								python-dev \
								py-pip \
								build-base \
                                xmlto  \
								python3  \
								python3 -m ensurepip \
								
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
