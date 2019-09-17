import xml.etree.ElementTree as ET
import sys
import os
import re
import csv
import json 

def exportCSV(inf):
    func_rows = {}
    row = 1
    for flag, dic in inf.items():
        for func_name, _ in dic.items():
            if func_name not in func_rows :
                func_rows[func_name] = row
                row += 1
    funcs = ['']
    for _ in range(row):
        funcs.append(0)

    for name, r in func_rows.items():
        funcs[r] = name

    with open('fread.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(funcs)

    for flag, dic in inf.items():
        exec_t = []
        exec_t.append(flag)
        for _ in range( len(funcs) ):
            exec_t.append(0.0)
        for name, extra in dic.items():
            index = func_rows[name]
            try:
                exec_t[index] = extra[0]
            except IndexError:
                print("index : ", index, len(exec_t), name)
        with open('fread.csv', mode='a') as data_file:
            data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            data_writer.writerow(exec_t)

def isLeaf(func_name):
    if func_name[-1] == ';':
        return True
    else:
        return False

def parser():
    path = "./data/"
    dir_list = os.listdir(path)
    ret = {}
    for d in dir_list:
        dir_count = len(os.listdir(path+str(d)))
        inf = {}
        for i in range (0,1):
            f = open(path+str(d)+"/test_"+str(i)+".dat", "r")
            data = []
            stack = []
            for line in f:
                data.append(line)

            c = 0
            print("dir : ", d)
            while True:
                exec_time = re.findall(r'\d+\.{1}\d+', data[c])
                func_name = re.findall(r'_{0,2}?\w+[\w.\w*]* ?\[?\w+?\]?\(\);?', data[c])
                func_end = re.findall(r'}', data[0])
                ret_func_name = re.findall(r'(}) \/\* (_{0,2}?\w+[\w.\w*]* ?\[?\w+?\]?) \*\/', data[c])
                if len(func_name) > 0:
                    break
                c+=1
            if len(func_name) > 0 and isLeaf(func_name[0]) == False:
                func_name[0] = func_name[0].replace("()", "")
                root = {}
                root["name"] = func_name[0]
                root["value"] = 0
                root["children"] =[]
                dfs(c+1, data, root, func_name[0])

        with open("./anychart_jsons/"+str(d)+"_"+str(i)+".json", "w") as write_file:
            json.dump(root, write_file)

def dfs(i, data, parent, p_name):
    s = 0
    while i < len(data):
        exec_time = re.findall(r'\d+\.{1}\d+', data[i])
        func_name = re.findall(r'_{0,2}?\w+[\w.\w*]* ?\[?\w+?\]?\(\);?', data[i])
        func_end = re.findall(r'}', data[i])
        ret_func_name = re.findall(r'(}) \/\* (_{0,2}?\w+[\w.\w*]* ?\[?\w+?\]?) \*\/', data[i])
        if len(func_name) > 0 and isLeaf(func_name[0]) == False:
            func_name[0] = func_name[0].replace("()","")
            item={}
            item["name"] = func_name[0]
            item["value"] = 0
            item["children"] = []
            parent["children"].append(item)
#            item = ET.SubElement(parent, func_name[0])
            i = dfs(i+1, data, item, func_name[0])
        elif len(func_name) > 0 and isLeaf(func_name[0]) == True:
            func_name[0] = func_name[0].replace("()","")
            func_name[0] = func_name[0].replace(";","")
            leaf = {}
            leaf["name"] = func_name[0]
            leaf["value"] = float(exec_time[0])
            parent["children"].append(leaf)
            i+=1
        elif (len(func_end) == 1 ):
            parent["size"] = float(exec_time[0])
            return i+1
        else:
            i+=1
            continue        

if __name__ == "__main__":
    parser()
