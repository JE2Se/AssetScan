# -*- encoding: utf-8 -*-
'''
@File : CVE_2014_4210.py
@Time : 2019/09/30 14:02:07
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

from lib import *
import sys
import requests


headers = {'user-agent': 'ceshi/0.0.1'}

def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/uddiexplorer/'
    url1='http://' + str(ur)+':'+str(port)+'/uddiexplorer/'
    try:
        r = requests.get(url, headers=headers)
    except:
        r = requests.get(url1, headers=headers)
    return r.status_code

def run(url,port):
    if islive(url,port)==200:
        u='http://' + str(url)+':'+str(port)+'/uddiexplorer/'
        print(Vcolors.RED+str(url) + ':'+str(port)+'\tweblogic存在SSRF漏洞(CVE-2014-4210)'+"\n\t地址为:"+u+Vcolors.ENDC)
        a = url +":"+port+":weblogic存在SSRF漏洞(CVE-2014-4210):\n\t地址为->"+u
        return a
    else:
        pass

