import subprocess


# create dataset
print('creating dataset')
subprocess.call(['python','create_dataset.py'])
print('done')
print()

# clean
print('cleaning dataset')
subprocess.call(['python','quality_check.py'])
print('done')
print()

# create background dataset
print('creating background dataset')
subprocess.call(['python','add_to_background.py'])
print('done')
print()

# split dataset
print('creating YOLO dataset')
subprocess.call(['python','split_train_val.py'])
print('done')
print()