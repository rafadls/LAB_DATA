import random
import shutil
import os
import glob

path_dataset = 'DATASET/'

# GET IMAGES
ext = ['png', 'jpg', '.jpeg','JPG']    # Add image formats here

files = []
[files.extend(glob.glob(path_dataset  + '*.' + e)) for e in ext]

# ITERATE
for img_name in files:
    label_name = img_name.split('.')[0] + '.txt'
    if not os.path.exists(label_name):
        open(label_name, mode='a').close()