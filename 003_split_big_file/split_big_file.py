#encoding=utf-8
import time

start_time = time.time()
print "begin"

def read_in_block(file_path,BLOCK_SIZE):
    '''使用生成器分割大文件'''
    #BLOCK_SIZE=10000000
    #BLOCK_SIZE = 1024
    with open(file_path,"r") as f:
        while True:
            block =f.readlines(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

def test_readlines(BLOCK_SIZE):
    i = 0
    start_time = time.time()
    for block in read_in_block('neo.log',BLOCK_SIZE):
        i = i+1
        #output = open('data.txt'+str(i), 'w')
        #for j in block:
        #   output.write(j)
        #output.close()
    print "when BLOCK_SIZE = ",BLOCK_SIZE,"  i = ",i,"  time is",time.time() - start_time , "s"

BLOCK_SIZE = 1000
#test_readlines(BLOCK_SIZE)
BLOCK_SIZE = 100000
#test_readlines(BLOCK_SIZE)
BLOCK_SIZE = 10000000
#test_readlines(BLOCK_SIZE)

def test_readline():
    '''直接迭代'''
    i = 0
    j = 0
    start_time = time.time()
    with open('neo.log') as file:
        for line in file:
            i = i+1
            if i >10000 :
                j = j+1
                i = 0
    print " when readline, time = ", time.time() - start_time , "s ", " i = ",i,"  j = ",j

#test_readline()



f = open('neo.log')
i = 0

def read_last_line(start,size):
    '''从文件尾部开始读取
        start: 开始地址(从文件尾部倒推字节)
        参考值：10w 约等于100kb
               1000w 约等于 10mb
        size : 读取字节
    '''
    global i 
    i = i - start
    j = 0
    while True:
        i = i - 1
        f.seek(i,2)
        if f.read(1) == '\n':
            break
    output = open('data_all.txt', 'w')
    for line in f:
        j = j +len(line)
        if j < size:
            output.write(line)
    output.close()
start = 100000000
size  = 10000000
start_time = time.time()
read_last_line(start,size)
print " when size = ",size/1024/1024,"mb  time = ", time.time() - start_time , "s "


























    
