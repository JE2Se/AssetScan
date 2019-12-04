# -*- encoding: utf-8 -*-
'''
@File : WeblogicScanLot.py
@Time : 2019/09/30 13:00:09
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''


import re
from multiprocessing import Pool, Manager
import vuln.Console
import vuln.CVE_2014_4210
import vuln.CVE_2016_0638
import vuln.CVE_2016_3510
import vuln.CVE_2017_3248
import vuln.CVE_2017_3506
import vuln.CVE_2017_10271
import vuln.CVE_2018_2628
import vuln.CVE_2018_2893
import vuln.CVE_2018_2894
import vuln.CVE_2019_2725
import vuln.CVE_2019_2729

p7001dict=[]

def poolmana(portdic):
    p = Pool(10)
    q = Manager().Queue()
    for ip in portdic:
        ip = ip.split(":")
        if ip[-1] == "7001":
            rip = ip[0]
            rport = ip[-1]
            p7001dict.extend(p.apply_async(work,args=(rip,rport,q,)).get())
        else:
            pass
    p.close()
    p.join()
    return p7001dict

def work(rip,rport,q):
    p7001list=[]
    try:
        p7001list.append(vuln.Console.run(rip, rport))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2014_4210.run(rip,rport))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2016_0638.run(rip,rport,0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2016_3510.run(rip, rport, 0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2017_3248.run(rip, rport, 0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2017_3506.run(rip, rport, 0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2017_10271.run(rip, rport, 0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2018_2628.run(rip, rport, 0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2018_2893.run(rip, rport, 0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2018_2894.run(rip, rport, 0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2019_2725.run(rip, rport, 0))
    except:
        pass

    try:
        p7001list.append(vuln.CVE_2019_2729.run(rip, rport, 0))
    except:
        pass
    q.put(rip)
    return p7001dict.extend(p7001list)

