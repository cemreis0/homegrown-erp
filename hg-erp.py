import tkinter
from tkinter import *
import webbrowser

db_file = "db.csv"

root = Tk()
root.geometry("1100x500")


def getrownumber(db_name):
    row = len(open(db_name).readlines())
    return row


def opendb(db_name):
    db = open(db_name)
    return db


def getitem(db_name, index, line):
    db = opendb(db_name)
    db_line = db.readlines()
    db_item = db_line[line].split(",")
    if "\n" in db_item[line]:
        db_item[line] = db_item[line].replace("\n", "")
    db_spec_item = db_item[index]
    db.close()
    return db_spec_item


def main():
    getappname()
    getreloadbutton()
    opendb(db_file)

    def open_url():
        webbrowser.open_new(getitem(db_file, j, i))

    for i in range(0, getrownumber(db_file)):
        for j in range(0, 7):
            if j == 6:
                url_button = Button(root, text=getitem(db_file, j, i), command=open_url, fg="blue")
                url_button.grid(row=i+1, column=j, padx=10, pady=10)
            else:
                entry = Entry(root, width=25)
                entry.insert("0", getitem(db_file, j, i))
                entry.config(state=DISABLED)
                entry.grid(row=i+1, column=j, padx=10, pady=10)


def destroywidget():
    for widget in root.winfo_children():
        widget.destroy(),
    main()


def getreloadbutton():
    reload_button = Button(root, text="RELOAD", fg="white", bg="blue", height=2, width=10, command=destroywidget)
    reload_button.grid(row=int(getrownumber(db_file))+2, column=3, padx=10, pady=10)
    return reload_button


def getappname():
    app_name = Label(root, text="app-name")
    app_name.grid(row=0, column=0)


main()
tkinter.mainloop()
