from tkinter import *
from random import *

root = Tk()
root.title("Employee Data App")
root.geometry("350x400")


def creating_text_file():
    save_file = open("PersonalData.txt", "a")
    title = "Personal Datas"
    line = "\n"
    save_file.write(title)
    save_file.write(line)
    save_file.close()


def onClick():

    if clicked.get() == "Young":
        age = randrange(1, 30)
    elif clicked.get() == "Mid-age":
        age = randrange(31, 55)
    elif clicked.get() == "Elder-age":
        age = randrange(56, 85)

    emptyLabel1 = Label(root, text=" ").grid()
    nameLabelOut = Label(root, text="Name: " + inputNameField.get())
    nameLabelOut.grid()

    ageLabel = Label(root,text="Age: " + age.__str__())
    ageLabel.grid()

    ageCategoryLabel = Label(root, text="Age-category: " + clicked.get())
    ageCategoryLabel.grid()

    save_file = open("PersonalData.txt", "a")
    save_file.write(str(inputNameField.get() + " " + age.__str__()))
    save_file.write("\n")
    save_file.close()


myLabel = Label(root, text="Name")
myLabel.grid(row=0, column=0)

spaceLabel1 = Label(root, text=" ").grid()

inputNameField = Entry(root)
inputNameField.grid(row=2, column=0)

clicked = StringVar()
clicked.set("Select employees age category")
ageDropDownMenu = OptionMenu(root, clicked, "Young", "Mid-age", "Elder-age")
ageDropDownMenu.grid(row=2, column=1)

sendButton = Button(root, text="Save person", command=onClick, fg="blue")
sendButton.grid(row=3, column=0)

creating_text_file()
root.mainloop()
