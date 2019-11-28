# -*- encoding: utf-8 -*-
'''
@File : Console.py
@Time : 2019/09/30 14:02:03
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import sys
import requests
from lib import *


headers = {'user-agent': 'ceshi/0.0.1'}

def islive(ur,port):
    url='http://' + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
    url1='https://' + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
    try:
        r = requests.get(url, headers=headers)
    except:
        r = requests.get(url1, headers=headers)
    return r.status_code

def run(url,port):
    if islive(url,port)==200:
        u='http(s)://' + str(url)+':'+str(port)+'/console/login/LoginForm.jsp'
        print(Vcolors.RED+str(url) + ':'+str(port)+'\t检测weblogic是否存在弱密码'+"\n\t地址为:"+u+Vcolors.ENDC)
        a = url +":"+port+":检测weblogic是否存在弱密码:\n\t地址为->"+u
        return a
    else:
        pass

