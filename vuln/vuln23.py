# -*- encoding: utf-8 -*-
'''
@File : p23.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p23(portdic):
    p23list = []
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "23":
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查是否存在telnet存在弱口令~'+Vcolors.ENDC)
            a = ip[0]+":23:Telnet端口开放，请自行检测是否存在telnet弱口令"
            p23list.append(a)
            #do_nmap(ip[0])
    return p23list

def do_nmap(host_list):
    nm = nmap.PortScanner()
    nm.scan(hosts=host_list, arguments='-Pn -sC -p 23 -max-hostgroup 3 -open -script telnet-brute.nse -v')
    for host in nm.all_hosts():
        print(Vcolors.RED+str(host)+'\t简单爆破telnet，存在弱口令~'+Vcolors.ENDC)
