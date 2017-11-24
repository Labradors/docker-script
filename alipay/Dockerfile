FROM node:alpine
ENV NPM_CONFIG_LOGLEVEL info
MAINTAINER jiangtao103cp@gmail.com

# 需要挂在配置文件
# 需要安装git

RUN apk add --no-cache git && \
cd /root && \
git clone https://github.com/thundernet8/AlipayOrdersSupervisor.git && \
cd AlipayOrdersSupervisor && \
npm install && \
ENTRYPOINT ["forever","start","index.js"]