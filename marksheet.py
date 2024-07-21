# Python program to create a
# GUI mark sheet using tkinter

from tkinter import *

# creating a new tkinter window
master = Tk()

# assigning a title
master.title("MARKSHEET")

# specifying geometry for window size
master.geometry("700x300")


# declaring objects for entering data
entry_name = Entry(master)
entry_course_name = Entry(master)
entry_enrollment_no = Entry(master)


# function to display the total subject credits 
# total credits and SGPA according
# to grades entered
def display():

	# Variable to store total marks
	total = 0

	# 10*number of subject credits and give total credits for grade A
	if grade_entry_1.get() == "A":

		# grid method is used for placing the widgets at respective positions in table like structure .
		Label(master, text="40").grid(row=3, column=5)
		total += 40

	# 9*number of subject credits give total credits for grade B
	if grade_entry_1.get() == "B":
		Label(master, text="36").grid(row=3, column=5)
		total += 36

	# 8*number of subject credits give total credits for grade C
	if grade_entry_1.get() == "C":
		Label(master, text="32").grid(row=3, column=5)
		total += 32

	# 7*number of subject credits give total credits for grade D
	if grade_entry_1.get() == "D":
		Label(master, text="28").grid(row=3, column=5)
		total += 28

	# 6*number of subject credits give total credits for grade P
	if grade_entry_1.get() == "P":
		Label(master, text="24").grid(row=3, column=5)
		total += 24

	# 0*number of subject credits give total credits for grade F
	if grade_entry_1.get() == "F":
		Label(master, text="0").grid(row=3, column=5)
		total += 0

          # ======================================================================================
          
	# Similarly doing with other objects
	if grade_entry_2.get() == "A":
		Label(master, text="30").grid(row=4, column=5)
		total += 30
  
	if grade_entry_2.get() == "B":
		Label(master, text="27").grid(row=4, column=5)
		total += 27
  
	if grade_entry_2.get() == "C":
		Label(master, text="24").grid(row=4, column=5)
		total += 24
  
	if grade_entry_2.get() == "D":
		Label(master, text="21").grid(row=4, column=5)
		total += 21
  
	if grade_entry_2.get() == "P":
		Label(master, text="18").grid(row=4, column=5)
		total += 18
  
	if grade_entry_2.get() == "F":
		Label(master, text="0").grid(row=4, column=5)
		total += 0

          # ======================================================================================
          
	# Similarly doing with other objects
	if grade_entry_3.get() == "A":
		Label(master, text="40").grid(row=5, column=5)
		total += 40
  
	if grade_entry_3.get() == "B":
		Label(master, text="36").grid(row=5, column=5)
		total += 36

	if grade_entry_3.get() == "C":
		Label(master, text="32").grid(row=5, column=5)
		total += 30
  
	if grade_entry_3.get() == "D":
		Label(master, text="28").grid(row=5, column=5)
		total += 28
  
	if grade_entry_3.get() == "P":
		Label(master, text="24").grid(row=5, column=5)
		total += 24
  
	if grade_entry_3.get() == "F":
		Label(master, text="0").grid(row=5, column=5)
		total += 0

          # ======================================================================================
          
	# Similarly doing with other objects
	if grade_entry_4.get() == "A":
		Label(master, text="40").grid(row=6, column=5)
		total += 40
  
	if grade_entry_4.get() == "B":
		Label(master, text="36").grid(row=6, column=5)
		total += 36
  
	if grade_entry_4.get() == "C":
		Label(master, text="32").grid(row=6, column=5)
		total += 32
  
	if grade_entry_4.get() == "D":
		Label(master, text="28").grid(row=6, column=5)
		total += 28
  
	if grade_entry_4.get() == "P":
		Label(master, text="24").grid(row=6, column=5)
		total += 24
  
	if grade_entry_4.get() == "F":
		Label(master, text="0").grid(row=6, column=5)
		total += 0

          # ======================================================================================
          
	# Similarly doing with other objects
	if grade_entry_5.get() == "A":
		Label(master, text="20").grid(row=7, column=5)
		total += 20
  
	if grade_entry_5.get() == "B":
		Label(master, text="18").grid(row=7, column=5)
		total += 18
  
	if grade_entry_5.get() == "C":
		Label(master, text="16").grid(row=7, column=5)
		total += 16
  
	if grade_entry_5.get() == "D":
		Label(master, text="14").grid(row=7, column=5)
		total += 14
  
	if grade_entry_5.get() == "P":
		Label(master, text="12").grid(row=7, column=5)
		total += 12
  
	if grade_entry_5.get() == "F":
		Label(master, text="0").grid(row=7, column=5)
		total += 0

          # ======================================================================================
          
	# Similarly doing with other objects
	if grade_entry_6.get() == "A":
		Label(master, text="40").grid(row=8, column=5)
		total += 40
  
	if grade_entry_6.get() == "B":
		Label(master, text="36").grid(row=8, column=5)
		total += 36
  
	if grade_entry_6.get() == "C":
		Label(master, text="32").grid(row=8, column=5)
		total += 32
  
	if grade_entry_6.get() == "D":
		Label(master, text="28").grid(row=8, column=5)
		total += 28
  
	if grade_entry_6.get() == "P":
		Label(master, text="24").grid(row=8, column=5)
		total += 24
  
	if grade_entry_6.get() == "F":
		Label(master, text="0").grid(row=8, column=5)
		total += 0
  
  
	# to display total credits
	Label(master, text=str(total)).grid(row=12, column=5)

	# to display SGPA
	Label(master, text=str(total/21)).grid(row=13, column=5)

