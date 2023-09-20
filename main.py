from tkinter import *
import math

window = Tk()
window.geometry("400x400")
window.title("Base Converter")
img = PhotoImage(file='icon.ico')
window.iconphoto(False, img)

keys = open('keys.txt').read()


def removePlaceholder(*args):
    placeholder.set('')
def removePlaceholder2(*args):
    placeholder2.set('')

def Convert():
    p = int(placeholder.get())
    p2 = int(placeholder2.get())
    if p2<p:
        answer.set(keys[p2])
    else:
        powers=[]
        units = math.floor(round(math.log(p2,p),3))+1
        for i in range(units):
            powers.append(0)
            if i==units-1:
                powers[-1]+=p2
            else:
                while p2 - (p**(units-i-1)) >= (p**(units-i-2)) or p2==p**(units-i-1):
                    p2 -= p**(units-i-1)
                    powers[-1]+=1
        s = ""
        for i in powers:
            s += keys[i]
        answer.set(s)

placeholder = StringVar()
placeholder.set("Enter base here...")
e = Entry(window, textvariable=placeholder,font='Courier 20')
e.place(x=30,y=50)
e.bind("<Button-1>", removePlaceholder)

placeholder2 = StringVar()
placeholder2.set("Enter value to convert")
e2 = Entry(window, textvariable=placeholder2,font='Courier 20',width=23)
e2.place(x=10,y=100)
e2.bind("<Button-1>", removePlaceholder2)

b = Button(window, text="Convert",font='Courier 18',bg ='lightgrey',command=Convert).place(x=100,y=150)

answer = StringVar()
answer.set("0")
l=Entry(window,textvariable=answer,font='Courier 20',state='disabled').place(x=30,y=250)

window.mainloop()