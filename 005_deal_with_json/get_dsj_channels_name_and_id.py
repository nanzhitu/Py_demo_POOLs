# -*- coding: utf-8 -*-   
  
#import sys   
#reload(sys) # Python2.5 初始化后会删除 sys.setdefaultencoding 这个方法，我们需要重新载入   
#sys.setdefaultencoding('utf-8')
import urllib2 
import json

 


url = "http://cdn.idianshijia.com/tvlive/apk/json/3rd.json"
req = urllib2.Request(url)
result = urllib2.urlopen(req)

data = result.read()  
data = data.decode('UTF-8')  
#print(data)  

s = json.loads(data)
output = open('data_all.txt', 'w')
for i in s:
    ss = i['channels']
    for j in ss:
        name = j['name']
        idd = j['id']
        lalala = name +" "+idd+"\n"
        print lalala
        output.write(lalala.encode('gbk'))

output.close()
