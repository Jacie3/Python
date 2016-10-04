import shutil
from Tkinter import *
from ttk import *
import os, sys
import functools



root = Tk()
label = Label(root, text = 'Click button to move all .txt files from Folder A to Folder B')
label.pack()
   
spath = 'C:\Users\Student\Desktop\Folder A'
dest = 'C:\Users\Student\Desktop\Folder B'
#print(os.listdir(spath))

def move_txt():
    for filename in os.listdir(spath):
        if filename.endswith('.txt'):
            src = os.path.join(spath, filename)
            dst = os.path.join(dest, filename)
            shutil.move(src, dst)
            print("{} moved to: {}".format(filename, dst))

button = Button(root, text='Click Me!', command = lambda: move_txt())
button.pack()

root.mainloop()



    
            
    
    
