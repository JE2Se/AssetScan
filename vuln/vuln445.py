# -*- encoding: utf-8 -*-
'''
@File : 1.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p445(portdic):
    p445list =[]
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "445":
            p445list.append(do_nmap(ip[0]))
    return p445list

def do_nmap(host_list):
    nm = nmap.PortScanner()
    a = nm.scan(hosts=host_list, arguments='-Pn -sC -p 445 -max-hostgroup 3 -open -script smb-vuln-ms17-010.nse,smb-vuln-ms08-067.nse')
    #a = nm["scan"][host_list]["hostscript"][0]["output"]
    try:
        if "ms17-010" and "VULNERABLE" in str(a) :
            print(Vcolors.RED+str(host_list)+'\t存在永恒之蓝漏洞(MS17-010)~'+Vcolors.ENDC)
            a = host_list+":445:存在永恒之蓝漏洞(MS17-010)"
            return a
        elif "ms08-067" and "VULNERABLE" in a:
            print(Vcolors.RED+str(host_list)+'\t存在MS08-067漏洞~'+Vcolors.ENDC)
            a = host_list+":445:存在MS08-067漏洞"
            return a
        else:
            pass
    except:
        pass