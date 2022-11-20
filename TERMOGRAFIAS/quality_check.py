import glob, os

path_dataset = 'DATASET/'

os.chdir(path_dataset)

for file in glob.glob("*.txt"):
    if file != 'classes.txt':
        with open(file, "r+") as f:
            old = f.read() # read everything in the file
            new = ''
            for line in old.split('\n'):
                if line != '':
                    items = line.split(' ')
                    if len(items)==5:
                        new +=  '0 ' + ' '.join(items[1:]) + '\n'
            f.truncate(0)
            f.seek(0) # rewind
            f.write(new) # write the new line before