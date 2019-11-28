# -*- encoding: utf-8 -*-
'''
@File : p11211.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p11211(portdic):
    p11211list=[]
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "11211":
            p11211list.append(do_nmap(ip[0]))
    return p11211list

def do_nmap(host_list):
    nm = nmap.PortScanner()
    b = nm.scan(hosts=host_list, arguments='-p 11211  -script memcached-info.nse')
    try:
        #a = nm[host_list]["tcp"][11211]["script"]['memcached-info']
        if  "memcached-info" and "Architecture" and "CPU" in str(b) :
            print(Vcolors.RED+str(host_list)+'\t存在Memcached未授权访问漏洞~'+Vcolors.ENDC)
            a = host_list+":11211:存在Memcached未授权访问漏洞"
            return a
    except:
        pass