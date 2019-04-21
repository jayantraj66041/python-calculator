import tkinter
from tkinter import *
root = tkinter.Tk()
root.title("Jayant's Calculator")
root.minsize(440, 505)
root.maxsize(440, 505)
top = Frame(root, width=400, height=150, bg="black")
top.pack(fil=X)

num = IntVar()
sum = ""
def clear():
    global sum
    #num.set(0)
    form.delete(0,END)
    sum = ""

def total(data):
    global sum
    sum += str(data)
    num.set(sum)

def final():
    global sum
    data = eval(sum)
    num.set(data)
    sum = ""

form = Entry(top, width=20, font="arial 27 bold", fg="white", bd=10, bg="black", textvariable=num)
form.pack()
bottom = Frame(root, width=400, height=450, bg="black")
bottom.pack(fill=X)
btn1 = Button(bottom, text="CE", width=4, bd=15, relief="raised", bg="black", fg="white", font="arial 20", command=clear)
btn2 = Button(bottom, text="C", width=4, bd=15, relief="raised", bg="black", fg="white", font="arial 20")
btn3 = Button(bottom, text="X", width=4, bd=15, relief="raised", bg="black", fg="white", font="arial 20")
btn4 = Button(bottom, text="/", width=4, command=lambda:total("/"), bd=15, relief="raised", bg="black", fg="white", font="arial 20")
btn5 = Button(bottom, text="7", width=4, command=lambda:total("7"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn6 = Button(bottom, text="8", width=4, command=lambda:total("8"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn7 = Button(bottom, text="9", width=4, command=lambda:total("9"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn8 = Button(bottom, text="*", width=4, command=lambda:total("*"), bd=15, relief="raised", bg="black", fg="white", font="arial 20")
btn9 = Button(bottom, text="4", width=4, command=lambda:total("4"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn10 = Button(bottom, text="5", width=4, command=lambda:total("5"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn11 = Button(bottom, text="6", width=4, command=lambda:total("6"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn12 = Button(bottom, text="-", width=4, command=lambda:total("-"), bd=15, relief="raised", bg="black", fg="white", font="arial 20")
btn13 = Button(bottom, text="1", width=4, command=lambda:total("1"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn14 = Button(bottom, text="2", width=4, command=lambda:total("2"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn15 = Button(bottom, text="3", width=4, command=lambda:total("3"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn16 = Button(bottom, text="+", width=4, command=lambda:total("+"), bd=15, relief="raised", bg="black", fg="white", font="arial 20")
btn17 = Button(bottom, text="+-", width=4, command=lambda:total("+-"), bd=15, relief="raised", bg="black", fg="white", font="arial 20")
btn18 = Button(bottom, text="0", width=4, command=lambda:total("0"), bd=15, relief="raised", bg="#4b4b4b", fg="white", font="arial 20")
btn19 = Button(bottom, text=".", width=4, command=lambda:total("."), bd=15, relief="raised", bg="black", fg="white", font="arial 20")
btn20 = Button(bottom, text="=", width=4, bd=15, command=final, relief="raised", bg="black", fg="white", font="arial 20")
btn1.grid(row=0, column=0, padx=5, pady=3)
btn2.grid(row=0, column=1, padx=5, pady=3)
btn3.grid(row=0, column=2, padx=5, pady=3)
btn4.grid(row=0, column=3, padx=5, pady=3)
btn5.grid(row=1, column=0, padx=5, pady=3)
btn6.grid(row=1, column=1, padx=5, pady=3)
btn7.grid(row=1, column=2, padx=5, pady=3)
btn8.grid(row=1, column=3, padx=5, pady=3)
btn9.grid(row=2, column=0, padx=5, pady=3)
btn10.grid(row=2, column=1, padx=5, pady=3)
btn11.grid(row=2, column=2, padx=5, pady=3)
btn12.grid(row=2, column=3, padx=5, pady=3)
btn13.grid(row=3, column=0, padx=5, pady=3)
btn14.grid(row=3, column=1, padx=5, pady=3)
btn15.grid(row=3, column=2, padx=5, pady=3)
btn16.grid(row=3, column=3, padx=5, pady=3)
btn17.grid(row=4, column=0, padx=5, pady=3)
btn18.grid(row=4, column=1, padx=5, pady=3)
btn19.grid(row=4, column=2, padx=5, pady=3)
btn20.grid(row=4, column=3, padx=5, pady=3)

root.mainloop()