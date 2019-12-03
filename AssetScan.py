# -*- encoding: utf-8 -*-
'''
@File : AssetScan.py
@Time : 2019/08/27 21:50:46
@Author : JE2Se 
@Version : 1.1
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

import sys
from lib import *
import threading
import os
import time
#---------------------分割线--------------------------------------------------
#线程类
class Request(threading.Thread):
    def __init__(self, alive_queue, livecase, *args, **kwargs):
        super(Request, self).__init__(*args, **kwargs)
        self.alive_queue = alive_queue
        self.livecase = livecase

    def run(self):
        while True:
            if self.alive_queue.empty():
                break
            ip = self.alive_queue.get()
            self.alive(ip)
    def alive(self,ip):
        if self.livecase =="1":
            try:
                if os.name == "nt":
                    winping(ip)
                else:
                    unixping(ip)
            except:
                pass
        elif self.livecase =="2":
            arp_scan(ip)
        else:
            print(Vcolors.OKGREEN+"程序退出~")
            exit()
            
#---------------------分割线--------------------------------------------------
#通用处理
def father(iplist):
    print(Vcolors.OKGREEN+ "正在对目标地址进行存活检测~~"+ Vcolors.ENDC)
    ascii_banner = pyfiglet.figlet_format("AssetScan")
    print(Vcolors.PURPLE + ascii_banner+Vcolors.ENDC)
    print(Vcolors.OKGREEN+"请选择存活探测的方式~")
    print(Vcolors.OKBLUE+'''(1)Ping探测~(适用于内网内没有禁用Ping)\n(2)ARP探测~（适用于内网内禁用Pin探测)\n\n    任意键退出程序~'''+Vcolors.ENDC)
    print("\n")
    livecase = input(Vcolors.YELLOW+u"请选择探测存活方式->"+Vcolors.ENDC)
    
    alive_queue = Queue(len(iplist))
    for ip in iplist:
        alive_queue.put(ip)
    thread_list = []
    for u in range(500):
        t = Request(alive_queue,livecase)
        t.start()
        thread_list.append(t)
    for i in thread_list:
        i.join()
    print(Vcolors.OKGREEN + "存活地址已成功写入alive.txt中" + Vcolors.ENDC)
    print("\n")
    vullist = []
    portdic = []
    alivelist = []
    ipdata = open("./file/alive.txt","r")
    alivedata = ipdata.readlines()
    for i in alivedata:
        alivelist.append(i.strip("\n"))
    ipdata.close()
    ascii_banner = pyfiglet.figlet_format("AssetScan")
    print(Vcolors.PURPLE + ascii_banner+Vcolors.ENDC)
    print(Vcolors.OKGREEN+"请选择端口扫描的方式~")
    print(Vcolors.OKBLUE+'''(1)风险端口探测 (Socket方式,适用于少IP)\n(2)风险端口探测 (Masscan方式,适用于多IP)\n(3)常规端口探测 (Nmap方式,Nmap的top1000端口)\n(4)全端口探测   (Socket方式,适用于少IP，准确率高)\n(5)全端口探测   (Masscan方式,适用于多IP,存在误报率)\n\n    任意键退出程序,并生成当前进度报告~'''+Vcolors.ENDC)
    print("\n")
    scancase = input(Vcolors.YELLOW+u"请填写扫描方式->"+Vcolors.ENDC)
    if scancase == "1":
        portdic = portscan()
    elif scancase == "2":
        threadd = input(Vcolors.PURPLE+u"请填写进程配置(默认2000)->"+Vcolors.ENDC)
        if threadd == "":
            threadd ="2000"
        portdic = portmasscan_vul(threadd)
    elif scancase == "3":
        portdic = nmapscan()
    elif scancase == "4":
        portdic = portscanalll()
    elif scancase == "5":
        threadd = input(Vcolors.PURPLE+u"请填写进程配置(默认2000)->"+Vcolors.ENDC)
        if threadd == "":
            threadd ="2000"
        portdic = portmasscan_all(threadd)
    else:
        resultreport(iplist,alivelist,portdic,vullist)
        exit()
    print("\n")
    ascii_banner = pyfiglet.figlet_format("AssetScan")
    print(Vcolors.PURPLE + ascii_banner+Vcolors.ENDC)
    print(Vcolors.OKGREEN+"是否进行风险端口漏洞探测~")
    print(Vcolors.OKBLUE+'''(1)探测风险端口\n\n    任意键退出程序，并生成当前进度报告~'''+Vcolors.ENDC)
    print("\n")
    scancase = input(Vcolors.YELLOW+u"请选择是否进行漏洞探测->"+Vcolors.ENDC)
    if scancase == "1":
        #vullist是存在漏洞的ip地址以及漏洞信息
        vullist = p21(portdic)+p23(portdic)+p22(portdic)+p80(portdic)+p110(portdic)+p143(portdic)+p443(portdic)+p445(portdic)+p873(portdic)+p1433(portdic)+p3306(portdic)+p6379(portdic)+p8080(portdic)+p9200(portdic)+p11211(portdic)+p27017(portdic)+poolmana(portdic)+p1521(portdic)+p2601(portdic)+vulnall(portdic)+p4848(portdic)+p2181(portdic)+p389(portdic)+p5432(portdic)+p3389(portdic)
        resultreport(iplist,alivelist,portdic,vullist)
    elif scancase == "2":
        resultreport(iplist,alivelist,portdic,vullist)
    else:
        resultreport(iplist,alivelist,portdic,vullist)
        exit()
#---------------------分割线---------------存活数据-----------------------------------
    #alivelist = []
#---------------------分割线---------------端口数据-----------------------------------
    #portdic
#---------------------分割线---------------漏洞数据----------------------------------- 
    #vullist   
#---------------------分割线---------------报告模块----------------------------------- 

def resultreport(iplist,alivelist,portdic,vullist):
    vullist = list(filter(None, vullist))
    path = reportfile(iplist,alivelist,portdic,vullist) 
    print(Vcolors.OKGREEN+'正在生成报告~'+Vcolors.ENDC)
    print(Vcolors.OKBLUE+'生成报告成功~'+Vcolors.ENDC)
    print(Vcolors.OKGREEN+'报告地址:'+Vcolors.ENDC + Vcolors.RED+ path +Vcolors.ENDC)
    print(Vcolors.YELLOW+'扫描结束~'+Vcolors.ENDC)
    if os.path.exists("./file/alive.txt"):
        os.remove("./file/alive.txt")
    if os.path.exists("./file/port.txt"):
        os.remove("./file/port.txt")

#---------------------分割线--------------------------------------------------

#主程序
if __name__ == "__main__":
    if sys.version_info.major < 3:
        sys.stdout.write(Vcolors.PURPLE + "AssetScan 仅支持Python 3.x版本~\n" + Vcolors.ENDC)
    else:
        import argparse
        import pyfiglet
        from IPy import IP
        import telnetlib
        from script import *
        from  queue  import Queue
        from vuln import *
        import platform

        #重置部分
        if os.path.exists("./file/alive.txt"):
            os.remove("./file/alive.txt")
        if os.path.exists("./file/port.txt"):
            os.remove("./file/port.txt")

        #头部信息部分
        ascii_banner = pyfiglet.figlet_format("AssetScan")
        print(Vcolors.OKGREEN + ascii_banner+Vcolors.ENDC)
        print(Vcolors.OKBLUE + "\t\t\t\tPower by JE2Se" +"   "+ Vcolors.RED + "V1.1" +"\n" +Vcolors.ENDC)
        parser = argparse.ArgumentParser()
        #脚本执行帮助部分
        print(Vcolors.PURPLE + "\t~请输入 -h 获取命令帮助~" + "\n" + Vcolors.ENDC + Vcolors.OKGREEN)
        parser.add_argument("-i", "--ip", help = ' -i 参数，指定的IP范围  ~~') 
        parser.add_argument("-f", "--file", help = ' -f 参数，导入IP地址文件  ~~')
        args = parser.parse_args()
        params = vars(args)
        #导入文件处理簇
        if args.file:
            iplist = importfile(args.file)
            father(iplist)
        #直接输入范围处理簇
        if args.ip:
            ip =str(args.ip)
            iplist = IPinfo(ip)
            father(iplist)


