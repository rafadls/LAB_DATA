import random
import shutil
import os
import glob

path_dataset = 'DATASETS/Dataset_aws_transelec/'


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


# GET IMAGES
ext = ['png', 'jpg', 'jpeg','JPG']   # Add image formats here

files = []
[files.extend(glob.glob(path_dataset  + '*.' + e)) for e in ext]
files.sort()

folders = []
n_total_folder = len(files)//1000 + 1
print('n_total_folder:' + str(n_total_folder))
for i in range(n_total_folder):
    create_folder(path_dataset[:-1] + '_' + str(i) + '/')
    try:
        shutil.copy2(path_dataset + 'classes.txt', path_dataset[:-1] + '_' + str(i) + '/')
    except:
        continue

count = 0
for img_name in files:
    n_folder = count//1000
    label_name = '.'.join(img_name.split('.')[:-1]) + '.txt'
    path_folder = path_dataset[:-1] + '_' + str(n_folder) + '/'
    shutil.copy2(img_name, path_folder)
    shutil.copy2(label_name, path_folder)
    count+=1