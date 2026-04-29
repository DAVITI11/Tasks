import tkinter as t
root = t.Tk()
root.title("calculator")
root.geometry("500x500")

t1 = t.StringVar()
t1.set("")

entry = t.Entry(root, textvariable=t1)
entry.grid(row=0, column=0, columnspan=4)

def add_num(num):
    current = t1.get()
    t1.set(current + str(num))

def clear():
    t1.set("")

def calculate():
    try:
        result = eval(t1.get())
        t1.set(result)
    except:
        t1.set("Error")

buttons = []
for i in range(9, -1, -1):
    buttons.append(t.Button(root, text=i, width=5, height=2,command=lambda : add_num(i)))

for i, btn in enumerate(buttons):
    btn.grid(row=1 + i // 3, column=i % 3)

bottonpl = t.Button(root, text="+", width=5, height=2, command=lambda: add_num("+"))
bottonpl.grid(row=1, column=3)
bottonmin = t.Button(root, text="-", width=5, height=2,command=lambda: add_num("-"))
bottonmin.grid(row=2, column=3)
bottondiv = t.Button(root, text="/", width=5, height=2,command=lambda: add_num("/"))
bottondiv.grid(row=3, column=3)
bottonmul = t.Button(root, text="*", width=5, height=2,command=lambda: add_num("*"))
bottonmul.grid(row=4, column=3)
bottoneq = t.Button(root, text="=", width=5, height=2,command=calculate)
bottoneq.grid(row=4, column=2)
bottonclear = t.Button(root, text="C", width=5, height=2,command=clear)
bottonclear.grid(row=4, column=1)

root.mainloop()