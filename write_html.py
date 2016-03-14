#!/usr/bin/env python
#coding:utf-8
import sys,os
import time
import json
reload(sys)
sys.setdefaultencoding('utf8')
def write_html(result_json,html_path):
    #create a html file
    file_name=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))
    file_path="%s/%s.html"%(html_path,file_name)
    os.popen("touch %s"%(file_path))
    
    fp=open(file_path, 'a')
    os.popen("cat /dev/null > %s"%(file_path))

    #read result_json
    result_dict=json.loads(result_json)
    request_count=int(result_dict["request_count"])
    tids_count=int(result_dict["tids_count"])
    show_num_count=int(result_dict["show_num_count"])
    result_count=show_num_count
    if tids_count<show_num_count:
          result_count=tids_count
    #total
    fp.write("<!DOCTYPE html><html><head><meta http-equiv=\"Content Type\" content=\"text/html\" charset=\"utf-8\" /> <style>#container{margin-left: 20%;width:60%;margin-top: 50px;box-shadow: 10px 10px 5px;} #content{text-align: center;} body {}</style></head><body><div id=\"container\"><div id=\"content\"><table height=\"100px\" width=\"600px\" align=\"center\"><caption align=\"top\">结果信息</caption><tr>")
    
    result_percent=(0.0+request_count-result_count)/request_count
    show_num_percent=(0.0+request_count-show_num_count)/request_count
    tids_percent=(0.0+request_count-tids_count)/request_count

    fp.write("<td>总不同：%.2f</td><td>show_num不同：%.2f</td><td>tids不同：%.2f</td>.</tr><tr>"%(result_percent,show_num_percent,tids_percent))
    fp.write("<td>请求总数：%d</td><td>show_num相同数：%d</td><td>tids相同数：%d</td>"%(request_count,show_num_count,tids_count))

    fp.write("</tr></table></div></div><div id=\"container\"><div id=\"content\"><table height=\"100px\" width=\"600px\" align=\"center\"><caption align=\"top\">详细信息</caption>")
    fp.write("<tr><td>所有参数是否相同</td><td>shows_num是否相同</td><td>tids是否相同</td><td>query</td><td>show_num差值率</td><td>tids差值率</td><td>线上show_num数</td><td>线下show_num数</td><td>线上tids数</td><td>线下tids数</td><td>sort方法</td></tr>")
    #deail_info
    lines=result_dict["detail_info"]
    for line in lines:
        line_set=line.split("\t")
        if line_set[0]=="1":
            fp.write("<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(line_set[0],line_set[1],line_set[2],line_set[3],line_set[4],line_set[5],line_set[6],line_set[7],line_set[8],line_set[9],line_set[10]))
        else:
            fp.write("<tr bgcolor=#ff0000><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>"%(line_set[0],line_set[1],line_set[2],line_set[3],line_set[4],line_set[5],line_set[6],line_set[7],line_set[8],line_set[9],line_set[10]))

    fp.write("</table></div></div></body></html>")

    fp.close()
    return "%s.html"%(file_name)