# end of display function

# label to enter name
Label(master, text="Name :").grid(row=0, column=0)

# label for registration number
Label(master, text="Course :").grid(row=0, column=3)

# label for roll Number
Label(master, text="Roll.No :").grid(row=1, column=0)

# labels for serial numbers
Label(master, text="Srl.No").grid(row=2, column=0)
Label(master, text="1").grid(row=3, column=0)
Label(master, text="2").grid(row=4, column=0)
Label(master, text="3").grid(row=5, column=0)
Label(master, text="4").grid(row=6, column=0)
Label(master, text="5").grid(row=7, column=0)
Label(master, text="6").grid(row=8, column=0)

# labels for subject names
Label(master, text="Subject").grid(row=2, column=1)
Label(master, text="Object Oriented Programing").grid(row=3, column=1)
Label(master, text="Data Structures and Algorithms").grid(row=4, column=1)
Label(master, text="Relational Database Management System").grid(row=5, column=1)
Label(master, text="Fundamentals of Statistics").grid(row=6, column=1)
Label(master, text="Communication - II").grid(row=7, column=1)
Label(master, text="Environmental Studies").grid(row=8, column=1)

# labels for subject codes
Label(master, text="Subject Code").grid(row=2, column=2)
Label(master, text="CMP211").grid(row=3, column=2)
Label(master, text="CMP212").grid(row=4, column=2)
Label(master, text="CMP213").grid(row=5, column=2)
Label(master, text="MAT201").grid(row=6, column=2)
Label(master, text="COM209").grid(row=7, column=2)
Label(master, text="ENV102").grid(row=8, column=2)

# label for grades
Label(master, text="Grade").grid(row=2, column=3)
grade_entry_1 = Entry(master)
grade_entry_2 = Entry(master)
grade_entry_3 = Entry(master)
grade_entry_4 = Entry(master)
grade_entry_5 = Entry(master)
grade_entry_6 = Entry(master)
grade_entry_1.grid(row=3, column=3)
grade_entry_2.grid(row=4, column=3)
grade_entry_3.grid(row=5, column=3)
grade_entry_4.grid(row=6, column=3)
grade_entry_5.grid(row=7, column=3)
grade_entry_6.grid(row=8, column=3)


# labels for subject credits
Label(master, text="Subject Credit").grid(row=2, column=4)
Label(master, text="4").grid(row=3, column=4)
Label(master, text="3").grid(row=4, column=4)
Label(master, text="4").grid(row=5, column=4)
Label(master, text="4").grid(row=6, column=4)
Label(master, text="2").grid(row=7, column=4)
Label(master, text="4").grid(row=8, column=4)


Label(master, text="Credit obtained").grid(row=2, column=4)

# taking entries of name, reg, roll number respectively
entry_name = Entry(master)
entry_course_name = Entry(master)
entry_enrollment_no = Entry(master)

# organizing them in the grid
entry_name.grid(row=0, column=1)
entry_course_name.grid(row=0, column=4)
entry_enrollment_no.grid(row=1, column=1)

# button to display all the calculated credit scores and sgpa
button1 = Button(master, text="submit", bg="green", command=display)
button1.grid(row=12, column=1)


Label(master, text="Total credit").grid(row=12, column=4)
Label(master, text="SGPA").grid(row=13, column=4)


master.mainloop()