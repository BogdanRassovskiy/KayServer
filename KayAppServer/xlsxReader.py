import os;
import openpyxl;
import sqlite3;
import requests;
import Stats;
import converter;

URL=Stats.URL;

def prodRead(file):
    while True:
        wb = openpyxl.load_workbook(filename = 'workers/'+file)
        sheet = wb['Sheet']
        name = str(sheet['A'+str(i)].value)
        how_many = str(sheet['G'+str(i)].value)
        price = str(sheet['H'+str(i)].value).replace(" ","").replace(".","")
        rev=" ";
        if name=="None":
            print("read done")
            break;
        else:
            list_send=list_send+name+"|"+name+"|"+rev+"|"+rev+"|"+price+"|"+how_many+"|^";
            i+=1;

def nakRead(file):
    while True:
        wb = openpyxl.load_workbook(filename = 'workers/'+file)
        sheet = wb['Sheet']
        name = str(sheet['A'+str(i)].value)
        how_many = str(sheet['G'+str(i)].value)
        price = str(sheet['H'+str(i)].value).replace(" ","").replace(".","")
        rev=" ";
        if name=="None":
            print("read done")
            break;
        else:
            list_send=list_send+name+"|"+name+"|"+rev+"|"+rev+"|"+price+"|"+how_many+"|^";
            i+=1;

def cort_to_list(cort):
    list_ = [];
    for i in range(len(cort)):
        list_.append(cort[i][0]);
    return list_;
