import os
import time
import datetime
import shutil
from tkinter import *
from tkinter import ttk


class FileCheck(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.master = master
        self.master.minsize(300, 125)
        self.master.title('File Check App')

        self.frame1 = Frame(self.master)
        self.frame1.pack()

        self.label_header = Label(self.frame1, text = 'Welcome!')
        self.label_header.pack()

        self.label_message = Label(self.frame1, text = 'Choose your folders below: ')
        self.label_message.pack()

        self.frame2 = Frame(self.master)
        self.frame2.pack()

        self.source_button = Button(self.frame2, text = 'Source Folders: ', command = lambda: source(self))
        self.source_button.grid(row = 0, column = 0, padx = (25,0), sticky = NW)

        self.destination_button = Button(self.frame2, text = 'Destination Folders: ', command = lambda: destination(self))
        self.destination_button.grid(row = 0, column = 1, padx = (25, 25), sticky = NE)

        self.frame3 = Frame(master)
        self.frame3.pack(side = BOTTOM)
        self.submit_button = Button(self.frame3, text = 'Move Files', command = lambda: move(self))
        self.submit_button.grid(row = 0, column = 0, padx = (0, 0), pady = (15, 15))

        def source(self):
            x = filedialog.askdirectory(initialdir = [('/Users/jaciejermier/')])
            self.source_button['text'] = x

        def destination(self):
            y = filedialog.askdirectory(initialdir = [('/Users/jaciejermier/')])
            self.destination_button['text'] = y

        def move(self):
            x = self.source_button['text']
            y = self.destination_button['text']
            now = datetime.datetime.now()
            ago = now - datetime.timedelta(hours = 24)
            for filename in os.listdir(x):
                path = os.path.join(x, filename)
                statinfo = os.stat(path)
                mtime = datetime.datetime.fromtimestamp(statinfo.st_mtime)
                if mtime > ago and filename.endswith('.txt'):
                    src = os.path.join(x, filename)
                    dst = os.path.join(filename, y)
                    shutil.move(src, dst)
                    print (" {} file(s) moved to {} ".format(filename, dst))

if __name__ == "__main__":
    root = Tk()
    App = FileCheck(root)
    root.mainloop()
