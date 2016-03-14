#!/bin/bash

echo '<meta http-equiv="refresh" content="15">'>/home/work/hongmingguo/myproject/templates/doublelog.html

cat doublelog.txt | while read line
do
          echo $line'</br>' >>/home/work/hongmingguo/myproject/templates/doublelog.html
done
