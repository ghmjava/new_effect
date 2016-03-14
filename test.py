#coding:utf-8
import json,os,time,urllib
import base64


#url="http://172.16.0.18:8080/api/poster_statistics?page_num=1&ip=172.16.1.23&port=5020&tests=poster_ranking_1"

#myjson=json.loads(urllib.urlopen(url).read())
#newjson=json.dumps(myjson,ensure_ascii=False)

#for l in myjson['160'].keys:
#	m=myjson['160'][l]
#	print m





#js=json.loads('{"shop_dsr":"店铺平均dsr","cpc_shop_dsr":"cpc店铺平均dsr","nocpc_shop_dsr":"nocpc店铺平均dsr","shop_buy_again":"店铺平均复购率","shop_high_dsr":"店铺高dsr覆盖","shop_high_buy_again":"店铺高复购率覆盖","style_score_4":"款式4分","style_score_3":"款式3分","pic_score_4":"图片4分","pic_score_3":"图片3分","new_score":"平均上架时间","new_rate":"新品率","ecpm":"ecpm","boom_score":"平均热销分","boom_rate":"热销商品占比","avg_ctr":"平均ctr","ka_rate":"ka填充","shop_level_5":"5级商家占比","shop_level_4":"4级商家占比","shop_level_3":"3级商家占比","shop_level_2":"2级商家占比","shop_level_1":"1级商家占比","shop_level_0":"0级商家占比","area_n":"华北商家占比","area_s":"华南商家占比","area_e":"华东商家占比","price":"price","avg_dsr":"平均dsr","shop_service":"花花在线率","avg_intime_response_rate": "花花及时回复率","avg_first_response_time": "花花首次响应时间","avg_express_rate":"及时发货率","avg_reason_refund_rate": "有理由退款率","golden_fill_rate": "黄金橱窗填充率","top_fill_rate": "橱窗填充率","dacu_goods_rate": "915活动大促填充率","acg_fill":"推广商品填充率","avg_cpc_price":"cpc竞价单价","avg_cpc_price_gsp":"cpc竞价gsp","mark_rate":"打标新款填充","mark_rate_cpc":"cpc打标新款填充","mark_rate_nocpc":"nocpc打标新款填充","vip_fill_rate": "白名单店铺填充率","vip_fill_rate_cpc": "cpc 白名单店铺填充率","vip_fill_rate_nocpc": "nocpc 白名单店铺填充率","cs_shop_rate":"CS填充率","cs_shop_rate_cpc": "cpc CS填充率","cs_shop_rate_nocpc": "nocpc CS填充率","cheat_shop_rate":"作弊商家填充率"}')


#as=json.dumps(js,ensure_ascii=False)

#print (as)

#pagejson=json.loads('{"shop_dsr":"店铺平均dsr","cpc_shop_dsr":"cpc店铺平均dsr","nocpc_shop_dsr":"nocpc店铺平均dsr","shop_buy_again":"店铺平均复购率","shop_high_dsr":"店铺高dsr覆盖","shop_high_buy_again":"店铺高复购率覆盖","style_score_4":"款式4分","style_score_3":"款式3分","pic_score_4":"图片4分","pic_score_3":"图片3分","new_score":"平均上架时间","new_rate":"新品率","ecpm":"ecpm","boom_score":"平均热销分","boom_rate":"热销商品占比","avg_ctr":"平均ctr","ka_rate":"ka填充","shop_level_5":"5级商家占比","shop_level_4":"4级商家占比","shop_level_3":"3级商家占比","shop_level_2":"2级商家占比","shop_level_1":"1级商家占比","shop_level_0":"0级商家占比","area_n":"华北商家占比","area_s":"华南商家占比","area_e":"华东商家占比","price":"price","avg_dsr":"平均dsr","shop_service":"花花在线率","avg_intime_response_rate": "花花及时回复率","avg_first_response_time": "花花首次响应时间","avg_express_rate":"及时发货率","avg_reason_refund_rate": "有理由退款率","golden_fill_rate": "黄金橱窗填充率","top_fill_rate": "橱窗填充率","dacu_goods_rate": "915活动大促填充率","acg_fill":"推广商品填充率","avg_cpc_price":"cpc竞价单价","avg_cpc_price_gsp":"cpc竞价gsp","mark_rate":"打标新款填充","mark_rate_cpc":"cpc打标新款填充","mark_rate_nocpc":"nocpc打标新款填充","vip_fill_rate": "白名单店铺填充率","vip_fill_rate_cpc": "cpc 白名单店铺填充率","vip_fill_rate_nocpc": "nocpc 白名单店铺填充率","cs_shop_rate":"CS填充率","cs_shop_rate_cpc": "cpc CS填充率","cs_shop_rate_nocpc": "nocpc CS填充率","cheat_shop_rate":"作弊商家填充率"}')
#ls=pagejson.keys()
#print ls
#for i in ls:
#	print i
#	la=pagejson[i]
#	ll=json.dumps(la,ensure_ascii=False)
#	print (ll) 

