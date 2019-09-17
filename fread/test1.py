import xml.etree.ElementTree as ET

def main():
    # create the file structure
    data = ET.Element('data')
    a(data, "item")
    
    mydata = ET.tostring(data)
    myfile = open("items2.xml", "w")
    myfile.write(mydata)

def a(data, string):
    items = ET.SubElement(data, string)
    b(items, "item1")
    return
def b(data, string):
    items = ET.SubElement(data, string)
    return

if __name__ == "__main__":
    main()
