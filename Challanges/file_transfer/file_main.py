
import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
from datetime import datetime, timedelta
import time

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        self.master.title("File Transfer")

        # creates button for selecting file to transfer
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        # positoins source button using grid()
        self.sourceDir_btn.grid(row=0, column=0, padx=(20,10), pady=(30,0))

        # creates entry for source file
        self.source_dir = Entry(width=75)
        # postions ebtry box so it will line up with the button
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20,10), pady=(30,0))

        # creates the button for selecting the destination of the file
        self.destBir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        # positions the destination button using grid()
        self.destBir_btn.grid(row=1, column=0, padx=(20,10), pady=(15,10))

        # creates entry box for destination
        self.dest_dir = Entry(width=75)
        # postions the entry box inline with the button
        self.dest_dir.grid(row=1, column=1, columnspan=2, padx=(20,10), pady=(15,10))

        # creates tranfser button
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles) 
        # positions the button under the source and destination entries
        self.transfer_btn.grid(row=2, column=1, padx=(200,0), pady=(0,15)) 

        # creates tranfser button
        self.exit_btn = Button(text="Exit", width=20, command=self.exitProgram) 
        # positions the button under the source and destination entries
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15)) 

    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        self.source_dir.delete(0, END)
        self.source_dir.insert(0, selectSourceDir)

    def destDir(self):
        selectDestDir = tkinter.filedialog.askdirectory()
        self.dest_dir.delete(0, END)
        self.dest_dir.insert(0, selectDestDir)

    def transferFiles(self):
        # gets source directory
        source = self.source_dir.get()
        # gets destination directory
        destination = self.dest_dir.get()
        # gets list of files in the directory
        source_file = os.listdir(source)
        # runs through each file in the directory
        curTime = datetime.now()
        one_day = timedelta(hours=24)
        cuttOff = curTime - one_day
        for i in source_file:
            modTime = os.path.getmtime(source + "/" + i)
            print(modTime)
            if (time.time() - modTime) / (3600 >(24 * 1)):
                # moves each file from the source to the destination
                shutil.move(source + "/" + i, destination)
                print(i + " was succefully transfered")

    def exitProgram(self):
        root.destroy()

    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()