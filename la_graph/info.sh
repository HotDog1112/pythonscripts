#!/bin/bash
i=0
while [[ $i -le 10 ]]; do
a=`uptime | awk '{print $9}'`
b=`uptime | awk '{print $10}'`
c=`uptime | awk '{print $11}'`
current_time=`date +"%H:%M:%S"`
awc=${a%%,}
bwc=${b%%,}
echo $awc $bwc $c >> /home/kali/Desktop/scr/info
i=$(($i + 1))
sleep 5
done
