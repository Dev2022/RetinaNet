import xml.etree.ElementTree as ET
import pickle
import os
from os import listdir, getcwd
from os.path import join
import glob


#classes = ["bicycle", "bus", "car", "carplate", "lorry", "motorbike", "person", "truck", "van"]
#classes = ["bicycle", "bus", "car", "lorry", "motorbike", "truck", "van"]
#classes = ["person"]
classes = ["aeroplane","bicycle","bird","boat","bottle","bus","car","cat","chair","cow","diningtable","dog","horse","motorbike","person","pottedplant","sheep","sofa","train","tvmonitor"]




def convert_annotation(image_id):
    in_file = open('/home/deva/s165/RFBNet-master/data/VOCdevkit/VOC2012/Annotations/%s.xml'%(image_id))
    
    out_file_csv = open('/home/deva/s165/Focal_loss_for_object_detection-master/data/train.txt', 'a')
    
    tree=ET.parse(in_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)
    count=0
    out_file_csv.write('%s.jpg'%(image_id))
    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            continue
        else:
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            
            
            out_file_csv.write(" " + xmlbox.find('xmin').text+".0 "+xmlbox.find('ymin').text+".0 "+xmlbox.find('xmax').text+".0 "+xmlbox.find('ymax').text)
            out_file_csv.write(".0 " + str(cls_id))

    out_file_csv.write('\n')


list_name=glob.glob("/home/deva/s165/RFBNet-master/data/VOCdevkit/VOC2012/Annotations/*.xml")

for i in range(0, len(list_name)):
 
  list_name1=list_name[i].split("Annotations/")
  list_name2=list_name1[1].split(".xml")
  #print(list_name2[0])
  convert_annotation(list_name2[0])
  


