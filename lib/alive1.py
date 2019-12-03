# -*- encoding: utf-8 -*-
'''
@File : alive1.py
@Time : 2019/09/25 21:05:43
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

from scapy.all import *
from lib.color import Vcolors

def arp_scan(ip):
    arpPkt = Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=ip, hwdst="ff:ff:ff:ff:ff:ff")
    res = srp1(arpPkt, timeout=1, verbose=0)
    ipalive=open("./file/alive.txt",'a+')
    if res:
        ip = res.psrc
        print(Vcolors.RED + "测试范围中:\t"+ip+"\t存活~~" + Vcolors.ENDC)
        ipalive.write(ip)
        ipalive.write("\n")
    else:
        pass
    ipalive.close()

