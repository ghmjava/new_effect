#coding:utf-8
from flask import Flask, session, redirect, url_for, escape, request, render_template
import os,commands

from functools import partial
import traceback
import os,sys,re
import json
import urllib,urllib2
import time,datetime
import base64
from write_html import write_html
from collections import OrderedDict
import threading


app = Flask(__name__)

#设置index路由处理启动docker服务
@app.route('/user/<timeout>') 
def index(timeout):
	print timeout
	code=request.args.get('code')
	print code
        if code:
                print code
                access_token_url="""curl http://apitest.speed.meilishuo.com/oauth/access_token -d 'client_id=100001&client_secret=543774710dcc91a7e52428bf02ac8c41&grant_type=authorization_code&redirect_uri=http://localhost:8000/login&code=%s'""" % code
                cmd_re=os.popen(access_token_url).read()
                access_token_json=json.loads(cmd_re)
                #access_token_dumps=json.dumps(access_token_json,ensure_ascii=False)
                access_token=access_token_json['access_token']
                check_access_token="""curl http://apitest.speed.meilishuo.com/oauth/statuses -d 'client_id=100001&access_token=%s' """ % access_token
                cmd_re=os.popen(check_access_token).read()
                check_access_token_status=json.loads(cmd_re)
                check_status=check_access_token_status['code']
                check_mail =check_access_token_status['data']['mail']
		
	if 'gemini' in session:
		libsrc="http://svn.meilishuo.com/repos/meilishuo/middleware/libsrc"
		gemini=session['gemini']
		image_service="http://svn.meilishuo.com/repos/meilishuo/middleware/image_service"
		os.system('echo'+' '+gemini+' '+'>>/home/work/hongmingguo/myproject/count.txt')
		os.system('docker ps -q >/home/work/hongmingguo/myproject/num.txt')
		num=len(open('/home/work/hongmingguo/myproject/count.txt','rU').readlines())
		ps_num = len(open('/home/work/hongmingguo/myproject/num.txt','rU').readlines())
		if ps_num <=12 :
			count = len(open('/home/work/hongmingguo/myproject/count.txt','rU').readlines())
			#(status, output) = commands.getstatusoutput('docker ps -l -q')
			os.system('docker run --net=host -idt -v /home/work/conf/real/bj/mysql/online:/home/work/conf/real/bj/mysql/online -v /home/work/conf/real/jxq/mysql/qalab:/home/work/conf/mysql -v /home/work/jianhaowei/config:/home/index -v /home/dev/5001:/home/work centos:20151128')
			(status, output) = commands.getstatusoutput('docker ps -l -q')
			port  =5000+count
			port1 =5100+count
			port2 =5200+count
			#timestart=time.time()
			starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			print starttime
			os.system('rm -rf /home/work/hongmingguo/myproject/log/"%s".txt'%timeout)
			#os.system('touch /home/work/hongmingguo/myproject/log/"%s".txt'%timeout)
			os.system('touch /home/work/hongmingguo/myproject/log/"%s".txt'%timeout)
			print output
			commit='docker exec -ti %s /bin/bash -c "source /home/goodslistgetter/startGLS.sh %s %s %s %s %s %s">>/home/work/hongmingguo/myproject/log/%s.txt'%(output,libsrc,gemini,image_service,port,port1,port2,timeout)
			print commit
			os.popen(commit)
			os.system('rm -rf /home/work/hongmingguo/myproject/templates/result/"%s"_result.html'%timeout)
			os.system('touch /home/work/hongmingguo/myproject/templates/result/"%s"_result.html'%timeout)
			file_path="/home/work/hongmingguo/myproject/templates/result/%s_result.html"%timeout
			fp = file(file_path,'a+')
			#starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
			#url ="http://172.16.0.18:8080/api/poster_statistics?page_num=1&ip=10.6.3.113&port=%d"%port
			url="http://172.16.1.23:8080/api/poster_statistics?page_num=1&ip=10.6.3.113&port=%s"%port
			print url
			myjson=json.loads(urllib.urlopen(url).read())
			print myjson

			iport="IP:10.6.3.113  port :%d"%port
			
			fp.write(iport+'<br/>开始时间:'+starttime+'<br/>耗时:<br/>0ERROR pid:<br/>all request:1<br/>')
			fp.write('<html lang="zh-cn" slick-uniqueid="3"><head><link rel="stylesheet" href="http://cdn.bootcss.com/twitter-bootstrap/3.0.3/css/bootstrap.min.css"><meta charset="utf-8"><title>debug</title><style type="text/css">::selection{ background-color: #E13300; color: white; }::moz-selection{ background-color: #E13300; color: white; }::webkit-selection{ background-color: #E13300; color: white; }code {font-family: Consolas, Monaco, Courier New, Courier, monospace;font-size: 12px;background-color: #f9f9f9;border: 1px solid #D0D0D0;color: #002166;display: block;margin: 8px 0 8px 0;padding: 8px 8px 8px 8px;}body {background-color: #fff;margin: 40px;font: 13px/20px normal Helvetica, Arial, sans-serif;color: #4F5155;}#body{margin: 0 15px 0 15px;}#container{margin: 10px;border: 1px solid #D0D0D0;-webkit-box-shadow: 0 0 8px #D0D0D0;}td{width:2px;}</style><body style=""><div id="container"><div class="bs-example"> <table class="table table-hover"><tr><td><br/>第一页:</td><td></td></tr><tr><td align="center">评分标准</td><td>分值</td></tr>')
			for i in myjson['160'].keys():
				print i
				#la=json.dumps[i,ensure_ascii=False]
				kk=myjson["160"][i]
				ll=json.dumps(i,ensure_ascii=False)
				print ll.encode('utf-8')
				fp.write('<tr><td align="center">'+ll.encode('utf-8')+'</td><td>'+str(kk)+'</td></tr>')
			fp.write('<tr><td><br/>前两帧:</td><td></td></tr>')
			for m in myjson['60'].keys():
                                ks=myjson["60"][m]
                                lk=json.dumps(m,ensure_ascii=False)
                                fp.write('<tr><td align="center">'+lk.encode('utf-8')+'</td><td>'+str(ks)+'</td></tr>')
			fp.write('</table> </div></body></html>')
			os.system('docker stop'+' '+output)
			os.system('docker rm'+' '+output)
			
			result="%s_result.html"%timeout
			return redirect(url_for('rely',result=result))
			#result="result/%s_result.html"%timecode
			#return render_template(result)
			#return 'IP Port and ID: 10.6.3.113   %s  %s' % (escape(port),escape(output))
		else :
			return 'Start number over 12 please wait'
		#return 'You are not logged in'

