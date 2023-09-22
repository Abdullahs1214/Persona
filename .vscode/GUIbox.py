from tkinter import *
root = Tk()

root.title("My GUI App")
#iconpath = "C:\\Users\\srskh\\Code files\\.vscode\\dzb.ico"
#root.wm_iconbitmap(iconpath)
root.geometry("500x500")
mylabel = Label(root, text="my new gui app").grid(row=0,column=1)

mylabel2 = Label(root, text= "line 2").grid(row=0,column=2)


root.mainloop()