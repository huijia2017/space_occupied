import os
from os.path import join, getsize


# os.walk--tupple(dirpath, dirnames, filenames)
def s(dir):
    size = 0
    for root, dirs, files in os.walk(dir):
        size += sum([getsize(join(root, name))
                     for name in files])
    return size / 1024 // 1024


file_size = s('C:\\hugo\\airspace')
print(file_size, "MB")