@app.route('/index')
def indexii():
	username=111
	timecode=starttime()
	return render_template('index.html',username=username,timecode=timecode)


#登录首页
@app.route('/login', methods=['GET', 'POST'])
def login():
	#timeout =time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
	#timecode=timeout
	#timecode=starttime()
	code=request.args.get('code')
        if code:
		print code
		timecc=starttime()
                #access_token_url="""curl http://apitest.speed.meilishuo.com/oauth/access_token?client_id=100001&client_secret=543774710dcc91a7e52428bf02ac8c41&grant_type=authorization_code&redirect_uri=10.6.3.113:5077/login&code=%s""" % code
                #cmd_re=os.popen(access_token_url).read()
                #access_token_json=json.loads(cmd_re)
		#access_token_dumps=json.dumps(access_token_json,ensure_ascii=False)
                #access_token=access_token_json['access_token']
                #check_access_token="""curl http://apitest.speed.meilishuo.com/oauth/statuses?client_id=100001&access_token=%s' """ % access_token
                #cmd_re=os.popen(check_access_token).read()
                #check_access_token_status=json.loads(cmd_re)
                #check_status=check_access_token_status['code']
		#check_mail =check_access_token_status['data']['mail']
			
		#print check_mail
		#print check_status
		#os.system('echo '+check_mail+'>>/home/work/hongmingguo/effect_valuation/peoplecode.txt')
		#user_name=os.popen('tail -1 /home/work/hongmingguo/effect_valuation/peoplecode.txt').read()
		#print user_name
		#return render_template('login.html',username=user_namecodei,timecode=timecc)
	
	
	system=len(open('/home/work/hongmingguo/effect_valuation/people.txt','rU').readlines())
	sys=len(open('/home/work/hongmingguo/effect_valuation/peoplecode.txt','rU').readlines())
	if system==sys:
		return render_template('speedLogin.html')
	if request.method == 'POST':
		timeaa=open('/home/work/hongmingguo/effect_valuation/time.txt').readlines()[-1].strip('\n')
		print timeaa
		user_name=os.popen('tail -1 /home/work/hongmingguo/effect_valuation/peoplecode.txt').read()
		user_namecode=user_name.replace('@meilishuo.com','')
		session['gemini']=request.form['gemini']
		session['IP']=request.form['IP'] 
		session['PORT']=request.form['PORT']
		session['tests']=request.form['tests']
		session['page_num']=request.form['page_num']
		session['sort']=request.form['sort']
		print session['sort']
		if len(session['gemini']) == 0:
			print session['sort']
			return redirect(url_for('login_iport',timecode=timeaa))		
		else:
			return redirect(url_for('index',timeout=timeaa))
	user_name=os.popen('tail -1 /home/work/hongmingguo/effect_valuation/peoplecode.txt').read()
	user_namecode=user_name.replace('@meilishuo.com','')
	#user_nametime='%s%s'%(user_namecode,timecode)
	print user_name
	print user_namecode
	#print user_nametime
	timecode=starttime()
	print timecode
	os.system('echo "%s" >/home/work/hongmingguo/effect_valuation/time.txt'%timecode)
	print timecode
	return render_template('login.html',username=user_namecode,timecode=timecode)

