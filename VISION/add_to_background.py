import random
import shutil
import os
import glob

path_dataset = 'DATASET/'
path_background = 'Background_Dataset/'

def create_folder(path_folder):
    try:
        shutil.rmtree(path_folder)
    except:
        pass
    os.makedirs(path_folder)

def readFileNames(folder, pattern): 
    return [image_path 
            for x in os.walk(folder) 
            for image_path in glob.glob(os.path.join(x[0], pattern))] 

create_folder(path_background)

count=0
ext = ['png', 'jpg', '.jpeg','JPG']
files = []
[files.extend(readFileNames(path_dataset, '*' + e)) for e in ext]
for img_name in files:
    label_name = img_name.split('.')[0] + '.txt'
    if os.path.exists(label_name):
        with open(label_name, "r+") as f:
            old = f.read() # read everything in the file
            if len(old)<=1:
                name_bg_file = "{:05d}".format(count)
                shutil.copy2(label_name, path_background + name_bg_file + '.txt')
                shutil.copy2(img_name, path_background + name_bg_file + '.jpg')
                count+=1
