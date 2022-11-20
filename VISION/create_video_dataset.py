import random
import shutil
import os
import glob

path_video_folders = 'Entregable/'
path_video_dataset = 'aws_transelec/'


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

create_folder(path_video_dataset)

folders = os.listdir(path_video_folders)
count=0
for folder in folders:
    # GET VIDEOS
    ext = ['mp4', 'MP4']  
    files = []
    [files.extend(readFileNames(path_video_folders + folder + '/', '*' + e)) for e in ext]

    # ITERATE
    for file_name in files:
        shutil.copy2(file_name, path_video_dataset + 'aws_transelec_' + str(count) + '.mp4')
        count+=1

