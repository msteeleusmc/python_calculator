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
root.configure(background = "gray")
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

#================================================================================
# Creating a text display for the calculator
textDisplay = Entry(calc, font=('arial',20,'bold'), bg="white",bd=30, width=29, justify=RIGHT)
textDisplay.grid(row=0, column=0, columnspan=4, pady=1)
textDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range(2,5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, font=('arial',20,'bold'), bd=4, text=numberpad[i]))
        btn[i].grid(row=j, column=k, pady=1)
        i += 1


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
    root.geometry("480x568+0+0")

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