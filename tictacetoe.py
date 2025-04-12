from tkinter import *

turn = "O"

a1 = ""
a2 = ""
a3 = ""
b1 = ""
b2 = ""
b3 = ""
c1 = ""
c2 = ""
c3 = ""

def checker():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3
    if a1 == a2 and a1 == a3 == "O" or a1 == a2 and a1 == a3 == "X": #TOP
        z1 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z2 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z3 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z1.grid(row=1, column=1)
        z2.grid(row=1, column=2)
        z3.grid(row=1, column=3)
    elif b1 == b2 and b1 == b3 == "O" or b1 == b2 and b1 == b3 == "X": #MID
        z1 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z2 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z3 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z1.grid(row=2, column=1)
        z2.grid(row=2, column=2)
        z3.grid(row=2, column=3)
    elif c1 == c2 and c1 == c3 == "O" or c1 == c2 and c1 == c3 == "X": #BOTTOM
        z1 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z2 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z3 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z1.grid(row=3, column=1)
        z2.grid(row=3, column=2)
        z3.grid(row=3, column=3)
    elif a1 == b1 and a1 == c1 == "O" or a1 == b1 and a1 == c1 == "X": #LEFT-TOP
        z1 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z2 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z3 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z1.grid(row=1, column=1)
        z2.grid(row=2, column=1)
        z3.grid(row=3, column=1)
    elif a2 == b2 and a2 == c2 == "O" or a2 == b2 and a2 == c2 == "X": #MID-TOP
        z1 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z2 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z3 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z1.grid(row=1, column=2)
        z2.grid(row=2, column=2)
        z3.grid(row=3, column=2)
    elif a3 == b3 and a3 == c3 == "O" or a3 == b3 and a3 == c3 == "X": #LEFT-TOP
        z1 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z2 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z3 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z1.grid(row=1, column=3)
        z2.grid(row=2, column=3)
        z3.grid(row=3, column=3)
    elif a1 == b2 and a1 == c3 == "O" or a1 == b2 and a1 == c3 == "X": #RIGHT SLIDE
        z1 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z2 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z3 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z1.grid(row=1, column=1)
        z2.grid(row=2, column=2)
        z3.grid(row=3, column=3)
    elif a3 == b2 and a3 == c1 == "O" or a3 == b2 and a3 == c1 == "X": #RIGHT SLIDE
        z1 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z2 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z3 = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="red")
        z1.grid(row=1, column=3)
        z2.grid(row=2, column=2)
        z3.grid(row=3, column=1)

def switch():
    global turn
    if turn == "O":
        turn = "X"
    elif turn == "X":
        turn = "O"
def a1():
    global a1
    a1x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a1x.grid(row=1, column=1)
    a1 = turn
    checker()
    switch()

def a2():
    global a2
    a2x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a2x.grid(row=1, column=2)
    a2 = turn
    checker()
    switch()

def a3():
    global a3
    a1x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a1x.grid(row=1, column=3)
    a3 = turn
    checker()
    switch()

def b1():
    global b1
    a1x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a1x.grid(row=2, column=1)
    b1 = turn
    checker()
    switch()

def b2():
    global b2
    a1x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a1x.grid(row=2, column=2)
    b2 = turn
    checker()
    switch()

def b3():
    global b3
    a1x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a1x.grid(row=2, column=3)
    b3 = turn
    checker()
    switch()

def c1():
    global c1
    a1x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a1x.grid(row=3, column=1)
    c1 = turn
    checker()
    switch()

def c2():
    global c2
    a1x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a1x.grid(row=3, column=2)
    c2 = turn
    checker()
    switch()

def c3():
    global c3
    a1x = Label(window, text=turn, width=10, height=5, padx=3, pady=3, bg="grey")
    a1x.grid(row=3, column=3)
    c3 = turn
    checker()
    switch()

window = Tk()
window.title("GAWA NI RD")
#Buttons
a1 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=a1)
a2 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=a2)
a3 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=a3)
b1 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=b1)
b2 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=b2)
b3 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=b3)
c1 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=c1)
c2 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=c2)
c3 = Button(window, width=10, height=5, padx=3, pady=3, bg="grey", command=c3)

#Button Placing
a1.grid(row=1, column=1)
a2.grid(row=1, column=2)
a3.grid(row=1, column=3)
b1.grid(row=2, column=1)
b2.grid(row=2, column=2)
b3.grid(row=2, column=3)
c1.grid(row=3, column=1)
c2.grid(row=3, column=2)
c3.grid(row=3, column=3)

window.mainloop()