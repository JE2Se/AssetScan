# -*- encoding: utf-8 -*-
'''
@File : p5432.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *

def p5432(portdic):
    p5432list=[]
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "5432":
            print(Vcolors.OKGREEN+str(ip[0])+'\t请检查PostgreSQL是否存在弱口令~'+Vcolors.ENDC)
            a = ip[0]+":5432:PostgreSQL端口开放，请检查PostgreSQL是否存在弱口令"
            p5432list.append(a)
            pass
            #do_nmap(ip[0])
    return p5432list
    