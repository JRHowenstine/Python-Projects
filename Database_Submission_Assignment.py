#We want to find .txt from a list, then print new list
import sqlite3
conn = sqlite3.connect('submission.db')
with conn:
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files(ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                col_fname TEXT)")
    conn.commit()

conn = sqlite3.connect('submission.db')

# tuple of file names
fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

"""
create a for loop that analyzes the tuple of file names
and finds only those that end with ".txt" and then splits
the names we want into one-element tuples
"""

# loop through each object in the tuple to find the file that end in .txt.
for x in fileList:
    if x.endswith('.txt'):
        with conn:
            cur = conn.cursor()
        #the value for each row will be one name out of the tuple therefore (x,)
        #will denote a one element tuple for each file ending with .txt.
            cur.execute("INSERT INTO tbl_files (col_fname) VALUES (?)", (x,))
            print(x)

conn.close()
