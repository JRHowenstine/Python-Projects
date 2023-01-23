"""
Generate a window which allows the user to input text for the body of a webpage
Take that text and with the click of a button have a webpage open in
new tab of browser with the inputed text from user
"""
# Import all need packages and modules
import tkinter as tk
from tkinter import *
import webbrowser

class ParentWindow(Frame):
    # Generate a GUI for user interaction in a window
    def __init__(self,master):
        Frame.__init__(self,master)
        self.master.title("Web Page Generator")
        # Create a Label and Entry widget to allow user to input text for browser
        self.lbl_Entry = tk.Label(self.master,text='Enter Webpage Text:')
        self.lbl_Entry.grid(row=0,column=0,padx=(25,0),pady=(10,0))
        self.txt_Entry = tk.Entry(width=100)
        self.txt_Entry.grid(row=0,column=1,padx=(25,0),pady=(10,0)) 
        # Create a button for the creation of webpage
        self.btn = Button(self.master, text="Generate Basic HTML Page", width=30,height=2, command=self.defaultHTML)
        self.btn.grid(padx=(10,10), pady=(10,10))

    def defaultHTML(self):
        # get the text entered by user and put it in body of webpage
        htmlText = self.txt_Entry.get()
        htmlFile = open("index.html","w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")




if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
