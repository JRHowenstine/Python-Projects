
import tkinter
from tkinter import *


class ParentWindow(Frame):
    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False,height=False) # This makes the window not adjustable by user
        self.master.geometry('{}x{}'.format(700, 400)) # This sets dimensions of window
        self.master.title('Learning Tkinter!') # Sets the title
        self.master.config(bg='lightgrey') # Sets background color

        self.varFName = StringVar() # make sure to assign things to self.
        self.varLName = StringVar()

        self.lblFName = Label(self.master,text='First Name: ',font=("Helvetica", 16), fg='black', bg='lightgrey' ) # Uses Label widget of tkinter
        self.lblFName.grid(row=0, column=0,padx=(30,0),pady=(30,0)) # grid is specific needs parameters... .pack just stacks in center vertically
        
        self.lblLName = Label(self.master,text='Last Name: ',font=("Helvetica", 16), fg='black', bg='lightgrey' )
        self.lblLName.grid(row=1, column=0,padx=(30,0),pady=(30,0)) # adds padding to label boxes in pixels

        self.lblDisplay = Label(self.master,text='',font=("Helvetica", 16), fg='black', bg='lightgrey' )
        self.lblDisplay.grid(row=3 , column=1,padx=(30,0),pady=(30,0))

        self.txtFName = Entry(self.master,text=self.varFName, font=("Helvetica", 16), fg='black', bg='lightblue') # creating a text box on main window using tkinter widget entry
        self.txtFName.grid(row=0 , column=1,padx=(30,0),pady=(30,0)) # can't use .grid and .pack in same window

        self.txtLName = Entry(self.master,text=self.varLName, font=("Helvetica", 16), fg='black', bg='lightblue') # creating a text box on main window using tkinter widget entry
        self.txtLName.grid(row=1 , column=1,padx=(30,0),pady=(30,0)) 

        self.btnSubmit = Button(self.master, text="Submit", width=10, height=2, command=self.submit) #Uses Button widget of tkinter
        self.btnSubmit.grid(row=2 , column=1,padx=(0,0),pady=(30,0), sticky=NE) # sticky North East means put to top right but takes padding into consideration

        self.btnSubmit = Button(self.master, text="Cancel", width=10, height=2, command=self.cancel)
        self.btnSubmit.grid(row=2 , column=1,padx=(0,90),pady=(30,0), sticky=NE)

    def submit(self):
        fn = self.varFName.get()
        ln = self.varLName.get()
        self.lblDisplay.config(text='Hello {} {}!'.format(fn,ln))

    def cancel(self):
        self.master.destroy()

        


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() # Important to have so the program doesn't just close immediately, this makes it continuosly run until we choose to close
    