#chinajson=json.dumps(ls,ensure_ascii=False)


#print (chinajson)

#print myjson.keys()
#print myjson["60"]["vip_fill_rate_cpc"]
#print newjson

#starttime=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))


#fp=file("2.log","a+")
#fp.write('平台:beaver<br/>开始时间:'+starttime+'<br/>耗时:5.43811297417<br/>0ERROR pid:<br/>all request:1<br/>')
#fp.write('<link rel="stylesheet" href="http://cdn.bootcss.com/twitter-bootstrap/3.0.3/css/bootstrap.min.css"><meta charset="utf-8"><title>debug</title><style type="text/css">::selection{ background-color: #E13300; color: white; }::moz-selection{ background-color: #E13300; color: white; }::webkit-selection{ background-color: #E13300; color: white; }code {font-family: Consolas, Monaco, Courier New, Courier, monospace;font-size: 12px;background-color: #f9f9f9;border: 1px solid #D0D0D0;color: #002166;display: block;margin: 8px 0 8px 0;padding: 8px 8px 8px 8px;}body {background-color: #fff;margin: 40px;font: 13px/20px normal Helvetica, Arial, sans-serif;color: #4F5155;}#body{margin: 0 15px 0 15px;}#container{margin: 10px;border: 1px solid #D0D0D0;-webkit-box-shadow: 0 0 8px #D0D0D0;}td{width:2px;}</style><body style=""><div id="container"><div class="bs-example"> <table class="table table-hover">')
#for i in ls:
#        la=pagejson[i]
#	kk=myjson["60"][i]
#        ll=json.dumps(la,ensure_ascii=False)
#	print ll
#	print kk
#        fp.write('<tr><td>'+ll.encode('utf-8')+'</td></tr><tr><td>'+str(kk)+'</td></tr>')

#fp.write('</table></div></body></html>')




#mmm=os.popen('sh test.sh').read()
#mq=json.loads(mmm)
#mm=mq['detail_info']
#for l in mm:
	#print l.encode('utf-8')
	#fp.write('<tr><td>'+l.encode('utf-8')+'</td></tr>')
	#ml=mq[l]
	#print ml
#print mmm

#history=os.listdir('/home/work/hongmingguo/myproject/templates/result/')
#print history
#for his in history:
#	print his

iport = os.popen('sh double_iport.sh goodslist-bj.meiliworks.com 80 poster_ranking_1 1').read()
print iport
iport_json=json.loads('%s'%iport)
print iport_json
iport_key=iport_json['160'].keys()
print iport_key
iport_jumps=json.dumps(iport_json['160'],ensure_ascii=False)
iport_jumps_160=json.dumps(iport_json['160'],ensure_ascii=False)
#iport_jumps=json.dumps(iport_json['60'],ensure_ascii=False)
print iport_jumps
#print iport_jumps
for ip in iport_json['160']:
	ll=json.dumps(iport_json['160'][ip],ensure_ascii=False)
	aa=iport_json['160'][ip]
	print aa
	print ll
	print ip


#print s
#print s.keys()
#print s["name"]
#print s["type"]["name"]
#print s["type"]["parameter"][1]
