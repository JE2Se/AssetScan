# -*- encoding: utf-8 -*-
'''
@File : importfile.py
@Time : 2019/09/16 10:36:43
@Author : JE2Se 
@Version : 1.0
@Contact : admin@je2se.com
@WebSite : https://www.je2se.com
'''

#import pandas as pd
import xlrd as xl
import csv
from lib.color import Vcolors
import os



def to_xls(path):
    xls_file = xl.open_workbook(path)
    xls_sheet = xls_file.sheets()[0]
    col_value = xls_sheet.col_values(0)
    return col_value

def to_csv(path):
    csv_file = csv.reader(open(path,'r',encoding='utf-8'))
    csvdata = []
    for i in csv_file:
        csvdata.append(i)
    return csvdata

def to_txt(path):
    global ipcontent
    txtdata = open(path,'r')
    data = txtdata.readlines()
    txt_file = []
    for i in data:
        list1 = i.strip()
        txt_file.append(list1)
    return txt_file

def importfile(path):
    if "/" in path:
        houzhui =path.split(".")
        if houzhui[-1] =="txt":
            return to_txt(path)
        elif houzhui[-1] =="xls" or houzhui[-1] =="xlsx":
            return to_xls(path)
        elif houzhui[-1] == "csv":
            return to_csv(path)
        else:
            print(Vcolors.RED+ "本程序目前仅支持导入 xls , xlsx , csv , txt ~~"+ Vcolors.ENDC)
            exit()
    elif "\\" in path:
        houzhui =path.split(".")
        if houzhui[-1] =="txt":
            return to_txt(path)
        elif houzhui[-1] =="xls" or houzhui[-1] =="xlsx":
            return to_xls(path)
        elif houzhui[-1] == "csv":
            return to_csv(path)
        else:
            print(Vcolors.RED+ "本程序目前仅支持导入 xls , xlsx , csv , txt ~~"+ Vcolors.ENDC)
            exit()
    else:
        print(Vcolors.OKGREEN+ "请填写文件的绝对路径~~"+ Vcolors.ENDC)
        exit()