# -*- encoding: utf-8 -*-
'''
@File : p1521.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p1521(portdic):
    p1521list=[]
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "1521":
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查ORACLE是否存在弱口令~'+Vcolors.ENDC)
            a = ip[0]+":1521:Oracle端口开放，请检查Oracle是否存在弱口令"
            p1521list.append(a)
            pass
            #do_nmap(ip[0])
    return p1521list
    