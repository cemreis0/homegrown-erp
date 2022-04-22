import tkinter
from tkinter import *

db_name = "db.txt"
column = len(open(db_name).readlines())

def readdb(db_name, index, line):
    db = open(db_name)
    db_line = db.readlines()
    db_item = db_line[line].split(",")
    if "\n" in db_item[line]:
        db_item[line] = db_item[line].replace("\n", "")
    db_spec_item = db_item[index]
    db.close()
    return db_spec_item

root = Tk()
root.geometry("1100x500")

app_name = Label(root, text="app_name")
app_name.grid(row=0, column=0)

for i in range(0,column):
    for j in range(0,9):
        print(readdb(db_name,j,i))
        entry = Entry(root, width=25)
        entry.insert("0", readdb(db_name,j,i))
        entry.config(state=DISABLED)
        entry.grid(row=i, column=j, padx=5, pady=10)

tkinter.mainloop()