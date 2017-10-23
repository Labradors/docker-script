#!/bin/sh
echo -n "" > /root/rinetd.conf
while read line
do
        echo "0.0.0.0 $line 0.0.0.0 $line" >> /root/rinetd.conf
done < /root/mudb_port.txt

/root/rinetd_bbr_powered -f -c /root/rinetd.conf raw eth0 &
