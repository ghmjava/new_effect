#!/bin/bash

ip=$1
port=$2
tests=$3
page_num=$4
sort=$5
all=$6
timecode=$7

curl http://10.8.20.18:8080/api/poster_statistics?page_num=$page_num\&ip=$ip\&port=$port\&tests=$tests\&sort=$sort > $all/$timecode.txt
