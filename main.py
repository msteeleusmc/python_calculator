# Michael's Calculator
# Will upgrade to scientific calculator

from tkinter import*
import math
import parser
import tkinter.messagebox

#================================================================================
# Set up the object; Object being the calculator
root = Tk()
root.title("Scientific Calculator")
root.configure(background = "black")
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

#================================================================================
# Creating a text display for the calculator
textDisplay = Entry(calc, font=('arial',20,'bold'), bg="light gray",bd=30, width=29, justify=RIGHT)
textDisplay.grid(row=0, column=0, columnspan=4, pady=1)
textDisplay.insert(0, "0")

# Adding buttons to the calculator
numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial',20,'bold'), bd=4, bg="light gray", text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        i += 1

#================================================================================
# Creating buttons for various operations on the standard calculator
btnClear = Button(calc, text=chr(67), width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=1,column=0,pady=1)
btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=1,column=1,pady=1)
btnSq = Button(calc, text="√", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=1,column=2,pady=1)
btnAdd = Button(calc, text="+", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=1,column=3,pady=1)
btnSub = Button(calc, text="-", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=2,column=3,pady=1)
btnMult = Button(calc, text="*", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=3,column=3,pady=1)
btnDiv = Button(calc, text=chr(247), width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=4,column=3,pady=1)
btnPM = Button(calc, text=chr(177), width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=5,column=0,pady=1)
btnZero = Button(calc, text="0", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light gray").grid(row=5,column=1,pady=1)
btnDot = Button(calc, text=".", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="light gray").grid(row=5,column=2,pady=1)
btnEquals = Button(calc, text="=", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="orange").grid(row=5,column=3,pady=1)

#================================================================================
# Add scientific functions to the calculator
btnPi = Button(calc, text="π", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=1,column=4,pady=1)
btnCos = Button(calc, text="cos", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=1,column=5,pady=1)
btnTan = Button(calc, text="tan", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=1,column=6,pady=1)
btnSin = Button(calc, text="sin", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=1,column=7,pady=1)

btn2Pi = Button(calc, text="2π", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=2,column=4,pady=1)
btnCosh = Button(calc, text="cosh", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=2,column=5,pady=1)
btnTanh = Button(calc, text="tanh", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=2,column=6,pady=1)
btnSinh = Button(calc, text="sinh", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=2,column=7,pady=1)

btnLog = Button(calc, text="log", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=3,column=4,pady=1)
btnExp = Button(calc, text="Exp", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=3,column=5,pady=1)
btnMod = Button(calc, text="Mod", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=3,column=6,pady=1)
btnE = Button(calc, text="e", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=3,column=7,pady=1)

btnLog2 = Button(calc, text="log2", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=4,column=4,pady=1)
btnDeg = Button(calc, text="deg", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=4,column=5,pady=1)
btnACosh = Button(calc, text="acosh", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=4,column=6,pady=1)
btnASinh = Button(calc, text="asinh", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=4,column=7,pady=1)

btnLog10 = Button(calc, text="log10", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=5,column=4,pady=1)
btnLoglp = Button(calc, text="log1p", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=5,column=5,pady=1)
btnexpml = Button(calc, text="ecpm1", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=5,column=6,pady=1)
btnlgamma = Button(calc, text="lgamma", width=6, height=2, font=('arial',20,'bold'), bd=4,
                  bg="tan").grid(row=5,column=7,pady=1)




#================================================================================
# Exit function allows the calculator to be closed by selecting File->Exit
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

# Scientific function will change the calculator to a Scientific layout
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("958x568+0+0")

# Standard function will change the calculator to a Standard layout
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

#================================================================================
# Create the menu bar
menubar = Menu(calc)

#================================================================================
# Arranging the 'File' menu
filemenu = Menu(menubar, tearoff = 0)
# Adds the 'File' option to the window
menubar.add_cascade(label = "File", menu = filemenu)
# The 'File' menu lets you choose standard option
filemenu.add_command(label = "Standard", command = Standard)
# The 'File' menu lets you choose scientific option
filemenu.add_command(label = "Scientific", command = Scientific)
# Seperates with a line; Exit will appear below line
filemenu.add_separator()
# The 'File' menu lets you choose the exit option
filemenu.add_command(label = "Exit", command = iExit)

#================================================================================
# Arranging the 'Edit' menu
editmenu = Menu(menubar, tearoff = 0)
# Adds the 'Edit' option to the window
menubar.add_cascade(label = "Edit", menu = editmenu)
# The 'Edit' menu lets you choose cut
editmenu.add_command(label = "Cut")
# The 'Edit' menu lets you choose copy
editmenu.add_command(label = "Copy")
# Adds separator below copy
editmenu.add_separator()
# The 'Edit' menu lets you paste
editmenu.add_command(label = "Paste")

#================================================================================
# Create a Help menu
helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "View Help")

#================================================================================
# Print the menu option 'File' to the calculator window
root.configure(menu = menubar)
# Run a .mainloop() to start the calculator and keep it open
root.mainloop()