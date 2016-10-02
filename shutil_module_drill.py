import shutil
from Tkinter import *
from ttk import *
import os, sys
import functools


root = Tk()
label = Label(root, text = 'Click button to move all files from Folder A to Folder B')
label.pack()
    

def move_all():
    shutil.move(r'C:\Users\Student\Desktop\Folder A\Document1.txt',
            r'C:\Users\Student\Desktop\Folder B')
    shutil.move(r'C:\Users\Student\Desktop\Folder A\Document2.txt',
            r'C:\Users\Student\Desktop\Folder B')
    shutil.move(r'C:\Users\Student\Desktop\Folder A\Document3.txt',
            r'C:\Users\Student\Desktop\Folder B')
    shutil.move(r'C:\Users\Student\Desktop\Folder A\Document4.txt',
            r'C:\Users\Student\Desktop\Folder B')

    path = r'C:\Users\Student\Desktop\Folder B'
    dirs = os.listdir(path)

    for file in dirs:
        print file

button = Button(root, text = 'Click Me!', command = lambda: move_all())
button.pack()


root.mainloop()

  
