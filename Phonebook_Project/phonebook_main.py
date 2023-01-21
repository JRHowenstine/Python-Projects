# Python Versin:    3.11.1
#
# Author:           Justin R. Howenstine (Instructed by The Tech Academy)
#
# Purpose:          Create a dummy phonebook, demonstrating OOP, Tkinter GUI module
#                   using Tkinter parent and child relationships.
#
# Tested OS:        This code was written and tested to work with Windows 11.

# Import all widgets from Tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox

# Import our other custom modules in order to have access to them
import phonebook_gui
import phonebook_func

# Frame is the Tkinter frame class that out class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define master frame configuration
        self.master = master
        self.master.minsize(500,300) #(Width,Height) in pixels
        self.master.maxsize(500,300)
        # This CenterWIndow method will center our app on the user's screen
        phonebook_func.center_window(self,500,300)
        self.master.title('The Tkinter Phonebook Demo')
        self.master.configure(bg="#f0f0f0")
        # This protocol method is a tkinter built-in method to catch if
        # the used clicks the upper corner, 'X' on the Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self))
        arg = self.master

        # Load in the GUI widgets from a separate module,
        # keeping you code compartmentalized and clutter free
        phonebook_gui.load_gui(self)




if __name__ == "__main__":
    root = tk.Tk() # This is the syntax to create the window
    App = ParentWindow(root) # This passes the window to our class defined above
    root.mainloop() # Creates a loop so it is persistant and doesn't just close after running initially
        
