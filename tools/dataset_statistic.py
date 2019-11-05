# -*- coding: utf-8 -*-  
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
import os
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import argparse
import sys

def parse_txt(txt_dir,xml_dir):
    ftxt = open(txt_dir,'r')
    lines = ftxt.readlines()
    xmllist=[]
    for line in lines:
        line=os.path.join(xml_dir,line[:-1])
        line=line+'.xml'
        xmllist.append(line)
    
    return xmllist


def parse_args():
    """
       Parse input arguments
       """
    parser = argparse.ArgumentParser(description='Return data classes distribution')
    parser.add_argument('--txt', dest='txt_mode',
                        help='From a txt file load xml\'s name',
                        default=None, type=str)
    parser.add_argument('--txt_xml_dir',dest='xml_dir',
                        help='xml dir',
                        default=None,type=str)
    parser.add_argument('--dir', dest='dir_mode',
                        help='Load xml files from a dir',
                        default=None, type=str)

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()

    print('Called with args:')
    print(args)

    if args.txt_mode is not None:
        total_xml = parse_txt(args.txt_mode,args.xml_dir)
    elif args.dir_mode is not None:
        total_xml = os.listdir(args.dir_mode)
        for i in range(len(total_xml)):
            total_xml[i] = args.dir_mode+'/'+total_xml[i]
    else:
        sys.exit(1)

    print('Total xml file(s)')
    print(total_xml)
    
    pic_list=[]
    allname=[]
    xmllist=[]

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

    xxlist=[]
    yylist=[]
    appear_count=result
    classes_20=[]

    print('----------')
    for res in result:
        xxlist.append(res)
        yylist.append(result[res])
        appear_count[res]=0
        for pic in pic_list:
            if (res in pic):
                appear_count[res]+=1
        print('class name = '+ str(res) +' count in all data = '+ str(yylist[-1]) + ' count for appear on different picture = '+ str(appear_count[res]))

    print('total count = ' + str(np.sum(yylist)))

    plt.bar(xxlist, yylist)
    plt.show()


    fo = open('result.txt','w')
    for res in result:
        fo.write(str(res) + ' ' + str(yylist[-1]) + ' ' + str(appear_count[res]))
        fo.write('\n')

