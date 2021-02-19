import constants
import csv
import pandas as pd

df = pd.read_csv(constants.TRAIN_LABEL_MAP_PATH)
train_class_name_count = df.groupby("class_name")['image_id'].unique().count()

df2 = pd.read_csv(constants.VAL_LABEL_MAP_PATH)
val_class_name_count = df2.groupby("class_name")['image_id'].unique().count()


print(train_class_name_count)
print(val_class_name_count)