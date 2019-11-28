# -*- encoding: utf-8 -*-
'''
@File : portmsscan.py
@Time : 2019/09/26 14:32:39
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import masscan
from lib.color import Vcolors


portdict = []

def masscanresult(ipstr,thread):
    mas = masscan.PortScanner()
    threads = '--max-rate ' + str(thread)
    mas.scan(ipstr, ports="21,22,23,80,161,389,443,445,512,513,514,873,1025,111,1433,1521,5560,7778,2601,2604,3128,3306,3312,3311,3389,4440,5432,5900,5984,6082,6379,7001,7002,7778,8000,8001,8080,8089,8090,9090,8083,8649,8888,9200,9300,10000,11211,27017,27018,28017,50000,50070,50030", arguments=threads)
    for result in mas.scan_result['scan']: 
        yuanzu =list(mas.scan_result['scan'].values())
        port = list(yuanzu[0]["tcp"].keys())
        for i in port:
            ipdata =result+":"+ str(i)
            print(Vcolors.RED+ "发现端口开放~\tip地址为:"+result+"\t端口为:"+str(i)+ Vcolors.ENDC)
            portdict.append(ipdata)
        # for  port in mas.scan_result['scan'].values()["tcp"].keys():
        #     masscanport = result + ":" + port
        #     print(masscanport)

def portscanalll(thread):
    ipdata = open("./file/alive.txt","r")
    ipstr = ipdata.read().replace("\n",",")
    masscanresult(ipstr,thread)
    ipdata.close()

    #print(Vcolors.OKGREEN+ "发现端口未开放~\tip地址为:"+host+"\t端口为:"+str(port)+ Vcolors.ENDC)
def portmasscan_vul(thread):
    print(Vcolors.OKGREEN+ "正在目标全部端口进行Masscan探测扫描~~")
    portalive=open("./file/port.txt",'a+')
    portscanalll(thread)
    for port in portdict:   
        portalive.write(port)
        portalive.write("\n")
    portalive.close()
    return portdict 