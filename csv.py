import os
import json
import xlwt
from xlwt import Workbook

"""
def writeCSV(filename="", name, value):
    with open("test.csv", mode="a") as data_file:
        csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        data_writer.writerow(
"""    

"""
        try:
            sheet1.write(down, right, current["name"])
            sheet1.write(down+1, right, current["value"])
        except ValueError:
            pass
"""

def dfs(root, wb, f):
    sheet1 = wb.add_sheet('Sheet 1')
    down=0
    right=0
    s = []

    l = []
    p_stack=[]


    for node in root:
        s.append(node)

    while(len(s) != 0):
        current = s.pop()
        
        try:
            parent = current["parent"]
            if parent not in p_stack:
                p_stack.append(parent)
        except KeyError:
            parent = "root"
        try:
            sheet1.write(down, right, current["name"])
            sheet1.write(down+1, right, current["value"])
        except :
            print("OVERWRITE: ", down, right)
            break
        try:
            for child in current["children"]:
                s.append(child)
            down = down + 2
        except KeyError:
            try:
                next_item = s.pop()
                s.append(next_item)
                if parent == next_item["parent"]:
                    p_stack.pop()
                    right = right + 1
                else:
                    level = 0
                    for _ in range(0, len(p_stack)):
                        tmp = p_stack.pop()
                        if tmp != next_item["parent"]:
                            level+=1
                        else:
                            break
                    down = down - 2*level
                    right = right + 1
            except IndexError:
                break

    wb.save(f+".xls")

def dfs_diff(root, compare,wb, f):
    sheet1 = wb.add_sheet('Sheet 1')
    down=0
    right=0
    s = []
    c_s = []
    l = []
    p_stack=[]
    c_p_stack = []

    for node in root:
        s.append(node)
    for compare in root:
        s.append(node)

    while(len(s) != 0):
        current = s.pop()
        c_current = c_s.pop()
        
        try:
            parent = current["parent"]
            c_parent = c_current["parent"]
            if parent not in p_stack:
                p_stack.append(parent)
            if c_parent not in c_p_stack:
                c_p_stack.append(c_parent)
        except KeyError:
            parent = "root"
            c_parent = "root"
        try:
            if current["name"] == compare_current["name"]:
                print(current["name"], current["value"], c_current["name"], c_current["value"])
#            sheet1.write(down, right, current["name"])
#            sheet1.write(down+1, right, current["value"])
        except :
            print("OVERWRITE: ", down, right)
            break
        try:
            for child in current["children"]:
                s.append(child)
            for child in c_current["children"]:
                c_s.append(child)
            down = down + 2
        except KeyError:
            try:
                next_item = s.pop()
                c_next_item = c_s.pop()
                s.append(next_item)
                c_s.append(c_next_item)

                if parent == next_item["parent"] and c_parent == c_next_item["parent"]:
                    p_stack.pop()
                    right = right + 1
                    #p_stack = []
                else:
                    level = 0
                    for _ in range(0, len(p_stack)):
                        tmp = p_stack.pop()
                        if tmp != next_item["parent"]:
                            level+=1
                        else:
                            break
                    down = down - 2*level
                    right = right + 1
            except IndexError:
                break

 
def main():
    directory = os.listdir('./anychart_jsons')

    for f in directory:
        wb = Workbook()
        with open("./anychart_jsons/"+f) as json_file:
            root = json.load(json_file)
        dfs(root["children"], wb, f)
    
    return

if __name__ == "__main__":
    main()
