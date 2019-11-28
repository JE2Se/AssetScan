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
    mas.scan(ipstr, ports='1-65535', arguments=threads)
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
def portmasscan_all(thread):
    print(Vcolors.OKGREEN+ "正在目标全部端口进行Masscan探测扫描~~")
    portalive=open("./file/port.txt",'a+')
    portscanalll(thread)
    for port in portdict:   
        portalive.write(port)
        portalive.write("\n")
    portalive.close()
    return portdict 