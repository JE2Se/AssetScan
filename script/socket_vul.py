# -*- encoding: utf-8 -*-
'''
@File : portscan.py
@Time : 2019/09/05 23:14:43
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
from socket import *
import threading
from lib.color import Vcolors

threads = []
portdict = []

def portcheck():
    ipdata = open("./file/alive.txt","r")
    a = ipdata.readlines()
    for ip in a:
        ip = ip.strip("\n")
        portll(ip)
    ipdata.close()
    
def portll(ip):
    setdefaulttimeout(1)
    portList = ["21","22","23","80","161","389","443","445","512","513","514","873","1025","111","1433","1521","5560","7778","2601","2604","3128","3306","3312","3311","3389","4440","5432","5900","5984","6082","6379","7001","7002","7778","8000","8001","8080","8089","8090","9090","8083","8649","8888","9200","9300","10000","11211","27017","27018","28017","50000","50070","50030"]
    for p in portList:
        #p= int(p)
        t = threading.Thread(target=portScanner,args=(ip,p))
        threads.append(t)
        t.start()     
 
    for t in threads:
        t.join()

def portScanner(host,port):
    try:
        port = int(port)
        s = socket(AF_INET,SOCK_STREAM)
        s.settimeout(1)
        result = s.connect((host,port))
        if result:
            print("ok")
        else:
            #print("发现端口开放~\tip地址为:"+host+"\t端口为:"+str(port))
            print(Vcolors.RED+ "发现端口开放~\tip地址为:"+host+"\t端口为:"+str(port)+ Vcolors.ENDC)
            portname = host +":"+str(port)
            portdict.append(portname)
        s.close()
    except Exception as e:
        pass
        #print(e)
def portscan():
    #print( "正在目标风险端口进行探测扫描~~")
    print(Vcolors.OKGREEN+ "正在目标风险端口进行探测扫描~~"+ Vcolors.ENDC)
    portalive=open("./file/port.txt",'a+')
    portcheck()
    for port in portdict:   
        portalive.write(port)
        portalive.write("\n")
    portalive.close()
    return portdict