#处理请求，发送url获取json并解析
@app.route('/login_iport/<timecode>')
def login_iport(timecode):
	print timecode
	if 'IP' in session:
		IP=session['IP']
		PORT=session['PORT']
		tests=session['tests']
		page_num=session['page_num']
		sort=session['sort']
		print sort
		os.system('rm -rf /home/work/hongmingguo/effect_valuation/templates/result/%s_result.html'%timecode)
		os.system('touch /home/work/hongmingguo/effect_valuation/templates/result/%s_result.html'%timecode)
		file_path='/home/work/hongmingguo/effect_valuation/templates/result/%s_result.html'%timecode
		fs = file(file_path,'a+')
		starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		time_start=time.time()
		#iport=os.popen('sh /home/work/hongmingguo/myproject/double_iport.sh'+' '+IP+' '+PORT+' '+tests+' '+page_num).read()
		url="http://10.8.20.18:8080/api/poster_statistics?page_num=%s&ip=%s&port=%s&tests=%s&sort=%s"%(page_num,IP,PORT,tests,sort)
		print url
		time_end=time.time()
		#print iport
		iport_json=json.loads(urllib.urlopen(url).read(),object_pairs_hook=OrderedDict)
		iport_json_keys_160=iport_json['160'].keys()
		iport_json_keys_60=iport_json['60'].keys()
		print iport_json_keys_160
		print iport_json_keys_60
		time_total=time_start-time_end
		#starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		#将获取到结果展示
		fs.write('IP PORT:'+IP+' '+PORT+' '+tests+'<br/>开始时间:'+starttime+'<br/>耗时:'+str(time_total)+'<br/>')
		fs.write('<a href="javascript :;"onClick="javascript :history.back(-1);">返回上一页</a><br/>')
		fs.write('<html lang="zh-cn" slick-uniqueid="3"><head><link rel="stylesheet" href="http://cdn.bootcss.com/twitter-bootstrap/3.0.3/css/bootstrap.min.css"><meta charset="utf-8"><title>debug</title><style type="text/css">::selection{ background-color:         #E13300; color: white; }::moz-selection{ background-color: #E13300; color: white; }::webkit-selection{ background-color: #E13300; color: white; }code {font-family: Consolas, Monaco, Courier New, Courier, monospace;font-size: 12px;background-color: #f9f9f9;border:         1px solid #D0D0D0;color: #002166;display: block;margin: 8px 0 8px 0;padding: 8px 8px 8px 8px;}body {background-color: #fff;margin: 40px;font: 13px/20px normal Helvetica, Arial, sans-serif;color: #4F5155;}#body{margin: 015px 015px;}#container{margin: 10px;border:         1px solid #D0D0D0;-webkit-box-shadow: 0 0 8px #D0D0D0;}td{width:2px;}</style><body style=""><div id="container"><div class="bs-example"> <table class="table table-hover"><tr><td><br/>前两帧:</td><td></td></tr><tr><td align="center">评分标准</td><td>分值</td></tr>')
		for ip in iport_json_keys_60:
			iport_dumps_160=json.dumps(ip,ensure_ascii=False)
			iport_dumps_160 = re.sub('"(.*?)"',r'\1',iport_dumps_160)
			IP=iport_json['60'][ip]
			fs.write('<tr><td align="center">'+iport_dumps_160.encode('utf-8')+'</td><td>'+str(IP)+'</td></tr>')
		fs.write('<tr><td><br/>第一页:</td><td></td></tr>')
		for port in iport_json_keys_160:
			iport_dumps_60=json.dumps(port,ensure_ascii=False)
			iport_dumps_60 = re.sub('"(.*?)"',r'\1',iport_dumps_60)
			PORT=iport_json['160'][port]
			fs.write('<tr><td align="center">'+iport_dumps_60.encode('utf-8')+'</td><td>'+str(PORT)+'</td></tr>')
		fs.write('</table> </div></body></html>')
		result="%s_result.html"%timecode
                return redirect(url_for('rely',result=result))
		


def starttime():
	timeout =time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        timecode=timeout
	return timecode

