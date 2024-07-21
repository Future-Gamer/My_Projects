from tkinter import *
import math
import tkinter.messagebox

main_window = Tk()
# Sets a title to the GUI Window
main_window.title("Scientific Calculator")
# Applying an icon to the window
main_window.iconbitmap('calculator.ico')
# sets the background colour of the window
main_window.configure(background = 'grey')
# fixed the width and height of GUI, hence it can't be resized
main_window.resizable(width=False, height=False)
# sets the geometry of the GUI window
main_window.geometry("480x568+450+90")
# holds the button in the calculator and acts as a container for the numbers and operators
calc = Frame(main_window)
# creates a grid like pattern for the Frame
calc.grid()

class Calc():
	def __init__(self):
		self.total=0
		self.current=''
		self.input_value=True
		self.check_sum=False
		self.op=''
		self.result=False

	def numberEnter(self, num):
		self.result=False
		firstnum=txtDisplay.get()
		secondnum=str(num)
		if self.input_value:
			self.current = secondnum
			self.input_value=False
		else:
			if secondnum == '.':
				if secondnum in firstnum:
					return
			self.current = firstnum+secondnum
		self.display(self.current)

	def sum_of_total(self):
		self.result=True
		self.current=float(self.current)
		if self.check_sum==True:
			self.valid_function()
		else:
			self.total=float(txtDisplay.get())

	def display(self, value):
		txtDisplay.delete(0, END)
		txtDisplay.insert(0, value)

	def valid_function(self):
		if self.op == "add":
			self.total += self.current
		if self.op == "sub":
			self.total -= self.current
		if self.op == "multi":
			self.total *= self.current
		if self.op == "divide":
			self.total /= self.current
		if self.op == "mod":
			self.total %= self.current
		self.input_value=True
		self.check_sum=False
		self.display(self.total)

	def operation(self, op):
		self.current = float(self.current)
		if self.check_sum:
			self.valid_function()
		elif not self.result:
			self.total=self.current
			self.input_value=True
		self.check_sum=True
		self.op=op
		self.result=False

	def Clear_Entry(self):
		self.result = False
		self.current = "0"
		self.display(0)
		self.input_value=True

	def All_Clear_Entry(self):
		self.Clear_Entry()
		self.total=0

	def pi(self):
		self.result = False
		self.current = math.pi
		self.display(self.current)

	def tau(self):
		self.result = False
		self.current = math.tau
		self.display(self.current)

	def e(self):
		self.result = False
		self.current = math.e
		self.display(self.current)

	def mathPM(self):
		self.result = False
		self.current = -(float(txtDisplay.get()))
		self.display(self.current)

	def squared(self):
		self.result = False
		self.current = math.sqrt(float(txtDisplay.get()))
		self.display(self.current)

	def cos(self):
		self.result = False
		self.current = math.cos(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def cosh(self):
		self.result = False
		self.current = math.cosh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def tan(self):
		self.result = False
		self.current = math.tan(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def tanh(self):
		self.result = False
		self.current = math.tanh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def sin(self):
		self.result = False
		self.current = math.sin(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def sinh(self):
		self.result = False
		self.current = math.sinh(math.radians(float(txtDisplay.get())))
		self.display(self.current)

	def log(self):
		self.result = False
		self.current = math.log(float(txtDisplay.get()))
		self.display(self.current)

	def exp(self):
		self.result = False
		self.current = math.exp(float(txtDisplay.get()))
		self.display(self.current)

	def acosh(self):
		self.result = False
		self.current = math.acosh(float(txtDisplay.get()))
		self.display(self.current)

	def asinh(self):
		self.result = False
		self.current = math.asinh(float(txtDisplay.get()))
		self.display(self.current)

	def expm1(self):
		self.result = False
		self.current = math.expm1(float(txtDisplay.get()))
		self.display(self.current)

	def lgamma(self):
		self.result = False
		self.current = math.lgamma(float(txtDisplay.get()))
		self.display(self.current)

	def degrees(self):
		self.result = False
		self.current = math.degrees(float(txtDisplay.get()))
		self.display(self.current)

	def log2(self):
		self.result = False
		self.current = math.log2(float(txtDisplay.get()))
		self.display(self.current)

	def log10(self):
		self.result = False
		self.current = math.log10(float(txtDisplay.get()))
		self.display(self.current)

	def log1p(self):
		self.result = False
		self.current = math.log1p(float(txtDisplay.get()))
		self.display(self.current)

added_value = Calc()

txtDisplay = Entry(calc, font=('Helvetica',20,'bold'), bg='black',fg='white', bd=30,width=28,justify=RIGHT)
txtDisplay.grid(row=0,column=0, columnspan=4, pady=1)
txtDisplay.insert(0,"0")

# stores all the numbers in a variable
numberpad = "789456123"
# here i will count the no of rows for placing the buttons in the grid
i=0
# create an empty list to store each button with its particular specifications
btn = []
# j is in that range to place the button in that particular row
for j in range(2,5):
          # k is in this range to place the button in that particular column
	for k in range(3):
		btn.append(Button(calc, width=6, height=2, bg='black',fg='white', 
                    font=('Helvetica',20,'bold'), bd=4,text=numberpad[i]))
  
		# sets buttons in row and column and separate them with a padding of 1 unit
		btn[i].grid(row=j, column= k, pady = 1)
		# put that number as a symbol on that button
		btn[i]["command"]=lambda x=numberpad[i]:added_value.numberEnter(x)
		i+=1

	
Clear_button = Button(calc, text=chr(67),width=6, height=2,bg='powder blue',
                      font=('Helvetica',20,'bold'), bd=4, command=added_value.Clear_Entry)
Clear_button.grid(row=1, column= 0, pady = 1)

All_Clear_Button = Button(calc, text=chr(67)+chr(69), width=6, height=2, bg='powder blue',
                          font=('Helvetica',20,'bold'),bd=4, command=added_value.All_Clear_Entry)
All_Clear_Button.grid(row=1, column= 1, pady = 1)

Square_root_button = Button(calc, text="\u221A",width=6, height=2, bg='powder blue',
                            font=('Helvetica', 20,'bold'), bd=4,command=added_value.squared)
Square_root_button.grid(row=1, column= 2, pady = 1)

Addition_button = Button(calc, text="+",width=6, height=2, bg='powder blue',
                         font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.operation("add"))
Addition_button.grid(row=1, column= 3, pady = 1)

Substraction_button = Button(calc, text="-",width=6, height=2,bg='powder blue',
                             font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.operation("sub"))
Substraction_button.grid(row=2, column= 3, pady = 1)

Multiplication_button = Button(calc, text="x",width=6, height=2,bg='powder blue',
                               font=('Helvetica',20,'bold'),bd=4,command=lambda:added_value.operation("multi"))
Multiplication_button.grid(row=3, column= 3, pady = 1)

Division_button = Button(calc, text="/",width=6, height=2,bg='powder blue',
                         font=('Helvetica',20,'bold'), bd=4,command=lambda:added_value.operation("divide"))
Division_button.grid(row=4, column= 3, pady = 1)

Zero_button = Button(calc, text="0",width=6, height=2,bg='black',fg='white', 
                     font=('Helvetica',20,'bold'), bd=4,command=lambda:added_value.numberEnter(0))
Zero_button.grid(row=5, column= 0, pady = 1)

Decimal_button = Button(calc, text=".",width=6,	height=2,bg='powder blue', 
                        font=('Helvetica',20,'bold'), bd=4,command=lambda:added_value.numberEnter("."))
Decimal_button.grid(row=5, column= 1, pady = 1)

PM_button = Button(calc, text=chr(177),width=6, height=2,bg='powder blue', 
                   font=('Helvetica',20,'bold'), bd=4,command=added_value.mathPM)
PM_button.grid(row=5, column= 2, pady = 1)

Equal_button = Button(calc, text="=",width=6, height=2,bg='powder blue', 
                      font=('Helvetica',20,'bold'), bd=4,command=added_value.sum_of_total)
Equal_button.grid(row=5, column= 3, pady = 1)


# ROW 1 of Scientific Calculator :
PI_button = Button(calc, text="pi",width=6, height=2,bg='black',fg='white',
                   font=('Helvetica',20,'bold'),bd=4,command=added_value.pi)
PI_button.grid(row=1, column= 4, pady = 1)

cos_button = Button(calc, text="Cos",width=6, height=2,bg='black',fg='white',
                    font=('Helvetica',20,'bold'),bd=4,command=added_value.cos)
cos_button.grid(row=1, column= 5, pady = 1)

tan_button = Button(calc, text="tan",width=6, height=2,bg='black',fg='white', 
                    font=('Helvetica',20,'bold'), bd=4,command=added_value.tan)
tan_button.grid(row=1, column= 6, pady = 1)

sin_button = Button(calc, text="sin",width=6, height=2,bg='black',fg='white',
                    font=('Helvetica',20,'bold'), bd=4,command=added_value.sin)
sin_button.grid(row=1, column= 7, pady = 1)


# ROW 2 of Scientitfic Calculator :
button_2PI = Button(calc, text="2pi",width=6, height=2,bg='black',fg='white', 
                    font=('Helvetica',20,'bold'),bd=4,command=added_value.tau)
button_2PI.grid(row=2, column= 4, pady = 1)

cosh_buttton = Button(calc, text="Cosh",width=6, height=2,bg='black',fg='white', 
                      font=('Helvetica',20,'bold'),bd=4,command=added_value.cosh)
cosh_buttton.grid(row=2, column= 5, pady = 1)

tanh_button = Button(calc, text="tanh",width=6, height=2,bg='black',fg='white', 
                     font=('Helvetica',20,'bold'), bd=4,command=added_value.tanh)
tanh_button.grid(row=2, column= 6, pady = 1)

sinh_button = Button(calc, text="sinh",width=6, height=2,bg='black',fg='white', 
                     font=('Helvetica',20,'bold'), bd=4,command=added_value.sinh)
sinh_button.grid(row=2, column= 7, pady = 1)


# ROW 3 of Scientific Calculator :
log_button = Button(calc, text="log",width=6, height=2,bg='black',fg='white',
                    font=('Helvetica',20,'bold'), bd=4,command=added_value.log)
log_button.grid(row=3, column= 4, pady = 1)

Exp_button = Button(calc, text="exp",width=6, height=2,bg='black',fg='white', 
                    font=('Helvetica',20,'bold'),	bd=4,command=added_value.exp)
Exp_button.grid(row=3, column= 5, pady = 1)

Mod_button = Button(calc, text="Mod",width=6,height=2,bg='black',fg='white', 
                    font=('Helvetica',20,'bold'), bd=4,command=lambda:added_value.operation("mod"))
Mod_button.grid(row=3, column= 6, pady = 1)

e_button = Button(calc, text="e",width=6, height=2,bg='black',fg='white',
              font=('Helvetica',20,'bold'), bd=4,command=added_value.e)
e_button.grid(row=3, column= 7, pady = 1)


# ROW 4 of Scientific Calculator :
log10_button = Button(calc, text="log10",width=6, height=2,bg='black',fg='white', 
                      font=('Helvetica',20,'bold'),bd=4,command=added_value.log10)
log10_button.grid(row=4, column= 4, pady = 1)

log1p_button = Button(calc, text="log1p",width=6, height=2,bg='black',fg='white',
                      font=('Helvetica',20,'bold'), bd=4,command=added_value.log1p)
log1p_button.grid(row=4, column= 5, pady = 1)

expm1_button = Button(calc, text="expm1",width=6,	height=2,bg='black',fg='white', 
                      font=('Helvetica',20,'bold'), bd = 4,command=added_value.expm1)
expm1_button.grid(row=4, column= 6, pady = 1)

gamma_button = Button(calc, text="gamma",width=6, height=2,bg='black',fg='white', 
                      font=('Helvetica',20,'bold'), bd=4,command=added_value.lgamma)
gamma_button.grid(row=4, column= 7, pady = 1)


# ROW 5 of Scientific Calculator :
log2_button = Button(calc, text="log2",width=6, height=2,bg='black',fg='white', 
                 font=('Helvetica',20,'bold'), bd=4,command=added_value.log2)
log2_button.grid(row=5, column= 4, pady = 1)

deg_button = Button(calc, text="deg",width=6, height=2,bg='black',fg='white', 
                font=('Helvetica',20,'bold'), bd=4,command=added_value.degrees)
deg_button.grid(row=5, column= 5, pady = 1)

acosh_button = Button(calc, text="acosh",width=6,	height=2,bg='black',fg='white',
                      font=('Helvetica',20,'bold'),bd=4,command=added_value.acosh)
acosh_button.grid(row=5, column= 6, pady = 1)

asinh_button = Button(calc, text="asinh",width=6, height=2,bg='black',fg='white',
                  font=('Helvetica',20,'bold'), bd=4,command=added_value.asinh)
asinh_button.grid(row=5, column= 7, pady = 1)


# this will display the the label Scientific Calculator
Display_label = Label(calc, text = "Scientific Calculator",	font=('Helvetica',30,'bold'),
                      bg='black',fg='white',justify=CENTER)
Display_label.grid(row=0, column= 4,columnspan=4)


# this is the function to EXIT from the window
def iExit():
	iExit = tkinter.messagebox.askyesno("Scientific Calculator", "Do you want to exit ?")
	if iExit>0:
		main_window.destroy()
		return


# this function will restrict the scientific calculator frame from resizing 
def Scientific():
	main_window.resizable(width=False, height=False)
	main_window.geometry("944x568+0+0")


# this function will restrict the standard calculator frame from resizing 
def Standard():
	main_window.resizable(width=False, height=False)
	main_window.geometry("480x568+0+0")


menubar = Menu(calc)

# ManuBar 1 :
filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'File', menu = filemenu)
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

# ManuBar 2 :
editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = 'Edit', menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_command(label = "Paste")
editmenu.add_separator()

main_window.config(menu=menubar)

main_window.mainloop()
