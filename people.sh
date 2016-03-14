#!/bin/bash
echo '<!DOCTYPE html><html lang="zh-CN"><head>'>/home/work/hongmingguo/myproject/templates/people.html
echo '<meta http-equiv="refresh" content="5">'>>/home/work/hongmingguo/myproject/templates/people.html
echo '</head>'>>/home/work/hongmingguo/myproject/templates/people.html
echo '<table>'>>/home/work/hongmingguo/myproject/templates/people.html

sed -i 's/CONTAINER ID/使用中ID<\/td> /g'  people.txt
sed -i 's/IMAGE               COMMAND/ /g'  people.txt
#sed -i 's/centos:20151123     "\/bin\/bash"/<\/td><td>/g'  people.txt
sed -i 's/ago/ /g' people.txt
sed -i 's/Up/ /g' people.txt
sed -i 's/seconds/ seconds<\/td><td>/g' people.txt
sed -i 's/minutes/ minutes<\/td><td>/g' people.txt	
sed -i 's/hours/ hours<\/td><td>/g'  people.txt
sed -i 's/CREATED/ <td>创建时间<\/td>  /g' people.txt
sed -i 's/centos:20151128     "\/bin\/bash"/<\/td><td>/g'  people.txt
sed -i 's/STATUS/  <td>使用时间<\/td> /g' people.txt
sed -i 's/PORTS/  /g' people.txt
sed -i 's/NAMES/    <td>使用人 /g' people.txt
#sed -i 's/centos:20151123     "\/bin\/bash"/<\/td><td>/g'  people.txt

cat people.txt | while read line
do
          echo '<tr><td>' $line'</td></tr>' >>/home/work/hongmingguo/myproject/templates/people.html
done


echo '</table>'>>/home/work/hongmingguo/myproject/templates/people.html

echo '</html>'>>/home/work/hongmingguo/myproject/templates/people.html
