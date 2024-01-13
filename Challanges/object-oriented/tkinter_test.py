
from tkinter import *

def btn1():
    print("button 1 was pressed")

if __name__ == "__main__":

    win = Tk()
    f = Frame(win)
    b1 = Button(f, text = "Button1")
    b2 = Button(f, text = "Button2")
    b3 = Button(f, text = "Button3")
    list1 = Listbox(win, height = 3)
    sb = Scrollbar(win, orient=VERTICAL)
    v = StringVar()
    e = Entry(win, textvariable=v)
    e.pack(pady=10)
    v.get()
    list1.pack()
    sb.pack(side=LEFT, fill=Y)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)
    b3.pack(side=LEFT)
    label1 = Label(win, text=("this is a label for the buttons"))
    #label2 = Label(win, text=("this is a label for button2"))
    label1.pack()
    #label2.grid(row=2, column=0)
    f.pack()
    list1.insert(END, "Entry 1")
    list1.insert(END, "Entry 2")
    list1.insert(END, "Entry 3")
    list1.insert(END, "Entry 4")
    

    b1.configure(command= lambda: btn1())
    sb.configure(command=list1.yview)
    list1.configure(yscrollcommand=sb.set)
    win.mainloop()
