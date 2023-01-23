# Import all widgets from Tkinter
from tkinter import *
import tkinter as tk

# Frame is the Tkinter frame class that out class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Width,Height) in pixels
        self.master.maxsize(500,300)
        self.master.title('MY Program')
        self.lbl_fname =tk.Label(self.master,text='Hello User')
        self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

        self.closeButton =Button(self.master,text="Close",width=5, height=2)
        self.closeButton.grid(row=1,column=0,padx=(27,0),pady=(10,0),sticky=E+W)
        
       


if __name__ == "__main__":
    root = tk.Tk() # This is the syntax to create the window
    App = ParentWindow(root) # This passes the window to our class defined above
    root.mainloop() # Creates a loop so it is persistant and doesn't just close after running initially
        
