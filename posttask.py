#!/usr/bin/python  
#coding=utf-8  
  
import urllib  
import urllib2  
import simplejson
import json

def get(url):
    return urllib2.urlopen(url).read()
  
def post(url, data):  
    req = urllib2.Request(url)  
    data = urllib.urlencode(data)  
    #enable cookie  
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor())  
    response = opener.open(req, data)  
    return response.read()  

def postJsonData(url, data):
    # datas = input("Please enter your date:") 
    data_json = json.dumps(data) 
    print type(data_json)
    req = urllib2.Request(url,data_json) 
    response_stream = urllib2.urlopen(req) 
    res = response_stream.read() 
    return res

def postAgain(url, data):
    # print json.dumps(data, ensure_ascii=True, encoding='gbk')
    print json.dumps(data)
    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')
    req.add_header('charset', 'GBK')

    response = urllib2.urlopen(req, json.dumps(data))
    res = response.read()
    return res

def xiaoxiong():
    params = urllib.urlencode(
      {'queryStudentId': cardnum, 
      'queryAcademicYear':'13-14-2'
      }) 
    ufile = urllib.urlopen("http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action", params)
    text = ufile.read().decode('utf-8')
  
def main():  
    # posturl = "http://127.0.0.1:8000/depot/postJson"
    # posturl = "http://www.xiami.com/member/login"
    # posturl = "httdata = {"access_token":"ACCESS_TOKEN", "expires_in":7200}ps://api.weixin.qq.com/cgi-bin/menu/create?access_token=ACCESS_TOKEN"  
    # data = {'email':'myemail', 'password':'mypass', 'autologin':'1', 'submit':'登 录', 'type':''} 
    # posturl = "http://xk.urp.seu.edu.cn/jw_service/service/lookCurriculum.action"
    posturl = "http://xk.urp.seu.edu.cn/jw_service/service/stuCurriculum.action"
    #data = {"access_token":"ACCESS_TOKEN", "expires_in":7200}
    data = {"queryStudentId":213101579, "queryAcademicYear":"13-14-2"}
    postdata = simplejson.dumps(data)
    '''data = {
     "button":[
     {  
          "type":"click",
          "name":"今日歌曲",
          "key":"V1001_TODAY_MUSIC"
      },
      {
           "type":"view",
           "name":"歌手简介",
           "url":"http://www.qq.com/"
      },
      {
           "name":"菜单",
           "sub_button":[
            {
               "type":"click",
               "name":"hello word",
               "key":"V1001_HELLO_WORLD"
            },
            {
               "type":"click",
               "name":"赞一下我们",
               "key":"V1001_GOOD"
            }]
       }]
 }'''
    print post(posturl, data) 
    # print postAgain(posturl, postdata)
    # print postJsonData(posturl, postdata)  
    # print get(posturl)

def jsongbk():
    import json
    # js = json.loads('{"haha": "哈哈"}')
    js = {"haha": "哈哈"}
    a = {'key':'中文'}
    print js
    print json.dumps(js)
    print json.dumps(js, ensure_ascii=False)  
    print json.dumps(js, ensure_ascii=True, encoding='gbk')   
    print json.dumps(a, ensure_ascii=True, encoding='gbk')





  
if __name__ == '__main__':  
    main()
    # get()  
    # jsongbk()
#该代码片段来自于: http://www.sharejs.com/codes/python/5756
