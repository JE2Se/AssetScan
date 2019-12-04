# -*- encoding: utf-8 -*-
'''
@File : CVE_2018_2894.py
@Time : 2019/09/30 14:02:50
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


from lib import *
import sys
import requests

VUL=['CVE-2018-2894']
headers = {'user-agent': 'ceshi/0.0.1'}

def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/ws_utc/resources/setting/options/general'
    url1='https://' + str(ur)+':'+str(port)+'/ws_utc/resources/setting/options/general'
    try:
        r = requests.get(url, headers=headers,verify=False)
    except:
        r = requests.get(url1, headers=headers,verify=False)
    return r.status_code

def run(url,port,index):
    if islive(url,port)!=404:
        print(Vcolors.RED+str(url) + '\t存在JAVA deserialization漏洞(CVE-2018-2894)\n\t'+Vcolors.ENDC)
        a = url+":"+port+":存在JAVA deserialization漏洞(CVE-2018-2894)"
        return a
    else:
        pass
