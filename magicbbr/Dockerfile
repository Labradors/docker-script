FROM debian:latest
MAINTAINER jiangtao103cp@gmail.com
#Download applications
RUN apt-get update \
    && apt-get install -y libsodium-dev python git ca-certificates iptables --no-install-recommends

COPY rinetd_bbr rinetd_bbr_powered rinetd_pcc start.sh /root/
RUN chmod a+x /root/rinetd_bbr /root/rinetd_bbr_powered /root/rinetd_pcc /root/start.sh
WORKDIR /shadowsocksr
ENTRYPOINT ["/root/start.sh"]
CMD /root/start.sh