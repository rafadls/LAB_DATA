import random
import shutil
import os
import glob

path_dataset = 'DATASET/'
path_yolo_dataset = 'DATASET_yolo/'

def create_folder(path_folder):
    try:
        shutil.rmtree(path_folder)
    except:
        pass
    os.makedirs(path_folder)

create_folder(path_yolo_dataset + 'train/images/')
create_folder(path_yolo_dataset + 'train/images/')
create_folder(path_yolo_dataset + 'train/labels/')
create_folder(path_yolo_dataset + 'val/images/')
create_folder(path_yolo_dataset + 'val/labels/')


# GET IMAGES
ext = ['png', 'jpg', 'jpeg','JPG']   # Add image formats here

files = []
[files.extend(glob.glob(path_dataset  + '*.' + e)) for e in ext]

# PARAMETERS
prob_train = 0.8

# ITERATE
for img_name in files:
    label_name = '.'.join(img_name.split('.')[:-1]) + '.txt'
    try:
        if random.uniform(0,1) < prob_train:
            shutil.copy2(label_name, path_yolo_dataset + 'train/labels/')
            shutil.copy2(img_name, path_yolo_dataset + 'train/images/')
        else:
            shutil.copy2(label_name, path_yolo_dataset + 'val/labels/')
            shutil.copy2(img_name, path_yolo_dataset + 'val/images/')
    except:
        print(label_name)