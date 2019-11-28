# -*- encoding: utf-8 -*-
'''
@File : color.py
@Time : 2019/07/05 14:20:03
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''
import platform

if "Darwin" in platform.system():
    class Vcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        RED = '\033[31m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
        YELLOW= '\033[1;33m'
        DARKGRAY= "\033[1;30m"   
        CYAN= "\033[0;36m"   
        PURPLE= "\033[0;35m"  
        BROWN= "\033[0;33m"  
        WHITE= "\033[1;37m" 
elif "Windows" in platform.system():
    class Vcolors:
        HEADER = ''
        OKBLUE = ''
        OKGREEN = ''
        WARNING = ''
        FAIL = ''
        RED = ''
        ENDC = ''
        BOLD = ''
        UNDERLINE = ''
        YELLOW= ''
        DARKGRAY= ""   
        CYAN= ""   
        PURPLE= ""  
        BROWN= ""  
        WHITE= "" 