#结果页面
@app.route('/result/<result>')
def rely(result):
	#if request.method == 'POST':
	#html=result
	#print html
	return render_template('result/%s'%result)

#效果对比首页
@app.route('/double/<username>', methods=['GET', 'POST'])
def double(username):
	#timecode =time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
        if request.method == 'POST':
		timeout =open('/home/work/hongmingguo/effect_valuation/doubletime.txt').readlines()[-1].strip('\n')
                session['gemini']=request.form['gemini']
                session['gemini1']=request.form['gemini1']
		session['IP']=request.form['IP']
		session['PORT']=request.form['PORT']
		session['tests']=request.form['tests']
		session['ipone']=request.form['ipone']
		session['portone']=request.form['portone']
		session['testsone']=request.form['testsone']
		session['page_num']=request.form['page_num']
		session['page_num_one']=request.form['page_num_one']
		session['sort']=request.form['sort']
		session['sort_one']=request.form['sort_one']
		print session['IP']
		print session['PORT']
                #if len(session['gemini']) == 0:
                #        return render_template('login1.html',timecode=timeout,username=username)
                #elif len(session['PORT']) == 0:
		#	return render_template('login1.html',temcode=timeout,username=username)
		#elif len(session['PORT']) == 0:
                #return redirect(url_for('double_index',timecode=timeout))
		if len(session['gemini']) ==0:
			return redirect(url_for('double_iport',timecode=timeout,username=username))
		else:
			return redirect(url_for('double_index',timecode=timeout))
	timecode=starttime()
	os.system('echo "%s" >/home/work/hongmingguo/effect_valuation/doubletime.txt'%timecode)
        return render_template('login1.html',timecode=timecode,username=username)
