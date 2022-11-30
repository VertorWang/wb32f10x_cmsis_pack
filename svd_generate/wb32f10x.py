import os
import xml.etree.ElementTree as ET
from device import dataSvd

svd_dict = r"./WestBerry.WB32F10x_DFP/SVD/"
svd_path = r"./WestBerry.WB32F10x_DFP/SVD/WB32F10x.svd"

def __indent(elem, level=0):
    i = "\n" + level * "\t"
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "\t"
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            __indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def parseJson(parentNode: ET.Element, data: dict) -> ET.Element:
    for key, value in data.items():
        if key.find('_') != -1:
            key = key.split('_')[0]
        item1 = ET.Element(key)
        # 如果数据是字典，递归解析,将解析得到的数据返回
        if isinstance(value, dict):
            parseJson(item1, value)
        else:
            item1.text = value
        parentNode.append(item1)


device = ET.Element("device", {"schemaVersion": "1.1", "xmlns:xs": "http://www.w3.org/2001/XMLSchema-instance",
                               "xs:noNamespaceSchemaLocation": "CMSIS-SVD_Schema_1_1.xsd"})
tree = ET.ElementTree(device)
parseJson(device, dataSvd)

# 添加外设寄存器域
__indent(device)

# 检查SVD文件夹是否存在，如果不存在就创建一个文件夹
if not os.path.exists(svd_dict):
    os.makedirs(svd_dict)
# 将生成的svd保存
tree.write(svd_path, encoding="utf-8", xml_declaration=True)