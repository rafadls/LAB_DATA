import random
import shutil
import os
import glob
import cv2
import numpy as np

path_dataset_in = 'Dataset_aws_transelec/'

class CompareImage(object):

    def __init__(self, image_1, image_2):
        self.minimum_commutative_image_diff = 1
        self.image_1 = image_1
        self.image_2 = image_2

    def compare_image(self):
        commutative_image_diff = self.get_image_difference(self.image_1, self.image_2)

        return commutative_image_diff

    @staticmethod
    def get_image_difference(image_1, image_2):
        first_image_hist = cv2.calcHist([image_1], [0], None, [256], [0, 256])
        second_image_hist = cv2.calcHist([image_2], [0], None, [256], [0, 256])

        img_hist_diff = cv2.compareHist(first_image_hist, second_image_hist, cv2.HISTCMP_BHATTACHARYYA)
        img_template_probability_match = cv2.matchTemplate(first_image_hist, second_image_hist, cv2.TM_CCOEFF_NORMED)[0][0]
        img_template_diff = 1 - img_template_probability_match

        # taking only 10% of histogram diff, since it's less accurate than template method
        commutative_image_diff = (img_hist_diff / 10) + img_template_diff
        return commutative_image_diff

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
ext = ['png', 'jpg']  
files = []
[files.extend(readFileNames(path_dataset_in, '*' + e)) for e in ext]
minimo_error = 0.03

files.sort()

print('imágenes totales: ' + str(len(files)))

file_to_remove = []
# ITERATE
dict_img = {}

print('creando diccionario')

actual_video_name = None
img_array = []
for file_name in files:
    video_name = ' '.join(file_name.split('_')[:-1])
    if actual_video_name == None:
       actual_video_name =  video_name
    if actual_video_name == video_name:
        img_array.append(file_name)
    else:
        dict_img[actual_video_name] = img_array
        actual_video_name =  video_name
        img_array = []
        img_array.append(file_name)
dict_img[actual_video_name] = img_array

print('listo diccionario')

count = 0
for file_name in files:
    if count%100 == 0:
        print(count)
    count += 1
    if file_name not in file_to_remove:
        video_name = ' '.join(file_name.split('_')[:-1])
        video_list = dict_img[video_name]
        img = cv2.imread(file_name)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        resized = cv2.resize(img, (100,100), interpolation = cv2.INTER_AREA)
        for file_name_2 in video_list:
            if (not file_name_2 in file_to_remove) and file_name_2!=file_name:
                img_2 = cv2.imread(file_name_2)
                img_2 = cv2.cvtColor(img_2, cv2.COLOR_BGR2RGB)
                resized_2 = cv2.resize(img_2, (100,100), interpolation = cv2.INTER_AREA)

                compare_image = CompareImage(resized, resized_2)
                image_difference = compare_image.compare_image()

                if image_difference < minimo_error:
                    file_to_remove.append(file_name_2)

print('Comenzando a eliminar: ' + str(len(file_to_remove)) + ' elementos')

for file in file_to_remove:
    image_name = file
    label_name = image_name.split('.')[0] + '.txt'
    try:
        os.remove(image_name)
    except Exception as e: 
        print(e)
    try:
        os.remove(label_name)
    except Exception as e: 
        print(e)