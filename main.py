#Michael's Calculator
#Will upgrade to scientific calculator

from tkinter import*
import math
import parser
import tkinter.messagebox


# Set up the object; Object being the calculator
root = Tk()
root.title("Scientific Calculator")
root.configure(background = "gray")
root.resizable(width = False, height = False)
root.geometry("480x568+0+0")

calc = Frame(root)
calc.grid()

# Exit function allows the calculator to be closed by selecting File->Exit
def iExit():
    iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Confirm if you want to exit")
    if iExit > 0:
        root.destroy()
        return

# Scientific function will change the calculator to Scientific layout
def Scientific():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

# Standard function will change the calculator to Standard layout
def Standard():
    root.resizable(width=False, height=False)
    root.geometry("480x568+0+0")

menubar = Menu(calc)

# Arranging the 'File' menu
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit) # iExit added to this command

# Arranging the 'Edit' menu
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

# Create a Help menu
helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "View Help")

# Print the menu option 'File' to the calculator window
root.configure(menu = menubar)

#run a .mainloop() to start the calculator and keep it open
root.mainloop()

#def btnClick(numbers):
 #   global operator
  #  operator=operator + str(numbers)
   # text_Input.set(operator)

#def btnClearDisplay():
 #   global operator
  #  operator=""
   # text_Input.set("")

#def btnEqualsInput():
 #   global operator
  #  sumup=str(eval(operator))
   # text_Input.set(sumup)
    #operator=""

#operator=""
#text_Input =StringVar()

#txtDisplay = Entry(cal,font=('arial', 20, 'bold'), textvariable= text_Input,
 #                  bd=30, insertwidth=4, bg="powder blue", justify= 'right').grid(columnspan=4)

#btn7=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="7",bg="powder blue",command=lambda:btnClick(7)).grid(row=3, column=0)

#btn8=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="8", bg="powder blue",command=lambda:btnClick(8)).grid(row=3, column=1)

#btn9=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
#            text="9", bg="powder blue",command=lambda:btnClick(9)).grid(row=3, column=2)

#Addition=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
#            text="+", bg="powder blue",command=lambda:btnClick('+')).grid(row=3, column=3)
#==============================================================================

#btn4=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="4", bg="powder blue",command=lambda:btnClick(4)).grid(row=2, column=0)

#btn5=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="5", bg="powder blue",command=lambda:btnClick(5)).grid(row=2, column=1)

#btn6=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="6", bg="powder blue",command=lambda:btnClick(6)).grid(row=2, column=2)

#Subtraction=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="-", bg="powder blue",command=lambda:btnClick('-')).grid(row=2, column=3)
#==============================================================================

#btn1=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="1", bg="powder blue",command=lambda:btnClick(1)).grid(row=1, column=0)

#btn2=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="2", bg="powder blue",command=lambda:btnClick(2)).grid(row=1, column=1)

#btn3=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="3", bg="powder blue",command=lambda:btnClick(3)).grid(row=1, column=2)

#Multiply=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="*", bg="powder blue",command=lambda:btnClick('*')).grid(row=1, column=3)
#==============================================================================

#btn0=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="0", bg="powder blue",command=lambda:btnClick(0)).grid(row=4, column=0)

#btnClear=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="C", bg="powder blue",command=btnClearDisplay).grid(row=4, column=1)

#btnEquals=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="=", bg="powder blue",command=btnEqualsInput).grid(row=4, column=2)

#Division=Button(cal,padx=16,bd=8, fg="black", font=('arial', 20,'bold'),
 #           text="/", bg="powder blue",command=lambda :btnClick('/')).grid(row=4, column=3)


#cal.mainloop()
