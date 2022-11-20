import random
import shutil
import os
import glob

path_dataset = 'DATASET/'
path_detections_dataset = 'DATASET_detections/'
path_has = path_detections_dataset + 'has/'
path_no_has = path_detections_dataset + 'no has/'

def create_folder(path_folder):
    try:
        shutil.rmtree(path_folder)
    except:
        pass
    os.makedirs(path_folder)

create_folder(path_has)
create_folder(path_no_has)


# GET IMAGES
ext = ['png', 'jpg', 'gif']    # Add image formats here

files = []
[files.extend(glob.glob(path_dataset  + '*.' + e)) for e in ext]

# ITERATE
for img_name in files:
    try:
        label_name = img_name.split('.')[0] + '.txt'
        with open(label_name, "r+") as f:
            old = f.read() # read everything in the file
            if len(old)>1:
                shutil.copy2(label_name, path_has)
                shutil.copy2(img_name, path_has)
            else:
                shutil.copy2(label_name, path_no_has)
                shutil.copy2(img_name, path_no_has)
    except:
        print(img_name)
