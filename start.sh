#!/bin/bash

rm -rf index.html
touch index.html
docker ps >1.log
sed -i '1d' 1.log

cat 1.log | while read line
do
          echo '<p>'$line'</p>' >>index.html
done
