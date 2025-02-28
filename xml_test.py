import xml.etree.ElementTree as ET

path_1 = '/Users/admin/Downloads/ON_EMCHD_20240907_85978867-6d1b-4885-b12f-ea07913c82c2.xml'

tree = ET.parse(path_1)
root = tree.getroot()




if __name__ == '__main__':

    for elem in root.iter():
        print(elem.tag, elem.attrib)