#效果对比页面处理
@app.route('/double_iport/<timecode><username>')
def double_iport(timecode,username):
	if 'IP' in  session:
		IP=session['IP']
		PORT=session['PORT']
		tests=session['tests']
		page_num=session['page_num']
		ipone=session['ipone']
		portone=session['portone']
		testsone=session['testsone']
		page_num_one=session['page_num_one']
		sort=session['sort']
		sort_one=session['sort_one']
		starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
		time_start=time.time()
		#IP_cmd='sh /home/work/hongmingguo/myproject/double_iport.sh'+' '+IP+' '+PORT+' '+tests+' '+page_num
		#PORT_cmd='sh /home/work/hongmingguo/myproject/double_iport.sh'+' '+ipone+' '+portone+' '+testsone+' '+page_num_one
		#print IP_cmd
		#print PORT_cmd
		#cmds=['sh /home/work/hongmingguo/myproject/double_iport.sh'+' '+IP+' '+PORT+' '+tests+' '+page_num +'> /home/work/hongmingguo/myproject/IP_cmd/'+timecode+'.txt','sh /home/work/hongmingguo/myproject/double_iport.sh'+' '+ipone+' '+portone+' '+testsone+' '+page_num_one+'>/home/work/hongmingguo/myproject/PORT_cmd/'+timecode+'.txt',]
		cmds=['sh /home/work/hongmingguo/effect_valuation/double_iport.sh'+' '+IP+' '+PORT+' '+tests+' '+page_num+' '+sort+' '+'IP_cmd'+' '+timecode,'sh /home/work/hongmingguo/effect_valuation/double_iport.sh'+' '+ipone+' '+portone+' '+testsone+' '+page_num_one+' '+sort_one+' '+'PORT_cmd'+' '+timecode]
		#线程池
		threads=[]
		print "程序开始运行%s" % datetime.datetime.now()
		for cmd in cmds:
        		th = threading.Thread(target=execCmd, args=(cmd,))
        		th.start()
        		threads.append(th)
         		print cmd	
		#print threads
   		 # 等待线程运行完毕
    		for th in threads:
        		th.join()
		print "程序结束运行%s" % datetime.datetime.now()



		double_IP=os.popen('cat /home/work/hongmingguo/effect_valuation/IP_cmd/'+timecode+'.txt').read()
		double_PORT=os.popen('cat /home/work/hongmingguo/effect_valuation/PORT_cmd/'+timecode+'.txt').read()
		time_end=time.time()
		IP_json=json.loads(double_IP,object_pairs_hook=OrderedDict)
		PORT_json=json.loads(double_PORT,object_pairs_hook=OrderedDict)
		IP_json_keys_160=IP_json['160'].keys()
		IP_json_keys_60=IP_json['60'].keys()
		PORT_json_keys_160=PORT_json['160'].keys()
		PORT_json_keys_60=PORT_json['60'].keys()
		if len(PORT_json_keys_160) == 0:
			return redirect(url_for('double',username=username))
		os.system('rm -rf /home/work/hongmingguo/effect_valuation/templates/double/%s.html'%timecode)
		os.system("touch /home/work/hongmingguo/effect_valuation/templates/double/%s.html"%timecode)
		file_path="/home/work/hongmingguo/effect_valuation/templates/double/%s.html"%timecode
		fp = file(file_path,'a+')
		time_total=time_end-time_start
		fp.write('开始时间:'+starttime+'<br/>耗时:'+str(time_total)+'<br/>')
		fp.write('测试组：<br/>host:'+ipone+'<br/>port:'+portone+'<br/>tests:'+testsone+'<br/>poster_num:'+page_num_one+'<br/>')
		fp.write('对照组：<br/>host:'+IP+'<br/>port:'+PORT+'<br/>tests:'+tests+'<br/>poster_num:'+page_num+'<br/>')
		fp.write('<a href="javascript :;"onClick="javascript :history.back(-1);">返回上一页</a><br/>')
                fp.write('<html lang="zh-cn" slick-uniqueid="3"><head><link rel="stylesheet" href="http://cdn.bootcss.com/twitter-bootstrap/3.0.3/css/bootstrap.min.css"><meta charset="utf-8"><title>debug</title><style type="text/css">::selection{ background-color: #E13300; color: white; }::moz-selection{ background-color: #E13300; color: white; }::webkit-selection{ background-color: #E13300; color: white; }code {font-family: Consolas, Monaco, Courier New, Courier, monospace;font-size: 12px;background-color : #f9f9f9;border: 1px solid #D0D0D0;color: #002166;display: block;margin: 8px 0 8px 0;padding: 8px 8px 8px 8px;}body {background-color: #fff;margin: 40px;font: 13px/20px nor mal Helvetica, Arial, sans-serif;color: #4F5155;}#body{margin: 0 15px 0 15px;}#container{margin: 10px;border: 1px solid #D0D0D0;-webkit-box-shadow: 0 0 8px #D0D0D0;}td{width :2px;}</style><body style=""><div id="container"><div class="bs-example"> <table class="table table-hover"<tr><td align="center">评分标准</td><td align="center">'+'测试组：'+'</td><td align="center">'+'对照组：'+'</td><td align="center">差值</td><td align="center">百分比</td></tr><tr><td><br/>第一页:</td><td></td><td></td><td></td><td></td></tr>')
		for ip in PORT_json_keys_160:
			ip_up=json.dumps(ip,ensure_ascii=False)
			ip_up = re.sub('"(.*?)"',r'\1',ip_up)
			#测试IP
			ip_one=IP_json['160'][ip]
			#实验IP
			ip_two=PORT_json['160'][ip]
			ip_total=ip_two-ip_one
			if ip_total == 0:
				ip_percent = 0
			elif ip_two ==0:
				ip_percent = 0
			else:
				ip_percent="%3f%%"%(abs(ip_total)/ip_one*100)
			if  ip_percent >= "2%" and ip_total >=0:
				fp.write('<tr><td align="center">'+ip_up.encode('utf-8')+'</td><td align="center">'+str(ip_two)+'</td><td align="center">'+str(ip_one)+'</td><td align="center"><font color="red">'+str(ip_total)+'</font></td><td align="center"><font color="red">'+str(ip_percent)+'</font></td></tr>')
			elif ip_percent >= "2%" and ip_total <0:
				fp.write('<tr><td align="center">'+ip_up.encode('utf-8')+'</td><td align="center">'+str(ip_two)+'</td><td align="center">'+str(ip_one)+'</td><td align="center"><font color="green">'+str(ip_total)+'</font></td><td align="center"><font color="green">'+'-'+str(ip_percent)+'</font></td></tr>')
			#elif ip_percent >= "2%" and ip_total > 0:
				#fp.write('<tr><td align="center">'+ip_up.encode('utf-8')+'</td><td align="center">'+str(ip_two)+'</td><td align="center">'+str(ip_one)+'</td><td align="center"><font color="red">'+str(ip_total)+'</font></td><td align="center"><font color="red">'+str(ip_percent)+'</font></td></tr>')
			else :
				if ip_total >=0:
					fp.write('<tr><td align="center">'+ip_up.encode('utf-8')+'</td><td align="center">'+str(ip_two)+'</td><td align="center">'+str(ip_one)+'</td><td align="center">'+str(ip_total)+'</td><td align="center">'+str(ip_percent)+'</td></tr>')
				else:
					fp.write('<tr><td align="center">'+ip_up.encode('utf-8')+'</td><td align="center">'+str(ip_two)+'</td><td align="center">'+str(ip_one)+'</td><td align="center">'+str(ip_total)+'</td><td align="center">'+'-'+str(ip_percent)+'</td></tr>')
		fp.write('<tr><td><br/>前两帧:</td><td></td><td></td><td></td><td></td></tr>')
		for port in PORT_json_keys_60:
			port_up=json.dumps(port,ensure_ascii=False)
			port_up = re.sub('"(.*?)"',r'\1',port_up)
			port_one=IP_json['60'][port]
			port_two=PORT_json['60'][port]
			port_total=port_two-port_one
			if port_total == 0:
				port_percent = 0
			elif port_two == 0:
				port_percent = 0
			else:
				port_percent = "%3f%%"%(abs(port_total)/port_one*100)
			if port_total < 0 and port_percent > "2%":
				fp.write('<tr><td align="center">'+port_up.encode('utf-8')+'</td><td align="center">'+str(port_two)+'</td><td align="center">'+str(port_one)+'</td><td align="center"><font color="green">'+str(port_total)+'</td><td align="center"><font color="green">'+'-'+str(port_percent)+'</td></tr>')
			elif port_total > 0 and port_percent >"2%":
				fp.write('<tr><td align="center">'+port_up.encode('utf-8')+'</td><td align="center">'+str(port_two)+'</td><td align="center">'+str(port_one)+'</td><td align="center"><font color="red">'+str(port_total)+'</font></td><td align="center"><font color="red">'+str(port_percent)+'</font></td></tr>')
			else :
				if port_total >= 0:
					fp.write('<tr><td align="center">'+port_up.encode('utf-8')+'</td><td align="center">'+str(port_two)+'</td><td align="center">'+str(port_one)+'</td><td align="center">'+str(port_total)+'</td><td align="center">'+str(port_percent)+'</td></tr>')
				else:
					fp.write('<tr><td align="center">'+port_up.encode('utf-8')+'</td><td align="center">'+str(port_two)+'</td><td align="center">'+str(port_one)+'</td><td align="center">'+str(port_total)+'</td><td align="center">'+"-"+str(port_percent)+'</td></tr>')
		fp.write('</table> </div></body></html>')


		doubleresult="%s.html"%timecode
		return redirect(url_for('double_result',doubleresult=doubleresult))	
		



