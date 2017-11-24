FROM ubuntu:16.04
MAINTAINER jiangtao103cp@gmail.com

RUN apt-get update && apt-get install -y git \
										sudo \
										wget \
										curl \
										nodejs \
										npm && \
npm install hexo-cli -g && \
hexo init blog && \
cd blog && \
npm install && \
npm install hexo-renderer-scss --save && \
git clone https://github.com/ahonn/hexo-theme-even themes/even && \
VOLUME ["/root/blog/"]
ENTRYPOINT ["hexo","server","-p","8000"]