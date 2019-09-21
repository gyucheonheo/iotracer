import sys
import os
import re
import csv

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

    with open('fopen_t.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(funcs)

    for flag, dic in inf.items():
        exec_t = []
        exec_t.append(flag)
        for _ in range( len(funcs) -1 ):
            exec_t.append(0.0)
        for name, extra in dic.items():
            index = func_rows[name]
            try:
                exec_t[index] = extra[0]
            except IndexError:
                print("index : ", index, len(exec_t), name)
        with open('fopen_t.csv', mode='a') as data_file:
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
        for i in range (dir_count):
            f = open(path+str(d)+"/test_"+str(i)+".dat", "r")
            data = []
            stack = []
            for line in f:
                data.append(line)
            for asdf, line in enumerate(data):
                exec_time = re.findall(r'\d+\.{1}\d+', line)
                func_name = re.findall(r'_{0,2}?\w+[\w.\w*]* ?\[?\w+?\]?\(\);?', line)
                func_end = re.findall(r'}', line)
                SyS_count = 0
                ret_func_name = re.findall(r'(}) \/\* (_{0,2}?\w+[\w.\w*]* ?\[?\w+?\]?) \*\/', line)
                """
                This conditional branch prevents duplication
                """
                if len(func_name) > 0 and func_name[0] == "SyS_open()":
                    SyS_count += 1

                if "SyS_open()" in inf and inf["SyS_open()"][1] == i and SyS_count > 1:
                    break
                if len(func_name) > 0 and isLeaf(func_name[0]) == False :
                    if func_name[0] not in inf:
                        inf[func_name[0]] = [0, i] # will update time later
#                    stack.append(func_name[0])
                elif len(func_name) > 0 and isLeaf(func_name[0]) == True:
                    if func_name[0] in inf:
                        inf[func_name[0]][0] += float(exec_time[0])
                    else:
                        inf[func_name[0]] = [float(exec_time[0]),i]
                elif ( len(func_end) == 1 ) :
                    """
                    This try and except injection is because ftrace sometimes traces a piece of the previous function.
                    """
                    if ret_func_name[0][1]+"()" in inf:
                        inf[ret_func_name[0][1]+"()"][0] += float(exec_time[0])
                    else:
                        inf[ret_func_name[0][1]+"()"] = [float(exec_time[0]),i]

        ret[d] = inf
    exportCSV(ret)
if __name__ == "__main__":
    parser()