def execCmd(cmd):
    try:
        print "命令%s开始运行%s" % (cmd,datetime.datetime.now())
       	os.system(cmd)
        print "命令%s结束运行%s" % (cmd,datetime.datetime.now())
    except Exception, e:
        print '%s\t 运行失败,失败原因\r\n%s' % (cmd,e)



#启动docker并处理页面逻辑
@app.route('/double_index/<timecode>')
def double_index(timecode):
	if 'gemini' in session:
                #user=session['username']
                #libsrc=session['libsrc']
		libsrc="http://svn.meilishuo.com/repos/meilishuo/middleware/libsrc"
                image_service="http://svn.meilishuo.com/repos/meilishuo/middleware/image_service"
                geminione=session['gemini']
		geminitwo=session['gemini']
                #image_service=session['image_service']
                os.system('echo'+' '+geminione+' '+'>>/home/work/hongmingguo/effect_valuation/count.txt')
		os.system('echo'+' '+geminitwo+' '+'>>/home/work/hongmingguo/effect_valuation/count.txt')
                os.system('docker ps -q >/home/work/hongmingguo/effect_valuation/num.txt')
                numtwo = len(open('/home/work/hongmingguo/effect_valuation/num.txt','rU').readlines())
		numone=numtwo -1
		
                if numtwo <=12 :
                        counttwo = len(open('/home/work/hongmingguo/effect_valuation/count.txt','rU').readlines())
			countone = counttwo -1
                        os.system('docker run --net=host -idt -v /home/work/conf/real/bj/mysql/online:/home/work/conf/real/bj/mysql/online -v /home/work/conf/real/jxq/mysql/qalab:/home/work/conf/mysql -v /home/work/jianhaowei/config:/home/index centos:20151128')
                        (statusone, outputone) = commands.getstatusoutput('docker ps -l -q')
                        port  =5000+countone
                        porta =5100+countone
                        portb =5200+countone
			portc =5000+counttwo
			portd =5100+counttwo 
			porte =5200+counttwo
			
			
			os.system('rm -rf /home/work/hongmingguo/myproject/doublelog/%s.txt'%timecode)
			os.system('touch /home/work/hongmingguo/myproject/doublelog/%s.txt'%timecode)
			commitone='docker exec -ti %s /bin/bash -c "source /home/goodslistgetter/startGLS.sh %s %s %s %d %d %d">>/home/work/hongmingguo/myproject/doublelog/%s.txt'%(outputone,libsrc,geminione,image_service,port,porta,portb,timecode)		

                        os.system(commitone)
                        

			os.system('docker run --net=host -idt -v /home/work/conf/real/bj/mysql/online:/home/work/conf/real/bj/mysql/online -v /home/work/conf/real/jxq/mysql/qalab:/home/work/conf/mysql -v /home/work/jianhaowei/config:/home/index centos:20151128')
			(statustwo, outputtwo) = commands.getstatusoutput('docker ps -l -q')


			committwo='docker exec -ti %s /bin/bash -c "source /home/goodslistgetter/startGLS.sh %s %s %s %d %d %d">>/home/work/hongmingguo/myproject/doublelog/%s.txt'%(outputtwo,libsrc,geminitwo,image_service,portc,portd,porte,timecode)
			os.system(committwo)


			os.system('rm -rf /home/work/hongmingguo/myproject/templates/double/%s.html'%timecode)
                        os.system("touch /home/work/hongmingguo/myproject/templates/double/%s.html"%timecode)
                        file_path="/home/work/hongmingguo/myproject/templates/double/%s.html"%timecode
                        fp = file(file_path,'a+')
			starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                        urlone ="http://172.16.0.18:8080/api/poster_statistics?page_num=1&ip=10.6.3.113&port=%d"%port
                        myjsonone=json.loads(urllib.urlopen(urlone).read())
                        newjsonone=json.dumps(myjsonone,ensure_ascii=False)
                        

			urltwo="http://172.16.1.23:8080/api/poster_statistics?page_num=1&ip=10.6.3.113&port=%d"%portc
			myjsontwo=json.loads(urllib.urlopen(urltwo).read())
			

			iportone="IP=10.6.3.113 port=%d"%port
			iporttwo="IP=10.6.3.113 port=%d"%portc

			
			fp.write('开始时间:'+starttime+'<br/>耗时:5.43811297417<br/>0ERROR pid:<br/>all request:1<br/>')
                        fp.write('<html lang="zh-cn" slick-uniqueid="3"><head><link rel="stylesheet" href="http://cdn.bootcss.com/twitter-bootstrap/3.0.3/css/bootstrap.min.css"><meta charset="utf-8"><title>debug</title><style type="text/css">::selection{ background-color: #E13300; color: white; }::moz-selection{ background-color: #E13300; color: white; }::webkit-selection{ background-color: #E13300; color: white; }code {font-family: Consolas, Monaco, Courier New, Courier, monospace;font-size: 12px;background-color: #f9f9f9;border: 1px solid #D0D0D0;color: #002166;display: block;margin: 8px 0 8px 0;padding: 8px 8px 8px 8px;}body {background-color: #fff;margin: 40px;font: 13px/20px normal Helvetica, Arial, sans-serif;color: #4F5155;}#body{margin: 0 15px 0 15px;}#container{margin: 10px;border: 1px solid #D0D0D0;-webkit-box-shadow: 0 0 8px #D0D0D0;}td{width:2px;}</style><body style=""><div id="container"><div class="bs-example"> <table class="table table-hover"><tr><td><br/>第一页:</td><td></td></tr><tr><td align="center">评分标准</td><td>'+iportone+'</td><td>'+iporttwo+'</td><td>差值</td><td>百分比</td></tr>')
                        for i in myjsonone['160']:
                                kk=myjsonone['160'][i]
				mm=myjsontwo['160'][i]
				doubleone=kk-mm
				if doubleone==0:
					percentone=0
				else:
					percentone="%.3f%%" % (abs(doubleone)/kk*100)
                                ll=json.dumps(i,ensure_ascii=False)
				if doubleone < 0:
					fp.write('<tr><td align="center">'+ll.encode('utf-8')+'</td><td>'+str(kk)+'</td><td>'+str(mm)+'</td><td><font color="green">'+str(doubleone)+'</td><td><font color="green">'+str(percentone)+'</td></tr>')
                                elif doubleone ==0 :
					fp.write('<tr><td align="center">'+ll.encode('utf-8')+'</td><td>'+str(kk)+'</td><td>'+str(mm)+'</td><td>'+str(doubleone)+'</td><td>'+str(percentone)+'</td></tr>')
				elif doubleone >0 :
					 fp.write('<tr><td align="center">'+ll.encode('utf-8')+'</td><td>'+str(kk)+'</td><td>'+str(mm)+'</td><td><font color="red">'+str(doubleone)+'</td><td><font color="red">'+str(percentone)+'</td></tr>')
                        fp.write('<tr><td><br/>前两帧:</td><td></td></tr>')
                        for m in myjsonone['60']:
                                ww=myjsonone['60'][m]
				ee=myjsontwo['60'][m]
				doubletwo=ww-ee
				if doubletwo==0:
					percenttwo=0
				else:
					percenttwo="%3f%%"%(abs(doubletwo)/ww*100)
                                qw=json.dumps(m,ensure_ascii=False)
				if doubletwo < 0:
					fp.write('<tr><td align="center">'+qw.encode('utf-8')+'</td><td>'+str(ww)+'</td><td>'+str(ee)+'</td><td style="background-color:rgb(255,69,0)">'+str(doubletwo)+'</td><td style="background-color:rgb(255,69,0)">'+str(percenttwo)+'</td></tr>')
                                else:
					fp.write('<tr><td align="center">'+qw.encode('utf-8')+'</td><td>'+str(ww)+'</td><td>'+str(ee)+'</td><td>'+str(doubletwo)+'</td><td>'+str(percenttwo)+'</td></tr>')
                        fp.write('</table> </div></body></html>')
			os.system('docker stop'+' '+outputone)
			os.system('docker stop'+' '+outputtwo)
			os.system('docker rm'+' '+outputone)
			os.system('docker rm'+' '+outputtwo)

			doubleresult="%s.html"%timecode
			return redirect(url_for('double_result',doubleresult=doubleresult))
                        #return render_template('doubleresult.html')
                        #return 'IP Port and ID: 10.6.3.113   %s  %s' % (escape(port),escape(output))
                else :
                        return 'Start number over 12 please wait'
                #return 'You are not logged in'
