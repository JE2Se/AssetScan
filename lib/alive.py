# -*- encoding: utf-8 -*-
'''
@File : ping.py
@Time : 2019/09/25 21:05:43
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''



import subprocess
import os
import sys
import re
from lib.color import Vcolors

def unixping(ip):
    p = subprocess.Popen(["ping -c 1 -i 0.2 -W 3 " +ip],stdin = subprocess.PIPE,stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell = True)
    out = p.stdout.read()
    ipalive=open("./file/alive.txt",'a+')
    if "ttl" in str(out):
        print(Vcolors.RED + "测试范围中:\t"+ip+"\t存活~~" + Vcolors.ENDC)
        ipalive.write(ip)
        ipalive.write("\n")
    else:
        pass
    ipalive.close()

def winping(ip):
    p = subprocess.Popen(['ping','-n','1','-w','3 ',ip],
                stdout=subprocess.PIPE,
                stdin = subprocess.PIPE,
                stderr = subprocess.PIPE,
                shell = True)
    output = p.stdout.read().decode("gbk").upper()
    ipalive=open("./file/alive.txt",'a+')
    if "TTL" in output:
        print(Vcolors.RED + "测试范围中:\t"+ip+"\t存活~~" + Vcolors.ENDC)
        ipalive.write(ip)
        ipalive.write("\n")
    else:
        pass
    ipalive.close()
    
    
if __name__ == "__main__":
    ip = sys.argv[1]
    if os.name =="nt":
        winping(ip)
    else:
        unixping(ip)