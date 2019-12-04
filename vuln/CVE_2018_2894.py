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
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:49.0) Gecko/20100101 Firefox/49.0"}

def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/ws_utc/resources/setting/options/general'
    url1='https://' + str(ur)+':'+str(port)+'/ws_utc/resources/setting/options/general'
    error=['404','Not Found','找不到','安全狗','无权访问','403']
    try:
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url, headers=headers,verify=False)     
        for e in error:
            if r.status_code==200 and e not in r.text:
                print(Vcolors.RED+str(ur) + '\t存在JAVA deserialization漏洞(CVE-2018-2894)'+Vcolors.ENDC)
                a = ur+":7001:存在JAVA deserialization漏洞(CVE-2018-2894)"
                return a
        else:
            pass
    except:
        requests.packages.urllib3.disable_warnings()
        r = requests.get(url1, headers=headers,verify=False)     
        for e in error:
            if r.status_code==200 and e not in r.text:
                print(Vcolors.RED+str(ur) + '\t存在JAVA deserialization漏洞(CVE-2018-2894)'+Vcolors.ENDC)
                a = ur+":7001:存在JAVA deserialization漏洞(CVE-2018-2894)"
                return a

def run(url,port,index):
    try:
        return islive(url,port)
    except:
        pass