#历史页面的展示
@app.route('/historytotal/<username>')
def history_total(username):
	return render_template('HistoryTotal.html',username=username)



#效果对比历史页面
@app.route('/doublehistory')
def double_history():
	history=os.listdir('/home/work/hongmingguo/effect_valuation/templates/double/')
	history.sort(reverse = True)
        os.system('rm -rf /home/work/hongmingguo/effect_valuation/templates/doublehistory.html')
        os.system('touch  /home/work/hongmingguo/effect_valuation/templates/doublehistory.html')
        fp_file="/home/work/hongmingguo/effect_valuation/templates/doublehistory.html"
        fp=file(fp_file,"a+")
        for his in history:
                fp.write('<p><a href="/doubleresult/%s" target="_blank">%s<p>'%(his,his))
        #return render_template('history.html')
        return redirect(url_for('doublehistory_code'))

@app.route('/doublehistorycode')
def doublehistory_code():
	return render_template('doublehistory.html')



@app.route('/doubleresult/<doubleresult>')
def double_result(doubleresult):
        #if request.method == 'POST':
	print doubleresult	
        return render_template('double/%s'%doubleresult)

#日志
@app.route('/doublelog/<timecode>')
def double_log(timecode):
	double_log=os.popen('cat doublelog/%s.txt'%timecode).read()
	return render_template('doublelog.html',login_log=double_log)


