# -*- coding: utf-8 -*-  
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os
from collections import Counter
import sys


if __name__ == '__main__':

    total_file = os.listdir(os.getcwd())
    total_xml = []
    for filename in total_file:
        if (filename.find('.xml')!=-1):
            total_xml+=[filename]

    pic_list=[]
    allname=[]

    for xmlName in total_xml:
        tree = ET.parse(xmlName)
        nameListPerPic=[]

        for elem in tree.iter(tag='name'):
            if (elem.text.find('.')!=-1):
                name_index=elem.text.find('.')
                class_name=int(elem.text[:name_index])
            else:
                class_name=int(elem.text)
            #print(elem.text)
            allname.append(class_name)
            nameListPerPic.append(class_name)
        
        pic_list.append(nameListPerPic)
        
    result = Counter(allname)

    print('----------')
    for res in result:
        result[res]=0
        for pic in pic_list:
            if (res in pic and pic.count(res)>=8):
                result[res]+=1
        if (result[res]<4):
            print('%d 类别不符合要求, 需要再标注 %d 张图片, 每张图片至少标记8个该类别样本'%(res,4-result[res]))

