

import os
import glob

fPath = 'C:\\Assignment_Directory\\'

list_dir = os.listdir(fPath)
print(list_dir)



path = r'C:\\Assignment_Directory\\*.txt'

files = glob.glob(path)
print(files)

i = 0
while i<len(files):
    mtime = os.path.getmtime(files[i])
    print(str(files[i]) + " last modified " + str(mtime))
    i += 1
