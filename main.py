from tkinter import *
from google_translate import *

def evaluateEvent(event):
    evaluateButton()

def evaluateButton():
    res.configure(text = translateSentence(str(entry.get())))


def set_text(text):
    ind = len(entry.get())+1
    entry.insert(ind,text)
    return

def delete_text():
    entry.delete(0,END)
    return

def stylingMethod(root):
	root.iconbitmap('translator.ico')
	root.title('Desktop Google Translator')


root = Tk()

stylingMethod(root)

topFrame = Frame(root)
topFrame.pack()

translateButton = Button(topFrame,text="Translate",command=evaluateButton)
translateButton.pack(side=TOP)
Label(topFrame, text="Please type here what would you like to translate:").pack(side=TOP)

entry = Entry(topFrame)
entry.bind("<Return>", evaluateEvent)
entry.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

res = Label(bottomFrame)
res.pack(side=TOP)

quitButton = Button(bottomFrame,text="Quit",command=topFrame.quit)
quitButton.pack(side=BOTTOM)


root.mainloop()