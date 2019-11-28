# -*- encoding: utf-8 -*-
'''
@File : p80.py
@Time : 2019/09/29 14:47:15
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import nmap
from lib import *
import requests

def p2601(portdic):
    p2601list = []
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "2601":
            p2601list.append(zebra(ip[0]))
        if ip[-1] == "2604":
            p2601list.append(zebra1(ip[0]))
    return p2601list


def zebra(host_list):
    url = "https://"+host_list+":2601/login"
    a = requests.get(url,timeout=5)
    if a.status_code == 200:
        print(Vcolors.OKGREEN+str(host_list)+'\t识别到Zebra路由，请检测默认口令zebra:zebra~'+Vcolors.ENDC)
        ff = host_list + ":2601:识别到Zebra路由，请检测默认口令zebra:zebra"
        return ff
    else:
        pass


def zebra1(host_list):
    url = "https://"+host_list+":2604/login"
    a = requests.get(url,timeout=5)
    if a.status_code == 200:
        print(Vcolors.OKGREEN+str(host_list)+'\t识别到Zebra路由，请检测默认口令zebra:zebra~'+Vcolors.ENDC)
        ff = host_list + ":2604:Zebra端口开放，识别到Zebra路由，请检测默认口令zebra:zebra"
        return ff
    else:
        pass
