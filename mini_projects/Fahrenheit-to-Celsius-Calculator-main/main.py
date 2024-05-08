from tkinter import *

root = Tk()
root.title("Fahrenheit to Celsius")
root.geometry("200x130")
root['background'] = '#262626'
root.resizable(False, False)


def buttonCtoF():
    if Fvar.get() == 1:
        trigvar.set(0)


def buttonFtoC():
    if trigvar.get() == 1:
        Fvar.set(0)


def calculate():
    hi = Enterin.get()
    try:
        if trigvar.get() == 1:
            fahrenheit = (float(hi) * 1.8) + 32
            label.config(text=fahrenheit)
        elif Fvar.get() == 1:
            celsius = (float(hi) - 32) * 5 / 9
            label.config(text=celsius)
    except:
        label.config(text="Not a Number")


label = Label(root, text='Enter Above')

Enterin = Entry(root)


Fvar = IntVar()
ff = Checkbutton(root, text='Fahrenheit to Celsius', variable=Fvar, onvalue=1, offvalue=0, command=buttonCtoF)
Fvar.set(1)

trigvar = IntVar()
trig = Checkbutton(root, text='Celsius to Fahrenheit', variable=trigvar, onvalue=1, offvalue=0, command=buttonFtoC)
trigvar.set(0)

calc = Button(root, text="Calculate", command=calculate)

Enterin.pack()
label.pack()
calc.pack()
ff.pack()
trig.pack()

if __name__ == "__main__":
    root.mainloop()
