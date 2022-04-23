import tkinter
from tkinter import *
import webbrowser

db_file = "db.csv"

root = Tk()
root.geometry("1100x500")


# get the title of the window
def gettitle():
    root.title("app-name")


# get the number of lines the .csv file has
def getrownumber(db_name):
    row = len(open(db_name).readlines())
    return row


def opendb(db_name):
    db = open(db_name)
    return db


# get the header of each column
def getcolumnnames():
    ao_approved = Label(root, text="AO APPROVED")
    ao_approved.grid(row=1, column=0, padx=5, pady=5)
    vendor_name = Label(root, text="VENDOR NAME")
    vendor_name.grid(row=1, column=1, padx=5, pady=5)
    integer1 = Label(root, text="INTEGER")
    integer1.grid(row=1, column=2, padx=5, pady=5)
    total_amount = Label(root, text="TOTAL AMOUNT")
    total_amount.grid(row=1, column=3, padx=5, pady=5)
    integer1 = Label(root, text="INTEGER")
    integer1.grid(row=1, column=4, padx=5, pady=5)
    integer1 = Label(root, text="INTEGER")
    integer1.grid(row=1, column=5, padx=5, pady=5)
    url = Label(root, text="URL")
    url.grid(row=1, column=6, padx=5, pady=5)


# get a single comma separated value in the .csv file
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
    gettitle()
    getappname()
    getcolumnnames()
    getreloadbutton()
    opendb(db_file)

    # direct the user to the browser
    def open_url():
        webbrowser.open_new(getitem(db_file, j, i))

    # carry out i-j indexing to print out the rows and columns
    for i in range(0, getrownumber(db_file)):
        for j in range(0, 7):
            if j == 6:
                # hyperlink button
                url_button = Button(root, text=getitem(db_file, j, i), command=open_url, fg="blue", bg="white")
                url_button.grid(row=i+2, column=j, padx=10, pady=10)
            else:
                # entry boxes
                entry = Entry(root, width=25)
                entry.insert("0", getitem(db_file, j, i))
                entry.config(state=DISABLED)
                entry.grid(row=i+2, column=j, padx=10, pady=10)


# destroy all entries and execute the main function to refresh the page
def destroywidget():
    for widget in root.winfo_children():
        widget.destroy(),
    main()


# button the trigger destroywidget() function
def getreloadbutton():
    reload_button = Button(root, text="RELOAD", fg="white", bg="blue", height=2, width=10, command=destroywidget)
    reload_button.grid(row=int(getrownumber(db_file))+3, column=3, padx=10, pady=10)
    return reload_button


def getappname():
    app_name = Label(root, text="app-name")
    app_name.grid(row=0, column=0, padx=25, pady=25)


main()
tkinter.mainloop()
