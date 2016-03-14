#!/bin/bash

time=$1

echo '<meta http-equiv="refresh" content="65">'>/home/work/hongmingguo/myproject/templates/$time.html

cat log/$time.txt | while read line
do
          echo $line'</br>' >>/home/work/hongmingguo/myproject/templates/$time.html
done
