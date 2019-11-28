# -*- encoding: utf-8 -*-
'''
@File : p3389.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p3389(portdic):
    p3389list = []
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "3389":
            p3389list.append(do_nmap(ip[0]))
            print(Vcolors.OKGREEN+str(ip[0])+'\t请确认是否存在CVE-2019-0708漏洞~'+Vcolors.ENDC)
            a = ip[0]+":3389:请确认是否存在CVE-2019-0708漏洞"
            p3389list.append(a)
    return p3389list

def do_nmap(host_list):
    nm = nmap.PortScanner()
    b=nm.scan(hosts=host_list, arguments='-p3389 -script rdp-vuln-ms12-020.nse')
    try:
        #a = nm[host_list]["tcp"][3389]["script"]['rdp-vuln-ms12-020']
        if "rdp-vuln-ms12-020" and "VULNERABLE" in str(b) :
            print(Vcolors.RED+str(host_list)+'\tRDP协议存在MS12-020漏洞~'+Vcolors.ENDC)
            a = host_list+":3389:存在MS12-020漏洞"
            return a
    except:
        pass