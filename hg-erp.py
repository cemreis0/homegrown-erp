import tkinter
from tkinter import *
import webbrowser

db_name = "db.csv"
column = len(open(db_name).readlines())

root = Tk()
root.geometry("1100x500")

app_name = Label(root, text="app_name")
app_name.grid(row=0, column=0)

entry = Entry(root, width=25)

def readdb(db_name, index, line):
    db = open(db_name)
    db_line = db.readlines()
    db_item = db_line[line].split(",")
    if "\n" in db_item[line]:
        db_item[line] = db_item[line].replace("\n", "")
    db_spec_item = db_item[index]
    db.close()
    return db_spec_item

def update():
    for widget in root.winfo_children():
        widget.destroy()
    main()


def main():
    def open_url():
        webbrowser.open_new(readdb(db_name, j, i))
    for i in range(0,column):
        for j in range(0,7):
            if j == 6:
                url_button = Button(root, text=readdb(db_name, j, i), command=open_url, fg="blue")
                url_button.grid(row=i+1,column=j,padx=10,pady=10)
            else:
                entry = Entry(root, width=25)
                entry.insert("0", readdb(db_name,j,i))
                entry.config(state=DISABLED)
                entry.grid(row=i+1, column=j, padx=10, pady=10)
    reload_button = Button(root, text="RELOAD", command=update, fg="white", bg="blue", height=2, width=10)
    reload_button.grid(row=i+2, column=3, padx=10, pady=10)

main()
tkinter.mainloop()