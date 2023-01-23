import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime


class ParentWindow(Frame):
    def __init__(self,master):
        Frame.__init__(self)
        # Sets title of the GUI window
        self.master.title("File Transfer")
        
        # Creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source",width=20, command=self.sourceDir)
        # Positions source button in GUI using tkinter grid()
        self.sourceDir_btn.grid(row=0,column=0, padx=(20,10),pady=(30,0))

        # Creates entry for source directory selection
        self.source_dir = Entry(width=75)
        # Positions entry in GUI using tkinter grid() padx and pady are the same as
        # the button to ensure they will line up
        self.source_dir.grid(row=0,column=1,columnspan=2,padx=(20,10),pady=(30,0))

        # Creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination",width=20, command=self.destDir)
        # Positions destination button in the GUI using tkinter grid()
        # on the next row under the source button
        self.destDir_btn.grid(row=1,column=0,padx=(20,10),pady=(15,10))

        # Creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        # Positions entry in the GUI using tkinter grid() padx pady same
        # as the button to ensure they will line up
        self.destination_dir.grid(row=1,column=1,columnspan=2,padx=(20,10),pady=(15,10))

        # Creates button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        # Position transfer files button
        self.transfer_btn.grid(row=2,column=1,padx=(200,0),pady=(0,15))

        # Create an Exit button
        self.exit_btn = Button(text="Exit", width=20,command=self.exit_program)
        # Positions the Exit button
        self.exit_btn.grid(row=2, column=2, padx=(10,40), pady=(0,15))

    # Creates function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        # The .delete(0,END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly
        self.source_dir.delete(0,END)
        # The .insert method will insert the user selection to the source_dir Entry
        self.source_dir.insert(0,selectSourceDir)

    # Creates function to select destination directory
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        # The .delete(0,END) will clear the content that is inserted in the Entry widget,
        # this allows the path to be inserted into the Entry widget properly
        self.destination_dir.delete(0,END)
        # The .insert method will insert the user selection to the destination_dir Entry
        self.destination_dir.insert(0,selectDestDir)

    # Creates function to transfer files from one directory to another
    def transferFiles(self):
        # Get source directory
        source = self.source_dir.get()
        # Get destination directory
        destination = self.destination_dir.get()
        # get a list of files in the source directory
        source_files = os.listdir(source)
        # Get current time and store it as a timestamp
        now = datetime.datetime.now()
        ts_now = now.timestamp()
        # Run through each file in the source directory
        for i in source_files:
            # Get the timestamp of each file in source folder
            ts_file = os.path.getmtime(source + "/" +i)
            # Subtract file's timestamp from current timestamp to find how long since modified
            ts_diff = ts_now - ts_file
            # if timestamp difference is less than 86400 seconds (24 hours) move file
            if ts_diff < 86400:
                # Move each file that was modified in the last 24 hours from the source to the destination
                shutil.move(source + '/' + i, destination)
                print(i + ' was successfully transferred.')

    # Create function to exit program
    def exit_program(self):
        # root is the main GUI window, the tkinter destroy method
        # tells Python to terminate root.mainloop and all widgets inside the GUI window
        root.destroy()



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
