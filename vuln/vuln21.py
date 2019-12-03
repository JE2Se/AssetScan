# -*- encoding: utf-8 -*-
'''
@File : p21.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p21(portdic):
    p21list = []
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "21":
            p21list.append(do_nmap0(ip[0]))
            p21list.append(do_nmap(ip[0]))
            p21list.append(do_nmap1(ip[0]))
            p21list.append(do_nmap2(ip[0]))        
    return p21list
def do_nmap0(host_list):
    print(Vcolors.OKGREEN+str(host_list)+'\tFTP开放，请自行检测是否存在弱口令~'+Vcolors.ENDC)
    a = host_list+":21:FTP端口开放，请自行检测是否存在弱口令"
    return a


def do_nmap(host_list):
    nm = nmap.PortScanner()
    b = nm.scan(hosts=host_list, arguments='-p 21  -script ftp-vsftpd-backdoor.nse')
    try:
        a  = str(b)
        if "VULNERABLE" and "vsftpd" in a :
            print(Vcolors.RED+str(host_list)+'\t存在vsftpd后门(CVE-2011-2523)~'+Vcolors.ENDC)
            a = host_list+":21:存在vsftpd后门(CVE-2011-2523)"
            return a
    except:
        pass

def do_nmap1(host_list):
    nm = nmap.PortScanner()
    b = nm.scan(hosts=host_list, arguments='-p 21 -script ftp-anon.nse')
    try:
        a = str(b)
        if "nonymous" and "230" in a :
            print(Vcolors.RED+str(host_list)+'\t存在FTP匿名访问漏洞~'+Vcolors.ENDC)
            a = host_list+":21:存在FTP匿名访问漏洞"
            return a
    except:
        pass

def do_nmap2(host_list):
    nm = nmap.PortScanner()
    nm.scan(hosts=host_list, arguments='-p 21 -script ftp-proftpd-backdoor.nse')
    try:
        a = nm[host_list]["tcp"][21]["script"]['ftp-proftpd-backdoor']
        if "ftp-proftpd-backdoor" and "VULNERABLE" and "CVE-2011-2523" in str(a):
            print(Vcolors.RED+str(host_list)+'\t存在proftpd后门漏洞~'+Vcolors.ENDC)
            a = host_list+":21:存在proftpd后门漏洞"
            return a
    except:
        pass
