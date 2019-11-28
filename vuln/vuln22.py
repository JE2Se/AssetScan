# -*- encoding: utf-8 -*-
'''
@File : p22.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p22(portdic):
    p22list = []
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "22":
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查是否存在SSH存在弱口令~'+Vcolors.ENDC) 
            a = ip[0]+":22:SSH端口开放，请检测是否存在SSH弱口令"
            p22list.append(a)
            #do_nmap(ip[0])
    return p22list

def do_nmap(host_list):
    nm = nmap.PortScanner()
    nm.scan(hosts=host_list, arguments='-Pn -sC -p 22 -max-hostgroup 3 -open -script ssh-brute -v')
    for host in nm.all_hosts():
        print(Vcolors.RED+str(host)+'\t正在进行SSH爆破~'+Vcolors.ENDC)
