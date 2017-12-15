# -*- coding: utf-8 -*-   
import json

data = open('data_all.txt', 'r')#原始电视家数据

live = open('lex-live.txt', 'r')#原始格式表

output = open('useLiveMatchData.txt', 'w')#以live匹配data输出档

output_temp = open('useDataMatchLive_temp.txt', 'w')#以data匹配live的输出档

data_temp = open('data_no_match.txt', 'w') #记录未匹配到的数据

def dealdata(name,line):
    data = open('data_all.txt', 'r')
    for l in data:
        z = 0
        l_id = l.split(' ')[1]#按空格切割取第二个数据
        l_name = l.split(' ')[0].decode('gb2312')#由gb2312转unicode
 
        if name == l_name:
            #print name
            z = 1 # 匹配成功
        elif name[-2:] == '频道'.decode('utf-8'):#最后两个字符
            if(name[:(len(name)-2)] == l_name):#切掉最后两个字符
               z = 1 # 匹配成功
        elif name[-1:] == '台'.decode('utf-8'):
            if(name[:(len(name)-1)] == l_name):
                z = 1 # 匹配成功
            elif name[-3:] == '综合台'.decode('utf-8'):
                if(name[:(len(name)-3)] == l_name):
                    z = 1 # 匹配成功
        if z == 1:
            line = line.strip() +','+l_id
            output.write(line)
            z = 0
            break;
            
    data.close()

def matchlive():
    
    for line in live:
        if line[0]!= '#':
            name = line.split(',')[1].decode('utf-8').strip()#按逗号切割取第二个并从utf-8解码为unicode再去掉尾部空格（默认为空格）
            dealdata(name,line)
        

#----------------------------------以下func为了获取为匹配的data------#
def deallive(l_name,l_id,l):
    q = 0 
    live = open('lex-live.txt', 'r')
    for line in live:
        z = 0
        if line[0]!= '#':
            name = line.split(',')[1].decode('utf-8').strip()
            if l_name == name:
                #print name
                z = 1 # 匹配成功
                q = 1 #用于记录是否所有live都没有匹配，为0则可以列入未匹配表
            elif name[-2:] == '频道'.decode('utf-8'):
                if(name[:(len(name)-2)] == l_name):
                    z = 1
                    q = 1
            elif name[-1:] == '台'.decode('utf-8'):
                if(name[:(len(name)-1)] == l_name):
                    z = 1
                    q = 1
                elif name[-3:] == '综合台'.decode('utf-8'):
                    if(name[:(len(name)-3)] == l_name):
                        z = 1
                        q = 1
        if z == 1:
            line = line.strip() +','+l_id
            output_temp.write(line)
            z = 0
            break;
            
    live.close()
    if q == 0:
        data_temp.write(l)
    

def matchdata():
    
    for line in data:
        l_id = line.split(' ')[1]
        l_name = line.split(' ')[0].decode('gb2312')
        deallive(l_name,l_id,line)
#--------------------------------------------------------------------#

   
matchlive()
matchdata()


output.close()
output_temp.close()
live.close()
data.close()
data_temp.close()
