# -*- encoding: utf-8 -*-
'''
@File : portscan1000.py
@Time : 2019/09/26 00:20:59
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import nmap
import os
from lib.color import Vcolors

portdict = []

def porttop():
    ipdata = open("./file/alive.txt","r")
    a = ipdata.readlines()
    for ip in a:
        ip = ip.strip("\n")
        nmaptop(ip)
    ipdata.close()

def nmaptop(network_prefix):
    global portdict
    try:
        nm = nmap.PortScanner() 
        ping_scan_raw = nm.scan(hosts = network_prefix,arguments='-sT')
        #print(ping_scan_raw['scan'])        
        for result in ping_scan_raw['scan'].values():  
            po = list(result["tcp"].keys())
            for port in po:
                top = str(list(result["addresses"].values())[0]) +':'+str(port) 
                print(Vcolors.RED+ "发现端口开放~\tip地址为:"+str(list(result["addresses"].values())[0])+"\t端口为:"+str(port)+ Vcolors.ENDC)      
                portdict.append(top)       
    except:
        pass

def nmapscan():
    print(Vcolors.OKGREEN+ "正在目标常用端口进行探测扫描~~"+ Vcolors.ENDC)
    portalive=open("./file/port.txt",'a+')
    porttop()
    for port in portdict:   
        portalive.write(port)
        portalive.write("\n")
    portalive.close()
    return portdict