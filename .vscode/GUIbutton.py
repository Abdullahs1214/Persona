from tkinter import *
root = Tk()
root.title("My Button")
iconpath = "C:\\Users\\srskh\\Code files\\.vscode\\dzb.ico"
root.wm_iconbitmap(iconpath)
root.geometry("500x500")

def myclick():
    mylabel = Label(root, text = "Conductor we have a problem", fg = "red",)
    mylabel.pack()

mybutton = Button(root, text = "Hey click this", command = myclick, fg = "black", bg = "light blue", padx = 30, pady = 70)
mybutton.pack()
root.mainloop()