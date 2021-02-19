import constants
import csv
import pandas as pd

df = pd.read_csv(constants.TRAIN_LABEL_MAP_PATH)
train_class_name_count = df.groupby("class_name")['image_id'].unique()

df2 = pd.read_csv(constants.VAL_LABEL_MAP_PATH)
val_class_name_count = df2.groupby("class_name")['image_id'].unique()


for item in train_class_name_count:
    print(len(item))

print('------------------------------------------')

for item in val_class_name_count:
    print(len(item))