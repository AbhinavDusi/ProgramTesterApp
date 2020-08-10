from tkinter import *
from tkinter import simpledialog
from tkinter.font import *

def showCase(verdicts, length):
    answer = simpledialog.askstring("Input", "Which case to check? ", parent = verdicts)
    answer = int(answer)
    if answer > 1 and answer < length + 1:
        print("Case " + answer)

def printVerdicts(results, myans, ans):
    verdicts = Tk()
    verdicts.title("Verdicts")
    headerFontStyle = Font(size = "50")
    Label(verdicts, text = "Your Verdicts:", font = headerFontStyle).pack()

    for i in range(len(results)):
        res = "TEST"
        if results[i] == '-1':
            res = "X"
        if results[i] == '0':
            res = "A"
        if results[i] == '-9':
            res = "T"
        else:
            res = "!"
        Label(verdicts, text = "Case " + str(i + 1) + ": " + res).pack()

    Button(verdicts, text = "See input case result", command = lambda: showCase(verdicts, len(results))).pack()

    verdicts.mainloop()