import random
import shutil
import os
import glob

path_datasets = 'DATASETS_produccion/'
path_dataset = 'DATASET/'


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

create_folder(path_dataset)

# GET IMAGES
folders = os.listdir(path_datasets)
count=0
for folder in folders:
    # GET VIDEOS
    ext = ['png', 'jpg', 'jpeg','JPG']
    files = []
    [files.extend(readFileNames(path_datasets + folder + '/', '*' + e)) for e in ext]
    for img_name in files:
        label_name = '.'.join(img_name.split('.')[:-1]) + '.txt'
        if not os.path.exists(label_name):
            open(label_name, mode='a').close()
        name_file = "{:06d}".format(count)
        shutil.copy2(label_name, path_dataset + name_file + '.txt')
        shutil.copy2(img_name, path_dataset + name_file + '.jpg')
        count+=1