import random
import shutil
import os
import glob

path_datasets = 'DATASETS_produccion/'

def add_clases_to_object(input,lista, object_name):
    output = input
    for item in lista:
        if output=='':
            output += object_name + ':' + item
        else:
            output += '\n' + object_name + ':' + item
    return output

'''
CLASES ANTES
0 cable: hebra cortada
1 cable: objeto extraño
2 cable: dañado
3 cable: fretting

4 aislador: bueno
5 aislador: roto
6 aislador: con descarga eléctrica
7 aislador: contaminado
8 aislador: ausente
9 aislador: desaplomado
10 aislador: objeto extraño


11 amortiguador: Bueno
12 amortiguador: Roto
13 amortiguador: contaminado
14 amortiguador: objeto extraño

15 baliza: buena
16 baliza: rota
17 baliza: contaminado
18 baliza: objeto extraño

19 estructura: nido de pájaro
20 estructura: óxido
21 estructura: escremento de pájaro
22 estructura: objeto extraño
'''

'''
CLASES AHORA
0 cable: hebra cortada
1 cable: hebra cortada en separador
2 cable: objeto extraño
3 cable: dañado
4 cable: fretting

5 aislador: roto
6 aislador: ausente
7 aislador: con descarga eléctrica
8 aislador: con óxido
9 aislador: con excremento de pájaro
10 aislador: sucio
11 aislador: desaplomado
12 aislador: con objeto extraño

13 amortiguador: bueno
14 amortiguador: Roto
15 amortiguador: con óxido
16 amortiguador: con excremento de pájaro
17 amortiguador: con objeto extraño

18 baliza: bueno
19 baliza: roto
20 baliza: contaminado
21 baliza: objeto extraño

22 estructura: nido de pájaro
23 estructura: óxido
24 estructura: escremento de pájaro
25 estructura: objeto extraño
'''
cable_list = ['hebra cortada','hebra cortada en separador','objeto extraño','dañado','fretting']
aislador_list = ['roto','ausente','con descarga eléctrica','con óxido','con excremento de pájaro','sucio','desaplomado','con objeto extraño']
amortiguador_list = ['bueno','roto','con óxido','con excremento de pájaro','con objeto extraño']
baliza_list = ['bueno','roto','contaminado','objeto extraño']
estructura_list = ['nido de pájaro','óxido','escremento de pájaro','objeto extraño']

clases_text = ''

clases_text = add_clases_to_object(clases_text,cable_list, 'cable')
clases_text = add_clases_to_object(clases_text,aislador_list, 'aislador')
clases_text = add_clases_to_object(clases_text,amortiguador_list, 'amortiguador')
clases_text = add_clases_to_object(clases_text,baliza_list, 'baliza')
clases_text = add_clases_to_object(clases_text,estructura_list, 'estructura')


dict_change_classes = {
    '0': 0,
    '1': 2,
    '2': 3,
    '3': 4,
    '5': 5,
    '6': 7,
    '8': 6,
    '9': 11,
    '10': 12,
    '11': 13,
    '12': 14,
    '13': 16,
    '14': 17,
    '15': 18,
    '16': 19,
    '17': 20,
    '18': 21,
    '19': 22,
    '20': 23,
    '21': 24,
    '22': 25,
}



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
folders = os.listdir(path_datasets)
for folder in folders:
    print(folder)
    count=0
    # GET IMAGES
    ext = ['png', 'jpg', 'jpeg','JPG']
    files = []
    [files.extend(readFileNames(path_datasets + folder + '/', '*' + e)) for e in ext]
    for img_name in files:
        label_name = img_name.split('.')[0] + '.txt'
        if os.path.exists(label_name):
            with open(label_name, "r+") as f:
                old = f.read() # read everything in the file
                new = ''
                for line in old.split('\n'):
                    if line != '':
                        items = line.split(' ')
                        if items[0] in dict_change_classes.keys():
                            new_class = dict_change_classes[str(items[0])]
                            if new_class!=None:
                                new +=  str(new_class) + ' ' + ' '.join(items[1:]) + '\n'
                f.truncate(0)
                f.seek(0) # rewind
                f.write(new) # write the new line before
                count+=1
        else:
            count+=1
            open(label_name, mode='a').close()
    print('modificados: ' + str(count))
    print()

    # GET TEXT
    ext = ['txt']
    files = []
    [files.extend(readFileNames(path_datasets + folder + '/', '*' + e)) for e in ext]
    for txt_file in files:
        if 'classes.txt' in txt_file:
            with open(txt_file, "r+") as f:
                f.truncate(0)
                f.seek(0) # rewind
                f.write(clases_text) # write the new line before