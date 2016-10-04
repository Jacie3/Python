import os
import time
import datetime
import shutil

now = datetime.datetime.now()
ago = now - datetime.timedelta(hours = 24)

spath = 'C:\Users\Student\Desktop\Folder A'
dest = 'C:\Users\Student\Desktop\Folder B'

for filename in os.listdir(spath):
    path = os.path.join(spath, filename)
    statinfo = os.stat(path)
    mtime = datetime.datetime.fromtimestamp(statinfo.st_mtime)
    if mtime > ago and filename.endswith('.txt'):
        src = os.path.join(spath, filename)
        dst = os.path.join(filename, dest)
        shutil.move(src, dst)
        print ("{} This file has been modifed within the last 24 hours, and has been moved to {} ".format(filename, dst))
    
