from tkinter import *;

expression = ""

# Function to update expression
def press(num):
          # pointout the global expression variable
          global expression
          # Concentation of String
          expression = expression + str(num)
          # update the expression by using set method
          equation.set(expression)
          
# Function to evaluate the final expression
def equalpress():
          # Try and except statement is used
          # for handling errors like zero division error, etc...
          try:
                    global expression
                    
                    # eval function evaluates the expression
                    # and str function convert the result into string
                    total = str(eval(expression))
                    equation.set(total)
                    # initialize the expression variable by empty string
                    expression = ""
          
          # if error is generated then handle by the except block
          except:
                    equation.set("ERROR")
                    expression = ""

# Function to clear the contents of the entry box
def clear():
          global expression
          expression = ""
          equation.set("")

# Driver Code
if __name__ == "__main__":
          # creating a GUI Window
          main_window = Tk()
          # stating the Title of the Window
          main_window.title('Simple Calculator')
          # Applying an icon to the window
          main_window.iconbitmap('calculator.ico')
          
          # StringVar() is the variable class
          # creating an instance of this class
          equation = StringVar()
          expression_field = Entry(main_window, textvariable=equation)
          expression_field.grid(columnspan=5, ipadx=75)

          # Buttons of numbers
          button1 = Button(main_window, text='1', fg='black', bg='grey', height=1, width=8, command = lambda: press(1))
          button2 = Button(main_window, text='2', fg='black', bg='grey', height=1, width=8, command = lambda: press(2))
          button3 = Button(main_window, text='3', fg='black', bg='grey', height=1, width=8, command = lambda: press(3))
          button4 = Button(main_window, text='4', fg='black', bg='grey', height=1, width=8, command = lambda: press(4))
          button5 = Button(main_window, text='5', fg='black', bg='grey', height=1, width=8, command = lambda: press(5))
          button6 = Button(main_window, text='6', fg='black', bg='grey', height=1, width=8, command = lambda: press(6))
          button7 = Button(main_window, text='7', fg='black', bg='grey', height=1, width=8, command = lambda: press(7))
          button8 = Button(main_window, text='8', fg='black', bg='grey', height=1, width=8, command = lambda: press(8))
          button9 = Button(main_window, text='9', fg='black', bg='grey', height=1, width=8, command = lambda: press(9))
          button0 = Button(main_window, text='0', fg='black', bg='grey', height=1, width=8, command = lambda: press(0))
          button00 = Button(main_window, text='00', fg='black', bg='grey', height=1, width=8, command = lambda: press(00))
          button1.grid(row=2, column=0)
          button2.grid(row=2, column=1)
          button3.grid(row=2, column=2)
          button4.grid(row=3, column=0)
          button5.grid(row=3, column=1)
          button6.grid(row=3, column=2)
          button7.grid(row=4, column=0)
          button8.grid(row=4, column=1)
          button9.grid(row=4, column=2)
          button0.grid(row=5, column=0)
          button00.grid(row=5, column=1)

          # Button of Clear
          clear_button = Button(main_window, text='AC', fg='black', bg='grey', height=1, width=8, command = clear)
          clear_button.grid(row=2, column=3)
          
          # Button of Addition
          addition = Button(main_window, text='+', fg='black', bg='grey', height=1, width=8, command = lambda: press("+"))
          addition.grid(row=3, column=3)

          # Buttion of Substraction
          substraction = Button(main_window, text='-', fg='black', bg='grey', height=1, width=8, command = lambda: press("-"))
          substraction.grid(row=4, column=3)

          # Button of Multiplication
          multiplication = Button(main_window, text='x', fg='black', bg='grey', height=1, width=8, command = lambda: press("x"))
          multiplication.grid(row=5, column=3)

          # Button of Division
          division = Button(main_window, text='/', fg='black', bg='grey', height=1, width=8, command = lambda: press("/"))
          division.grid(row=6, column=3)

          # Button of Decimal
          decimal = Button(main_window, text='.', fg='black', bg='grey', height=1, width=8, command = lambda: press("."))
          decimal.grid(row=5, column=2)

          # Button of Equal-To
          equal_to = Button(main_window, text='=', fg='black', bg='grey', height=1, width=8, command=equalpress)
          equal_to.grid(row=6, column=2)

          # Button of pie
          pie = Button(main_window, text='π', fg='black', bg='grey', height=1, width=8)
          pie.grid(row=6, column=1)

          # Button of Square Root
          square_root = Button(main_window, text='√', fg='black', bg='grey', height=1, width=8)
          square_root.grid(row=6, column=0)



          main_window.mainloop()