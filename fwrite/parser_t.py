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

    with open('fwrite.csv', mode='w') as data_file:
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
        with open('fwrite.csv', mode='a') as data_file:
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
        for i in range (1,dir_count+1):

            f = open(path+str(d)+"/"+str(i)+".txt", "r")
            data = []
            stack = []
            stack_c = 0
            for l in f:
                data.append(l)

            for line in data:
                exec_time = re.findall(r'\d+\.{1}\d+', line)
                func_name = re.findall(r'_{0,2}?\w+[\w.\w*]*\(\);?', line)
                func_end = re.findall(r'}', line)

                end_c = 0
                """
                This conditional branch prevents duplication
                """
                if "SyS_write()" in inf and inf["SyS_write()"][1] == i:
                    break
                if len(func_name) > 0 and isLeaf(func_name[0]) == False:
                    stack_c+=1
                    stack.append(func_name[0])
                elif len(func_name) > 0 and isLeaf(func_name[0]) == True:
                    if func_name[0] in inf:
                        inf[func_name[0]][0] += float(exec_time[0])
                    else:
                        inf[func_name[0]] = [float(exec_time[0]),i]
                elif ( len(func_end) == 1 ) :
                    """
                    This try and except injection is because ftrace sometimes traces a piece of the previous function.
                    """
                    try:
                        ret_func_name = stack.pop()
                    except IndexError:
                        continue
                    if ret_func_name in inf:
                        inf[ret_func_name][0] += float(exec_time[0])
                    else:
                        inf[ret_func_name] = [float(exec_time[0]),i]
                else:
                    pass
            print("stack_c : ", i,stack_c)
        ret[d] = inf

#    exportCSV(ret)
if __name__ == "__main__":
    parser()

