#speed登录
@app.route('/speed')
def speed():
	return render_template('speedLogin.html')



@app.route('/history')
def history():
	history=os.listdir('/home/work/hongmingguo/effect_valuation/templates/result/')
	history.sort(reverse = True)
	os.system('rm -rf /home/work/hongmingguo/effect_valuation/templates/history.html')
	os.system('touch  /home/work/hongmingguo/effect_valuation/templates/history.html')
	fp_file="/home/work/hongmingguo/effect_valuation/templates/history.html"
	fp=file(fp_file,"a+")
	for his in history:
		fp.write('<p><a href="/result/%s" target="_blank">%s<p>'%(his,his))
	#return render_template('history.html')
	return redirect(url_for('history_code'))


@app.route('/historycode')
def history_code():
	return render_template('history.html')

@app.route('/log/<timecode>')
def log(timecode):
	login_log=os.popen('cat log/%s.txt'%timecode).read()
	return render_template('doublelog.html',login_log=login_log)

#diff工具页面
@app.route('/diff/<username>')
def diff(username):
	return render_template('Diff.html',username=username)
#diff性能工具
@app.route('/diffpress/<username>')
def diffpress(username):
    return render_template('DiffPress.html',username=username)
#使用人
@app.route('/people/<username>')
def people(username):
	os.system('docker ps >/home/work/hongmingguo/effect_valuation/people.txt')
	os.system('sh /home/work/hongmingguo/effect_valuation/people.sh')
	return render_template('people.html',username=username)
	
#重新登录
@app.route('/logout') 
def logout():
	# remove the username from the session if its there
	session.pop('username', None) 
	return redirect(url_for('index'))
# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
	app.debug = True 
	app.run(host='0.0.0.0',port=5077)
