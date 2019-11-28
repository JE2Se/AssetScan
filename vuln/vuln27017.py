# -*- encoding: utf-8 -*-
'''
@File : p27017.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p27017(portdic):
    p27017list=[]
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "27017":
            p27017list.append(do_nmap(ip[0]))
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查是否存在Mongodb存在弱口令~'+Vcolors.ENDC)
            a = ip[0]+":27017:Mongodb端口开放，请检查是否存在Mongodb存在弱口令"
            p27017list.append(a)
    return p27017list

def do_nmap(host_list):
    nm = nmap.PortScanner()
    a = nm.scan(hosts=host_list, arguments=' -p 27017 -script mongodb-info.nse')
    try:
        #a = nm[host_list]["tcp"][27017]["script"]['mongodb-info']
        if  "mongodb-info" and "gitVersion" and "sysInfo" in str(a) :
            print(Vcolors.RED+str(host_list)+'\t存在Mongodb未授权访问漏洞~'+Vcolors.ENDC)
            a =host_list+":27017:存在Mongodb未授权访问漏洞"
            return a
    except:
        pass

def do_nmap1(host_list):
    nm = nmap.PortScanner()
    nm.scan(hosts=host_list, arguments='-Pn -sC -p 27017 -max-hostgroup 3 -open -script mongodb-brute.nse')
    for host in nm.all_hosts():
        print(Vcolors.RED+str(host)+'\t存在Mongodb爆破，存在弱口令~'+Vcolors.ENDC)

