import shutil
import os
import sys

if __name__ == '__main__':
    sources = [
        'window', 'gui.py'
    ]
    for file in sources:
        target = os.path.join('blivechat', file)
        if os.path.isfile(file):
            if os.path.exists(target):
                os.remove(target)
            shutil.copyfile(file, target)
        else:
            if os.path.exists(target):
                os.removedirs(target)
            shutil.copytree(file, target)



