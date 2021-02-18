from dataset import read_xml_file
import constants
from dataset import read_xml_file
import os

def get_dataset(url):
    data_list = open(url, 'r').read().splitlines()
    return data_list

train_dataset_ids = get_dataset(constants.TRAIN_PATH)
val_dataset_ids = get_dataset(constants.VAL_PATH)

train_dataset_list = []
val_dataset_list = []

train_label_map = open(constants.TRAIN_LABEL_MAP_PATH, 'a+')
val_label_map = open(constants.VAL_LABEL_MAP_PATH, 'a+')


for id in train_dataset_ids:
    xml_path = constants.annotation_path + id + '.xml'
    image_boxes = read_xml_file(xml_path)
    train_dataset_list += image_boxes

for id in val_dataset_ids:
    xml_path = constants.annotation_path + id + '.xml'
    image_boxes = read_xml_file(xml_path)
    val_dataset_list += image_boxes

for item in train_dataset_list:
    train_label_map.write(item + '\n')

for item in val_dataset_list:
    val_label_map.write(item + '\n')

train_label_map.close()
val_label_map.close()