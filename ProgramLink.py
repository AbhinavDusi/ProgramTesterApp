from tkinter import *
from tkinter import messagebox
from tkinter.font import *
import requests
from GetProblemInfo import *
from Tester import *

def checkurl(url):
    urlFormat = "http://www.usaco.org/index.php?page=viewproblem2&cpid="
    if url[0 : len(urlFormat)] != urlFormat:
        print("Invalid Format!")
        return False
    rq = requests.get(url)
    if url[21 : len(url) - 1] not in rq.text:
        print("Invalid URL!")
        return False
    return True

def enter(url):
    if checkurl(url):
        problem = getProblemInfo(url)
        message = "'" + problem[0] + ".' " + problem[2] + ", " + problem[1] + ". " + problem[3] + "."
        messagebox.showinfo(title = "Entered Problem", message = message)
        root.destroy()
        createTester()
    else:
        messagebox.showerror(title = "Error!", message = "URL entered was not valid!")

root = Tk()
root.title("USACO Program Tester - Enter URL")
root.geometry("700x150")

headerFontStyle = Font(size = "30")
title = Label(root, text = "USACO Program Tester", font = headerFontStyle)
title.pack()

info = Label(root, text = "Input code for any USACO problem, and get verdict on test cases, or input custom test cases")
info.pack()

frameURLEntry = Frame(root)
frameURLEntry.pack()

label = Label(frameURLEntry, text = "Enter URL Here:")
label.grid(row = "0", column = "0")

url = StringVar() 
urlEntry = Entry(frameURLEntry, textvariable = url)
urlEntry.grid(row = "0", column = "1")

button = Button(frameURLEntry, text = "Enter", command = lambda: enter(url.get()))
button.grid(row = "0", column = "2")

root.mainloop()