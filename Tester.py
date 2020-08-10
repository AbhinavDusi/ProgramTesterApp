import os
import shutil
from tkinter import *
from tkinter import messagebox
from tkinter.font import *
from subprocess import *
from PrintVerdicts import *

def onQuit(tester):
    os.remove("data.zip")
    os.remove("out.out")
    print("Quitting...")
    for file in os.listdir():
        if file.endswith(".in") or file.endswith(".out"):
            os.remove(file)
    tester.destroy()
    import ProgramLink

def testCase(caseNum):
    os.rename(str(caseNum) + ".in", "in.in"); 

    proc = Popen("java Main.java", shell = True)
    try:
        proc.communicate(timeout = 2)
    except:
        proc.kill()
        proc.communicate()

    os.rename("in.in", str(caseNum) + ".in"); 

    myresults, realresults = open("out.out").readlines(), open(str(caseNum) + ".out").readlines()
    if myresults != realresults:
        return -1, myresults, realresults

    return proc.returncode, myresults, realresults

def runJavaFile(text):
    open("text.txt", "a").write(text)
    #os.rename("text.txt", "Main.java")

    #A = accepted = 0
    #T = timeout = -9
    #X = wrong answer = -1 - check spacing
    #! = runtime error - check filename, main method, etc. = 1
    results, myans, ans = [], [], []
    numCases = 0
    for file in os.listdir():
        if file.endswith(".in") or file.endswith(".out"):
            numCases = numCases + 1

    numCases = (numCases - 1) / 2

    for i in range(1, int(numCases + 1)):
        r, m, a = testCase(i)
        results.append(r)
        myans.append(m)
        ans.append(a)
    
    printVerdicts(results, myans, ans)

def createTester():
    tester = Tk()
    tester.title("Test Code")
    tester.protocol("WM_DELETE_WINDOW", lambda: onQuit(tester))
    tester.geometry("700x350")

    headerFontStyle = Font(size = "25")
    label = Label(tester, text = "Paste Code and Hit Run! Supports Java Only!", font = headerFontStyle)
    label.pack()

    directions = Label(tester, text = "Input file is 'in.in' and output file is 'out.out'")
    directions.pack()

    codeFrame = Frame(tester)
    codeFrame.place(relheight = 0.5, relwidth = 0.75, relx = 0.125, rely = 0.25)
    
    textarea = Text(codeFrame)
    textarea.pack()

    submit = Button(tester, text = "Submit Code", command = lambda: runJavaFile(textarea.get("1.0", "end-1c")))
    submit.pack()

    tester.mainloop()