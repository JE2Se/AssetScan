# -*- encoding: utf-8 -*-
'''
@File : p143.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p143(portdic):
    p143list=[]
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "143":
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查是否存在IMAP存在弱口令~'+Vcolors.ENDC)
            a = ip[0]+":143:143端口开放，请检测是否存在IMAP存在弱口令"
            p143list.append(a)
            pass
            #do_nmap(ip[0])
        elif ip[-1] == "995":
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查是否存在IMAP存在弱口令~'+Vcolors.ENDC)
            a = ip[0]+":995:995端口开放，请检测是否存在IMAP存在弱口令"
            p143list.append(a)
            pass
            #do_nmap1(ip[0])
    return p143list

def do_nmap(host_list):
    nm = nmap.PortScanner()
    nm.scan(hosts=host_list, arguments='-Pn -sC -p 143 -max-hostgroup 3 -open -script imap-brute.nse -v')
    for host in nm.all_hosts():
        print(Vcolors.RED+str(host)+'\t存在imap简单弱口令爆破，存在弱口令~'+Vcolors.ENDC)

def do_nmap1(host_list):
    nm = nmap.PortScanner()
    nm.scan(hosts=host_list, arguments='-Pn -sC -p 995 -max-hostgroup 3 -open -script imap-brute.nse -v')
    for host in nm.all_hosts():
        print(Vcolors.RED+str(host)+'\timap简单弱口令爆破，存在弱口令~'+Vcolors.ENDC)

