# -*- encoding: utf-8 -*-
'''
@File : p110.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p110(portdic):
    p110list = []
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "110":
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查是否存在POP存在弱口令~'+Vcolors.ENDC)
            a = ip[0]+":110:110端口开放，请检测是否存在POP存在弱口令"
            p110list.append(a)
            pass
        if ip[-1] == "995":
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查是否存在POP存在弱口令~'+Vcolors.ENDC)
            b = ip[0]+":995:995端口开放，请检测是否存在POP存在弱口令"
            p110list.append(b)
            pass
            #do_nmap(ip[0])
    return  p110list

def do_nmap(host_list):
    nm = nmap.PortScanner()
    nm.scan(hosts=host_list, arguments='-Pn -sC -p 110 -max-hostgroup 3 -open -script pop3-brute.nse -v')
    for host in nm.all_hosts():
        print(Vcolors.RED+str(host)+'\tpop简单弱口令爆破，存在弱口令~'+Vcolors.ENDC)