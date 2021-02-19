from cv2 import cv2
import numpy as np 
import pandas as pd
import constants
from random import randint
from numpy import asarray
from PIL import Image

# Create a black image
font = cv2.FONT_HERSHEY_SIMPLEX


def draw_boudingbox(img_info):
    img_path = constants.images_path + img_info['image_id']
    # window_name = img_info['image_id']
    image = Image.open(img_path)
    # convert image to numpy array
    image_array = asarray(image)
    cv2.rectangle(image_array,(img_info['x1'],img_info['y1']),(img_info['x2'],img_info['y2']),(0,255,0),1)
    cv2.putText(image_array, img_info['class_name'], (img_info['x1'], img_info['y1'] - 5), font, 0.4, (0, 255, 0), 1, cv2.LINE_AA)
    image_rgb = cv2.cvtColor(image_array,cv2.COLOR_BGR2RGB)
    cv2.imshow('image', image_rgb) 


df = pd.read_csv(constants.TRAIN_LABEL_MAP_PATH)
all_records = df.to_dict('records')
list_of_images = []

if all_records:
    for _ in range(10):
        rand_item = randint(0, len(all_records))
        print(rand_item)
        record = all_records[rand_item]
        print(record)
        img_path = constants.images_path + record['image_id']
        img = cv2.imread(img_path)
        draw_boudingbox(record)
    cv2.waitKey(0)